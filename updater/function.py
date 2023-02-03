from app.models import *
from django.utils import timezone
from app.views import api
import requests
import time
from datetime import datetime
from django.core.files.base import ContentFile
from app.views import telem

def saveOld():
       
    #update users data 
    infl = Influencer.objects.all()
    for user in infl:
        data=api(user.user.username)
        try:
            user.followers = data['followers']
            user.following = data['following']
            user.post_number = data['lastMedia']['count']
            user.text = data['bio']
            user.user.first_name = data['full_name']
            user.save()
            print("user done ")
            
            profileImage = requests.get(data['profile_pic_url_hd_proxy'])
            user.image.delete()
            user.image.save(content=ContentFile(profileImage.content),name=str(user.user),save=True)
            post_count = len(data['lastMedia']['media'])
            time.sleep(1.2)
            if post_count != 0:
                for i in range(post_count):
                    try:
                        xtime = datetime.fromtimestamp(data['lastMedia']['media'][i]['timestamp'])
                        post =  Post(
                                    influencer = user , 
                                    like = data['lastMedia']['media'][i]['like'],
                                    is_video = data['lastMedia']['media'][i]['is_video'],
                                    comment_count = data['lastMedia']['media'][i]['comment_count'],
                                    caption = data['lastMedia']['media'][i]['caption'] ,
                                    code = data['lastMedia']['media'][i]['shortcode'],
                                    time = timezone.make_aware(xtime),
                                )
                        post.save()
                        print("post is done")
                        
                        media = requests.get(data['lastMedia']['media'][i]['display_url_proxy'])
                        post.media.save(
                            content=ContentFile(media.content),
                            name=str(data['lastMedia']['media'][i]['shortcode']),
                            save=True
                            )
                    except:
                        print("No new post's")
            time.sleep(1.2)
        except:
            print("user {} not found".format(user))
            
            time.sleep(1.2)
            
def masterT():
    t = timezone.now() 
    infl = Influencer.objects.all()
    for user in infl:
        try:
            mt = masterTable.get(time = t )
            print("master table is here ")
        except:
            mt = masterTable.objects.create()
            print("master table is create")
        posts = Post.objects.filter(influencer = user).all()
        post_count = len(posts)
        mt.infl = user
        mt.followers = user.followers
        mt.following = user.following 
        mt.post = posts.first()
        mt.post_count = user.post_number
        if post_count != 0:
            for post in posts:
                mt.total_likes += post.like
                mt.total_communt += post.comment_count
                mt.alike = mt.total_likes/post_count
                mt.acommunt = mt.total_communt/post_count
        else:
            post_count=1
            mt.total_communt = 1 
            mt.total_likes = 1
            mt.alike = 1
            mt.acommunt = 1
        #End Master Tabel For Post input Data 
        mt.er = (((mt.total_likes + mt.total_communt)/post_count)/mt.followers)*100
        user.engagemantRate = (((mt.total_likes + mt.total_communt)/post_count)/mt.followers)*100
        user.save()
        mt.communt_ratio = (mt.acommunt/mt.alike )*100            
        mt.save()
     