from asyncio.windows_events import NULL
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth.decorators import login_required
from coupon.models import *
from django.contrib import messages
from django.utils import timezone

def store(e):
    data = item.objects.all()
    return render(e,'store/main.html',{
        'data':data,
    })

def s_item(e,*args , **kwargs):
    sitem = item.objects.get(id=kwargs.get('id'))
    return render(e,'store/item.html' ,{
        'data':sitem,
    })

def addToCart(e):
    items = e.POST['item']
    xitem = item.objects.get(id = items)
    try:
        xcart = cart.objects.filter(adder = e.user).first()
        if not xcart:
            new = cart(adder = e.user)
            new.save()
            new.items.add(xitem)
            return redirect('stor')
        xcart.items.add(xitem)
        return redirect('stor')
    except:
        xcart = cart(
            adder = e.user ,
            items = xitem ,
        )
        xcart.save()
        return redirect('stor')

# # # # bay now  # # # # # 

def byNow(e):
        now = timezone.now()
        phone_number = e.POST['phone']
        email = e.POST['email']
        loc = e.POST['loc']
        note = e.POST['note']
        cop = Coupon.objects.get(
            code__iexact = e.POST['cop'],
            valid_from__lte = now,
            valid_to__gte = now,
            active = True
        )
        if e.user.is_anonymous:
            name = e.POST['name']
            qt = 0.0
            for n,i in enumerate(e.POST.getlist('item')):
                xitem = item.objects.get(id = i)
                qt = e.POST.getlist('qt')[n]
                if qt =='':
                    qt=1
                total =xitem.price * float(qt)
                
                new = checkout(
                    xitem = xitem,
                    name = name,
                    email = email,
                    phone_number = phone_number,
                    locathion = loc,
                    quantity = qt,
                    copone = cop,
                    note = note,
                    total_price = total,
                )
                new.save()
            messages.add_message(e,messages.INFO,'we will contact with you check your email')
            return redirect('stor')

        else:
            name = e.user.username
            cartx = cart.objects.get(adder = e.user)
            total = 0
        
            for n,i in enumerate(cartx.items.all()):
                qt = e.POST.getlist('qt')[n]
                if qt == '':
                    qt = 1
                total = i.price * int(qt)
                new = checkout(
                        xitem = i,
                        name = name,
                        email = email,
                        locathion = loc,
                        quantity = qt,
                        copone = cop,
                        note = note,
                        total_price = total,
                        phone_number = phone_number,
                    )
                new.save()
                cartx.delete()
        
        return redirect('stor')

#  # # # Cart for users items #  ## # ## # 

@login_required
def Cart(e):
    try:
        data = cart.objects.get(adder = e.user)
        if e.method == 'POST':
            if e.POST.get('delete'):
                xitem = item.objects.get(id = int(e.POST['delete']))
                itemInCart = cart.objects.get(adder = e.user)
                itemInCart.items.remove(xitem)
                return redirect('cart')
            if e.POST.get('baynow'):
                print(e.POST)
                byNow(e)
                return redirect('cart')
        return render(e,'store/cart.html',{
            'data':data
        })
    except:
         return render(e,'store/cart.html',{})