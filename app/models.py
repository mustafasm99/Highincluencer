from django.db import models
from django.contrib.auth.models import User 
from .utils import genrate_cod
from coupon.models import *
from django.utils.safestring import mark_safe

#tags model 
class tags(models.Model):
    title = models.CharField(max_length = 100,null=True,blank=True)

    def __str__(self):
        return self.title
    


#brand model
class Brand(models.Model):
    teleuser = models.CharField(max_length = 120,null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    block = models.BooleanField()
    def __str__(self):
        return self.user.username


#Shop Model
class shops(models.Model):
    Name = models.CharField(max_length=20)
    woner = models.OneToOneField(Brand,on_delete=models.CASCADE , null=True,blank = True)
    
    def __str__(self):
        return self.Name


######### CATEGORY ###########
class category(models.Model):
    title = models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        return self.title


############## ITEMS MODEL ################

class item(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    item_image = models.ImageField(upload_to='item_image/', blank=True , null=True)
    quintity = models.IntegerField(default = 0)
    sell_num = models.IntegerField(default = 0)
    shop = models.ForeignKey(shops,on_delete=models.CASCADE , blank=True , null = True)
    categorys = models.ManyToManyField(category)
    def __str__(self):
        return self.name

    def itemimage(self):
        return mark_safe('<img src="{}" width="100">'.format(self.item_image.url))

#IInfluencer - models 
class Influencer(models.Model):
    teleuser = models.CharField(max_length = 120,null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="influncer_images/" , blank=True , null=True)
    following = models.IntegerField(blank = True,null=True)
    followers = models.IntegerField(blank=True,null=True)
    post_number = models.IntegerField(null=True,blank=True)
    code = models.CharField(max_length=12,blank=True)
    time = models.DateField(auto_now = True)
    expirDate = models.DateField()
    block = models.BooleanField()
    text = models.TextField(null=True , blank=True)
    tag = models.ManyToManyField(tags)
    engagemantRate = models.FloatField(null=True,blank=True)
    location = models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.user.username

    def bay_py(self):
        pass
    @property
    def dimage(self):
        if self.image:
            return mark_safe('<img src={} width="100">'.format(self.image.url))
        else: pass
    def save(self,*args,**kwargs):
        if self.code=="":
            code = genrate_cod()
            self.code = code
        super().save(*args,**kwargs)
    
    def tagss(self):
        html="<ul>"
        for i in self.tag.all():
            html+="<li>{}</li>".format(i)
        html+="</ul>"
        return mark_safe(html)
    
############ Influncer POSTs ##############
class Post(models.Model):
    influencer = models.ForeignKey(Influencer,on_delete=models.CASCADE)
    like = models.IntegerField(null = True, blank = True)
    is_video = models.BooleanField()
    comment_count = models.IntegerField(null=True,blank=True)
    caption = models.TextField(null=True,blank=True)
    media = models.FileField(upload_to ='influncer_Posts/')
    code = models.CharField(null=True , blank=True ,unique = True , max_length = 200)
    time = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return str(self.influencer.user)


class offers(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField(null=True , blank=True)
    woner = models.ForeignKey(Brand,on_delete=models.CASCADE)
    startTime=models.DateField(auto_now = True)
    endTime = models.DateField()
    categorys = models.ManyToManyField(category)
    def __str__(self):
        return self.title

# item offer # 
class item_offer(models.Model):
    s_item = models.ForeignKey(item,on_delete=models.CASCADE,blank=True,null=True)
    influencer = models.ForeignKey(Influencer,on_delete=models.CASCADE ,blank=True,null=True)
    time = models.DateField(auto_now = True)
    accept = models.BooleanField(default=False)
    admin_accept = models.BooleanField(default=False)

    def itemimage(self):
        return mark_safe('<img src="{}" width="100" height="100" style="object-fit:cover">'.format(self.s_item.item_image.url))
    def infimage(self):
        return mark_safe('<img src="{}" width="100" height="100" style="object-fit:cover">'.format(self.influencer.image.url))

    def __str__(self):
        return str(self.s_item ) + "->" + str(self.influencer)

################ REQUEST ##########
class requests(models.Model):
    offer = models.ForeignKey(offers,on_delete=models.CASCADE,null=True,blank=True)
    time = models.DateField(auto_now = True)
    brand = models.ManyToManyField(Brand)
    influencer = models.ManyToManyField(Influencer)
    Accept = models.BooleanField(null=True,blank=True)
    admin_accept = models.BooleanField(default=False)
    def __str__(self):
        return str(self.brand.first()) + "_" + str(self.influencer.first()) 
    def influencers(self):
        st = ''
        for i in self.influencer.all():
            st+="<li>"+str(i)+"</li>"
        return mark_safe("<ol>"+st+"</ol>")
    def brands(self):
        st = ''
        for i in self.brand.all():
            st+="<li>"+str(i)+"</li>"
        return mark_safe("<ol>"+st+"</ol>")

############### Check out Class *****#####
class checkout(models.Model):
    time = models.DateTimeField(auto_now = True, null = True , blank=True)
    xitem = models.ForeignKey(item,on_delete=models.SET_NULL,null = True , blank=True)
    name = models.CharField(max_length = 25)
    phone_number = models.CharField(max_length = 15)
    email = models.CharField(max_length = 50)
    locathion = models.CharField(max_length = 120)
    quantity = models.IntegerField(default = 1)
    note = models.TextField()
    copone = models.OneToOneField(Coupon , on_delete = models.CASCADE,null=True,blank=True)
    total_price = models.FloatField()

    
    def __str__(self):
        return self.email
    
    def itemximage(self):
        return mark_safe('<img src="{}" width="100">'.format(self.xitem.item_image.url))
#***********# CART #**************#
class cart(models.Model):
    time = models.DateTimeField(auto_now = True)
    items = models.ManyToManyField(item)
    adder = models.OneToOneField(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.adder


class masterTable(models.Model):
    time = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(Post,null=True,blank=True,on_delete=models.SET_NULL)
    infl = models.ForeignKey(Influencer,null=True,blank=True,on_delete=models.SET_NULL)
    total_likes = models.IntegerField(null=True,blank=True,default=0)
    total_communt = models.IntegerField(null=True,blank=True,default=0)
    alike = models.FloatField(null=True,blank=True,default=0)
    acommunt = models.FloatField(null=True,blank=True,default=0)
    following = models.IntegerField(null=True,blank=True,default=0)
    followers = models.IntegerField(null=True,blank=True,default=0)
    communt_ratio = models.FloatField(null=True,blank=True,default=0)
    post_count = models.IntegerField(null=True,blank=True,default=0)
    er = models.FloatField(null=True,blank=True,default=0)

    def __str__(self):
        return str(self.post)

class saveInfluncer(models.Model):
    title = models.CharField(max_length=120)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    infl = models.ManyToManyField(Influencer)
    def __str__(self):
        return self.title
    
class influncerRequest(models.Model):
    maker = models.ForeignKey(Brand,on_delete=models.CASCADE)
    receiver = models.ForeignKey(Influencer,on_delete=models.CASCADE)
    influncerAccept = models.BooleanField(null=True,blank=True)
    adimnAccept = models.BooleanField(null=True,blank=True)
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.maker) + "->" + str(self.receiver) 