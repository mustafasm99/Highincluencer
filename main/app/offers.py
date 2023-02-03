from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def offer(e):
    data = offers.objects.order_by("-startTime")
    return render(e,'offers/alloffers.html',{
        'data':data,
    })

@login_required
def makeoffers(e):
    cat = category.objects.all()
    if e.method == 'POST':
        name = e.POST['name']
        text = e.POST['text']
        cat = e.POST['cat']
        date = e.POST['date']
        new = offers(title=name,text=text ,woner=Brand.objects.filter(user = e.user).first(),endTime=date)
        new.save()
        new.categorys.add(cat)
        messages.add_message(e,messages.INFO,"your offer's submited ")
        return redirect('makeoffers')
    data = offers.objects.filter(woner = Brand.objects.filter(user = e.user).first()).all()
    return render(e,'offers/makeoffer.html',{
        'data':data ,
        'cat':cat
    })

# make offer for item #

@login_required
def maike_item_offer(e):
    id = e.POST['offer']
    sitem= item.objects.filter(id = id).first()
    infl = Influencer.objects.get(user = e.user)
    new = item_offer(s_item = sitem , influencer = infl)
    new.save()
    messages.add_message(e,messages.INFO,"your request has been sened")
    return redirect('stor')



@login_required
def deleteoffer(e,id):
    x = offers.objects.filter(id = id).first()
    x.delete()
    return redirect('makeoffers')

@login_required
def updateoffer(e,id):
    x = offers.objects.filter(id = id).first()
    name = e.POST['name']
    text = e.POST['text']
    cat = e.POST['cat']
    x.title = name ; x.text = text ; x.categorys = cat
    x.save()
    return redirect('makeoffers')

@login_required
def send_request(e):
    #try:
        br = e.POST['woner']
        bra = User.objects.get(username = br)
        brand = Brand.objects.get(user = bra.id)
        inf = Influencer.objects.get(user = e.user)
        offer = offers.objects.get(id = e.POST['offer'])
        new = requests(offer = offer)
        new.save()
        new.brand.add(brand)
        new.influencer.add(inf)
        messages.add_message(e,messages.INFO,"your request has been sened")
        return redirect('alloffers')
    # except:
    #     messages.add_message(e,messages.INFO,"your request has been sened")
    #     return redirect('alloffers')

@login_required
def delete_request(e,id):
    x = requests.objects.filter(id = id).first()
    x.delete()
    return redirect('branddashboard')

@login_required
def Accept_request(e):
    id = e.POST['id']
    x = requests.objects.filter(id = id).first()
    if x.Accept == False:
        x.Accept=True
    else:
        x.Accept = False
    x.save()
    return redirect('branddashboard')

def Create_category(e):
    new = category(title = e.POST['Ncat'])
    new.save()
    messages.add_message(e,messages.INFO,"New Category has add")
    return redirect(e.path)