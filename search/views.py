from django.shortcuts import render,redirect
from app.models import Influencer
from app.models import masterTable
from app.models import Post
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import *
# Create your views here.
from app.views import api
import requests
from django.core.files.base import ContentFile

# if users earch for in out side influncer
def search_inf(e,infl):
    if e.method == 'POST':
        if e.POST.get('search' , 'none') != 'none':
            return redirect('search' , e.POST['dissearch'])
    users = User.objects.filter(username__contains = infl)
    alldata = Influencer.objects.filter(user__in = users)
    if len(alldata) == 0:
        NewData = api(infl)
        if NewData.get('error') == 'true':
            messages.add_message(e,messages.INFO , 'we could not found this user in Instagram try agin later')
            return redirect('inf')
        NewUSer = User.objects.create(
            username = NewData['username'],
            first_name = NewData['full_name']
        )
        NewUSer.set_password('sm99SM99')
        NewUSer.save()
        NewInf = Influencer(
            user = NewUSer,
            following = NewData['following'],
            followers = NewData['followers'],
            post_number = NewData['lastMedia']['count'],
            Active = False,
            text = NewData['bio'],
            block = False,
        )
        NewInf.save()
        image = requests.get(NewData['profile_pic_url_proxy'])
        NewInf.image.save(content=ContentFile(image.content),name=str(NewInf.user),save=True)
        for i in NewData['lastMedia']['media']:
                newposts = Post.objects.create(
                caption = i['caption'],
                comment_count = i['comment_count'],
                like = i['like'],
                is_video = i['is_video'],
                code = i['shortcode'],
                influencer = NewInf
                )
                newposts.media.save(
                content=ContentFile(requests.get(i['display_url_proxy']).content),
                name=newposts.code,
                save=True    
                )
        masterTable.objects.create(
                infl = NewInf,
                total_likes = NewInf.get_total_like(),
                total_communt = NewInf.get_total_communt(),
                alike = NewInf.get_alike(),
                acommunt = NewInf.get_acommunt(),
                following = NewInf.following,
                followers = NewInf.followers,
                communt_ratio = NewInf.get_commentRatio(),
                post_count = NewInf.postnum(),
                er = NewInf.get_er(),
            )
        alldata = otherInfluencer.objects.filter(username__contains = infl) 
    return render(e,'influencer/main.html',{
        'data':alldata,
    })

    
    
def otherdata(e):
    data = otherInfluencer.objects.all()
    return render(e,'otherdata.html' , {
        'data':data
    })