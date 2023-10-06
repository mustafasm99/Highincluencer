from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth.decorators import login_required
from coupon.models import *
from django.contrib import messages
from django.utils import timezone


def stor_by_link(e , brand):
    try:
        xcart = cart.objects.get(session_id = e.session['noneuser'])
    except:
        e.session.modified = True
        e.session['noneuser'] = str(uuid.uuid4())
        e.session['store'] = str(brand)
        xcart = cart.objects.create(session_id = e.session['noneuser'])
        
    if e.method == 'POST':
        if e.POST.get('item' , 'none') != 'none':
            addToCart(e)
            return redirect('stor')
    br = Brand.objects.get(user = User.objects.filter(username = brand).first())
    shp = shops.objects.get(woner = br)
    data = item.objects.filter(shop = shp).all()
    print(data , shp ,brand)
    if not e.user.is_anonymous:
        if Brand.objects.filter(user = e.user).first():
            shop = shops.objects.get(woner = Brand.objects.get(user = e.user))
            data = item.objects.filter(shop = shop).all()
    return render(e,'store/main.html',{
        'data':data,
        'store':shp
    })

@login_required
def store(e):
    admin = False
    if e.method == 'POST':
        if e.POST.get('item' , 'none') != 'none':
            addToCart(e)
            return redirect('cart')
    else:
        try:
            brand = Brand.objects.filter(user =e.user).first()   
            data = item.objects.all()
            shp = shops.objects.get(woner = brand)
            if e.user == shp.woner.user:
                admin = True
            # if not e.user.is_anonymous:
            #     if Brand.objects.filter(user = e.user).first():
            #         shop = shops.objects.get(woner = Brand.objects.get(user = e.user))
            #         data = item.objects.filter(shop = shop)
            return render(e,'store/main.html',{
                'data':data,
                'store':shp,
                'admin':admin,
            })
        except:
            return redirect('storBtLink',e.session['store'])

def s_item(e,*args , **kwargs):
    sitem = item.objects.get(id=kwargs.get('id'))
    return render(e,'store/item.html' ,{
        'data':sitem,
    })

def addToCart(e):
    print("added" , e.session['store'])
    xitem = item.objects.get(id = e.POST['item'])
    try:
        xcart = cart.objects.get(adder = e.user)
        xcart.items.add(xitem)
        print(xcart)
        return redirect('stor')
    except:
        try:
            xcart = cart.objects.get(session_id = e.session['noneuser'])
        except:
            e.session['noneuser'] = str(uuid.uuid4())
            xcart = cart.objects.create(session_id = e.session['noneuser'])
        xcart.items.add(xitem)
        brand = e.session['store']
        print(e.session['store'] , brand)
        return redirect('storBtLink' , e.session['store'])

# # # # bay now  # # # # # 

def byNow(e):
        now = timezone.now()
        name = e.POST['name']
        phone_number = e.POST['phone']
        email = e.POST['email']
        loc = e.POST['city']
        loc2 = e.POST['current_city']
        note = e.POST['note']
        if e.POST.get('cop' , 'none') != 'none':
            cop = Coupon.objects.filter(
                code__iexact = e.POST.get('cop' , 'none'),
                valid_form__lte = now,
                valid_to__gte = now,
                active = True
            ).first()
        try:
            cartx = cart.objects.get(adder = e.user)
        except:
            if cart.objects.filter(session_id = e.session['noneuser']).exists():
                cartx = cart.objects.get(session_id = e.session['noneuser'])
            else:
                e.session['noneuser'] = str(uuid.uuid4())
                cartx = cart.objects.create(session_id = e.session['noneuser'])
        sum = 0
        for i in e.session['qt']:
            sum+=int(i)
        new = checkout(
                name = name,
                email = email,
                city = loc,
                current_city = loc2,
                quantity = sum,
                copone = cop,
                note = note,
                total_price = e.session['total'],
                phone_number = phone_number,
            )
        new.save()
        new.xitem.set(cartx.items.all())
        index = 0
        for i in cartx.items.all():
            if int(e.session['qt'][index]) < i.quintity:
                i.quintity -= int(e.session['qt'][index])
            else:
                messages.add_message(e,messages.INFO,' الطلب خارج الكميه المتوفره ')
                return redirect('storBtLink' , e.session['store'])
            i.sell_num += 1
            cartx.items.remove(i)
            index+=1
        messages.add_message(e,messages.INFO,'we will contact with you check your email')
        return redirect('storBtLink' , e.session['store'])

#  # # # Cart for users items #  ## # ## # 


def Cart(e):
    # try:
        try:
            shop = shops.objects.get(woner = Brand.objects.get(user = e.user))
            data = cart.objects.get(adder = e.user)
        except:
            shop = shops.objects.get(woner = Brand.objects.get(user = User.objects.get(username = e.session['store'])))
            data = cart.objects.get(session_id = e.session['noneuser'])
        if e.method == 'POST':
            index = 0
            total = 0
            if e.POST.get('next' , 'none') != 'none':
                for items in data.items.all():
                    total += items.price * int(e.POST.getlist('qt')[index])
                    index +=1
                if e.POST.get('shipping' , 'none') != 'none':
                    total += float(e.POST['shipping'])
                else:
                    total += float(shop.shiping)
                e.session['total'] = total
                e.session['qt'] = e.POST.getlist('qt')
                print(e.session)
                return render(e,'store/checkout.html',{
                    
                })
            if e.POST.get('delete'):
                xitem = item.objects.get(id = int(e.POST['delete']))
                try:
                    itemInCart = cart.objects.get(adder = e.user)
                except:
                    itemInCart = cart.objects.get(session_id = e.session['noneuser'])
                itemInCart.items.remove(xitem)
                return redirect('cart')
            if e.POST.get('bynow'):
                byNow(e)
                return redirect('cart')
        return render(e,'store/cart.html',{
            'data':data,
            "stor":shop
        })
    # except:
    #      return render(e,'store/cart.html',{})
    
    
    
# function for testing outside templeates 
def aside(e):
    return render(e , 'store/AdminAside.html')

@login_required
def editlog(e):
    data = shops.objects.get(woner = Brand.objects.get(user = e.user))
    if e.method == "POST":
        data.icon = e.FILES['logo']
        data.save()
        return redirect('stor')
    return render(e,"store/Edit/logo.html" , {"data":data})

@login_required
def editCovers(e):
    if e.method == "POST":
        print(e.method)
    data = shops.objects.get(woner = Brand.objects.get(user = e.user))
    return render(e,'store/Edit/cover.html' , {'store':data})