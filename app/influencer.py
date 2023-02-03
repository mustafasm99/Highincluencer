from django.db.models import Q
from types import NoneType
from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.models import User 
from .models import *
from django.contrib import messages
from .views import api, influencer
from django.core.files.base import ContentFile
import requests
from datetime import datetime
import datetime

def infDashboard(e):
    return render(e,'influencer/dashboard.html',{})

def influencerpage(e,username):
    su = User.objects.get(username = username)
    data = Influencer.objects.filter(user = su.id).first()
    return render(e,'Influencer/influencer.html',{
        'data':data,
    })

def Item_work_with(e):
    infl = Influencer.objects.get(user = e.user)
    itemre = item_offer.objects.filter(influencer=infl).all()
    return render(e,'influencer/item_work_with.html',{
        'data':itemre,
    })

def InfAccount(e):
    inf = Influencer.objects.get(user = e.user)
    post = Post.objects.filter(influencer = inf).all()
    if not inf:
        messages.add_message(e,messages.INFO,'you dont have in account')
        return redirect('main')
    return render(e,'influencer/Account.html',{
        'data':inf,
        'post':post
    })

def updateInf(e):
    if e.method == 'POST':
        inf = Influencer.objects.get(user = e.user)
        newdata = api(e.user.username)
        inf.followers = newdata['followers']
        inf.following = newdata['following']
        inf.post_number = newdata['lastMedia']['count']
        profileImage = requests.get(newdata['profile_pic_url_hd_proxy'])
        inf.image.delete()
        inf.image.save(content=ContentFile(profileImage.content),name=str(inf.user),save=True)
        inf.text = newdata['bio']

        posts = Post.objects.filter(influencer = inf).all()
        post_count = len(newdata['lastMedia']['media'])
        for i in range(post_count):
            try:
                date = datetime.fromtimestamp(newdata['lastMedia']['media'][i]['timestamp'])
                post =  Post(
                            influencer = inf , 
                            like = newdata['lastMedia']['media'][i]['like'],
                            is_video = newdata['lastMedia']['media'][i]['is_video'],
                            comment_count = newdata['lastMedia']['media'][i]['comment_count'],
                            caption = newdata['lastMedia']['media'][i]['caption'] ,
                            code = newdata['lastMedia']['media'][i]['shortcode'],
                            time = date,
                        )
                post.save()
                media = requests.get(newdata['lastMedia']['media'][i]['display_url_proxy'])
                post.media.save(
                    content=ContentFile(media.content),
                    name=str(newdata['lastMedia']['media'][i]['shortcode']),
                    save=True
                    )
            except:
                pass
        return redirect('infacc')
    messages.add_message(e,messages.INFO,'Error')
    return redirect('infacc')

#|########################################|
#|########## Analysis Function ###########|
#|########################################|

def analysis(e,id):
    if e.user.is_anonymous == True:
        return render(e,'NoUser.html')
    data = Influencer.objects.get(id = id)
    posts = Post.objects.filter(influencer=data).all().order_by('-time')
    slist = saveInfluncer.objects.filter(brand = Brand.objects.get(user = e.user)).first()
    if data in slist.infl.all():
        saved = True
    else:
        saved = False
    
    sg = []
    for i in data.tag.all():
        x = Influencer.objects.filter(tag__title__contains=i.title).all()
        for  j in x:
            if j not in sg and j.user.username != data.user.username:
                sg.append(j)
    x=0.0
    totalLike = 0
    totalComment = 0
    names = ""
    eng = 0.0
    ###########################
    ####### Posts analysis ####
    ###########################
    for i in posts:
        x += (i.like + i.comment_count)
        totalLike +=i.like
        totalComment +=i.comment_count
        names+=str(i.time)[:10]+","
        
    # math exprathion 
    if len(posts) == 0 :
       x=(x/1)*0.1
       averageComments = totalComment/1
       averageLikes = totalLike/1
       Comment_Ratio = (averageComments/1)*100
       
    else:
        x=((x/len(posts))/data.followers)*100
        averageComments = totalComment/len(posts)
        averageLikes = totalLike/len(posts)
        Comment_Ratio = (averageComments/averageLikes)*100
    followersRatio = (data.following / data.followers)*100
    master = masterTable.objects.filter(infl = data).order_by('-time')
    
    ###########Last month Data ###################
    
    
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    lastMonthData = masterTable.objects.filter(
        Q(infl = data) & Q(time=last_month)
    )
    if len(lastMonthData) == 0:
        lastMonthData = master.last()
    else:
        lastMonthData = lastMonthData.first()
    dic =  (master.first().followers-lastMonthData.followers)/master.first().followers
    newNumber = (dic*master.first().followers)+master.first().followers
    forsixmonth = ''
    sixmonth =''
    from dateutil import relativedelta
    for i in range(1,7):
        forsixmonth +=str(abs(newNumber*(i)))+','
        sixmonth += str(today + relativedelta.relativedelta(months=i,day=1))+','
   
    hname = ""
    daly ="";temp=[];dalyLab=""
    avgdaly =0.0
    for i in master:
        hname+=str(i.time)[:10]+','
        avgdaly += int((i.following/i.followers)*100)
        if len(temp) == 0:
            if type(i.followers)!=NoneType and int(i.followers) > 0:
                temp.append(i.followers)
                
        else:
           
            if temp[0] > 0:
                xdly = temp[0] - i.followers
                daly+=str(xdly)+','
                dalyLab+=str(i.time.strftime('%Y:%m:%d'))+','
            else:continue

    wavg = int(avgdaly*7);mavg = int(avgdaly*30)
    disposts = Post.objects.order_by('-time').all()[:12]
    return render(e,'influencer/analysis.html',{
        'data':data,
        're':str(x)[:4],
        'posts':posts,
        'disposts':disposts,
        'avarageLikes':str(averageLikes)[:4],
        'avarageComments':averageComments,
        'names':names,
        'totalLike':totalLike,
        'totalComment':totalComment,
        'commintRitio':str(Comment_Ratio)[:4],
        'FR':str(followersRatio)[:4],
        'mt':master,
        'mtn':hname,
        'sg':sg,
        'daly':daly,
        'dl':dalyLab,
        'six':forsixmonth,
        'sm':sixmonth,
        'dv':avgdaly,'wv':wavg,'mv':mavg,
        'saved':saved
    })

def get_post(e):
    id = e.POST['id']
    x = Post.objects.get(id=id).media.url
    return HttpResponse(x)

