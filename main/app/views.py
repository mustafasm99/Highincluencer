from asyncio.windows_events import NULL
from django.shortcuts import render
from django.contrib.auth.models import User 
from .models import *
import requests
from django.core.files.base import ContentFile
# Create your views here.

# function for send telegram messages 
import telepot
def telem(username,message):
    token = "5689270064:AAGmTX_XrHnHn49ohQbAhJ6RQ_9PGFoLY0s"
    bot = telepot.Bot(token)
    data = bot.getUpdates()
    
    for i in data:
        Tusername = i['message']['from']['username']
        id = i['message']['from']['id']
        if Tusername == username:
            bot.sendMessage(id,message)
            break
#get influncer from api 
def api(user):
    import requests
    url = "https://instagram-profile1.p.rapidapi.com/getprofile/"+str(user)

    headers = {
        "X-RapidAPI-Key": "c3a7b0fbc3msh25d8b0397c4563cp11e098jsnf1d5daf22469",
        "X-RapidAPI-Host": "instagram-profile1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

def main(e,*args,**kwargs):
    code = str(kwargs.get('code'))
    try:
        influencer = Influencer.objects.get(code=code)
        e.session['code'] = influencer.id
    except:
        pass
    print(e.session.get_expiry_date())
    d1 = Influencer.objects.all()
    d2 = Brand.objects.all()
    for i in d1:
        if str(e.user) == str(i.user):
            d1="Influencer"
        else:
            d1 = "none"
    for i in d2:
        if str(e.user) == str(i.user):
            d2="Brand"
        else:
            d2= "none"
            
    return render(e,'main.html',{
        "d1":d1,
        "d2":d2,
    })


## main function for Descovery ## 
def Influencer_descovery(e):
    inf = Influencer.objects.all()

    try:
        brand = Brand.objects.get(user = e.user)
        list = saveInfluncer.objects.filter(brand = brand).all()
    except:
        list = "none"
    if e.method == 'GET':
            return render(e,'influencer/main.html',{
            "data":inf,
            "list":list,
            })
    else:
        if e.POST.get('most','none') != 'none':
            inf = Influencer.objects.order_by("-followers")
        elif e.POST['lest']:
            inf = Influencer.objects.order_by("followers")
        else:
            return render(e,'influencer/main.html',{
                    "data":inf,
                })
        return render(e,'influencer/main.html',{
                    "data":inf,
                    "list":list,
                })
        


def influencer(e):
    users = Influencer.objects.all()
    try:
        brand = Brand.objects.get(user = e.user)
        slist = saveInfluncer.objects.filter(brand = brand).first()
        print(brand,slist,"hello")
        return render(e,"influencer/main.html",{
            "data":users,
            "list":slist,
        })
    
    except:
        return render(e,"influencer/main.html",{
            "data":users,
        })
        
    
    