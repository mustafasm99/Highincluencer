#Brand file that contain all image's
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#Brand all requests 

# home page of the prand
@login_required
def dashboard(e):
    brand = Brand.objects.filter(user = e.user).first()
    rqu = requests.objects.filter(brand = brand.id).all()
    print(rqu ,e.user.id)
    return render(e,'brand/dashboard.html',{
        'data':rqu,
    })

# create stor for the brand 
@login_required
def CStor(e):
    if e.method == 'POST':
        try:
            if e.POST['create_item']:
                brand = Brand.objects.get(user = e.user)
                shop = shops.objects.filter(woner = brand).first()
                print(shop , e.user , e.user.id)
                name = e.POST['name']
                price = e.POST['price']
                qt = e.POST['qt']
                image = e.FILES['image']
                new = item(name = name , price=price,item_image = image,quintity = qt , shop=shop)
                new.save()
        except:
            if e.POST['Create_Stor']:
                brand = Brand.objects.get(user = e.user)
                name = e.POST['name']
                new = shops(Name=name , woner = brand)
                new.save()
                return redirect('CStore')
    data = shops.objects.all()
    for i in data:
        if str(e.user) == str(i.woner):
            items = item.objects.filter(shop = i.id)
            return render(e,'brand/CStroe.html',{
                'data':items,
                'flag':True,
            })    
    return render(e,'brand/CStroe.html',{})

def updateItem(e,id):
    pass 

# CRUDS
@login_required
def deleteItem(e,id):
    x = item.objects.get(id = id)
    x.delete()
    return redirect('CStore')

@login_required
def item_offers(e):
    if e.method == 'POST':
        data = item_offer.objects.get(id = e.POST['id'])
        if data.accept == True:
            data.accept = False
        else:data.accept = True
        data.save()
        return redirect('itemoffers')
    woner = Brand.objects.get(user = e.user)
    shop = shops.objects.filter(woner = woner).first()
    items = item.objects.filter(shop = shop).all()
    x=item_offer.objects.filter(s_item__id__in = items).all().order_by('-time')
    return render(e,'Brand/stor_offer.html',{
        'data':x,
    })

@login_required
def invoice(e):
    brand = Brand.objects.get(user = e.user)
    check = checkout.objects.all()
    data = []
    for i in check:
        if i.xitem.shop.woner == brand:
            data.append(i)
    return render(e,'Brand/invoce.html',{
        'data':data
    })

# to crate the save list 

@login_required
def create_Slist(e):
    brn = Brand.objects.get(user = e.user)
    new = saveInfluncer(brand = brn,title = e.POST['title'])
    new.save()
    return redirect('branddashboard')


# function to save influencer  in list 
@login_required
def save_inList(e , id):
    brand = Brand.objects.get(user = e.user)
    influencer = Influencer.objects.get(id = id)
    savelis = saveInfluncer.objects.filter(id = e.POST['listName']).first()
    if influencer in savelis.infl.all():
        savelis.infl.remove(influencer)
    else:
        savelis.infl.add(influencer)
    savelis.save()
    return redirect('inf')


# delete from saves list 
def delete_from_list(e,list,inf):
    slist = saveInfluncer.objects.get(id = int(list))
    infe = Influencer.objects.get(id = inf)
    slist.infl.remove(infe)
    return redirect('listM')
    
    

# to delete the save list 
@login_required
def delete_list (e,id):
    
    saveInfluncer.objects.get(id = id).delete()
    return redirect ('listM')
   
# update save list 
@login_required
def update_slist(e,id):
     name = e.POST['title']
     x = saveInfluncer.objects.get(id = id)
     x.title = name
     x.save()
     
    
@login_required
def RequestInfluncer(e):
    brand = Brand.objects.get(user = e.user)
    inf = Influencer.objects.filter(id = e.POST['id']).first()
    oldRequestCheck = influncerRequest.objects.filter(
        maker = brand,
        receiver = inf,
    ).first()
    if oldRequestCheck:
        messages.add_message(e,messages.INFO,'You Already have sent A Request.')
        return redirect('inf')
    else:
        new = influncerRequest(maker = brand , receiver = inf)
        new.save()
        return redirect('inf')
    

##### list mangement function #######
@login_required
def list_management(e):
    if e.method == 'POST':
        print("posting")
        if e.POST.get('addlist','none') != 'none':
            # print('creating' , e.POST)
            create_Slist(e)
        elif e.POST.get('delete','none') != 'none':
            delete_list(e,e.POST['delete'])
            # print(e.POST)
        elif e.POST.get('Edit','none') != 'none':
            update_slist(e,e.POST['Edit'])
        elif e.POST.getlist('deleteOne' , 'none') != 'none':
            ll = e.POST['deleteOne'].split(',')
            li = ll[1]
            infl = ll[0]
            delete_from_list(e,li,infl)
        elif e.POST.getlist('id' , 'none') != 'none':
            infl = e.POST.getlist('id')[0]
            # e.POST['id'] = infl
            RequestInfluncer(e)
            
            
            
    brand = Brand.objects.get(user = e.user)
    lists = saveInfluncer.objects.filter(brand = brand).all()
    return render(e,"Brand/listmanagement.html",{
        'lists':lists,
    })
    
#   functon for each list  to return list 
@login_required
def xlist(e,id):
    l = saveInfluncer.objects.get(id = id)
    return render(e,'Brand/List.html',{'data':l})