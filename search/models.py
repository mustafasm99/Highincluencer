from django.db import models

# the main reson of these app is to create other data that users search about it 

class otherInfluencer(models.Model):
    username = models.CharField(max_length=120)
    fullName = models.CharField(max_length=120 , null=True ,blank=True)
    following = models.PositiveBigIntegerField(default=0)
    followers = models.PositiveBigIntegerField(default=0)
    postsCount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='OtherData/' , null=True , blank=True)
    AcceptByAdmin = models.BooleanField(default=False)
    caption = models.TextField(blank=True , null=True)
    
    def postnum(self):
        return len(otherPosts.objects.filter(infl = self).all())
    
    def get_er(self):
        er = 0
        postnumber = self.postnum()
        for i in otherPosts.objects.filter(infl = self).all():
            er += (i.like + i.commintes  )
        result = ((er/postnumber) / self.followers)
        return result        
    
    def get_total_like(self):
        total = 0
        for i in otherPosts.objects.filter(infl = self).all():
            total += i.like
        return total
    
    def get_total_communt(self):
        total = 0
        for i in otherPosts.objects.filter(infl = self).all():
            total += i.commintes
        return total
    
    def get_alike(self):
        return self.get_total_like() / self.postnum()
         
    def get_acommunt(self):
        return self.get_total_communt() / self.postnum()
    
    def get_commentRatio(self):
        return (self.get_acommunt()/self.get_alike())*100
    
    def __str__(self):
        return self.username
class otherPosts(models.Model):
    medai = models.FileField(null=True , blank=True)
    caption = models.TextField(null=True , blank=True)
    commintes = models.PositiveBigIntegerField(default=0)
    like = models.IntegerField(default=0)
    isvideo = models.BooleanField(default=False)
    shortcode = models.CharField(max_length=100 , null=True , blank=True)
    infl = models.ForeignKey(otherInfluencer , on_delete=models.SET_NULL , null=True , blank=True)
    


class otherData(models.Model):
    time = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(otherPosts,null=True,blank=True,on_delete=models.SET_NULL)
    infl = models.ForeignKey(otherInfluencer,null=True,blank=True,on_delete=models.SET_NULL)
    total_likes = models.IntegerField(null=True,blank=True,default=0)
    total_communt = models.IntegerField(null=True,blank=True,default=0)
    alike = models.FloatField(null=True,blank=True,default=0)
    acommunt = models.FloatField(null=True,blank=True,default=0)
    following = models.IntegerField(null=True,blank=True,default=0)
    followers = models.IntegerField(null=True,blank=True,default=0)
    communt_ratio = models.FloatField(null=True,blank=True,default=0)
    post_count = models.IntegerField(null=True,blank=True,default=0)
    er = models.FloatField(null=True,blank=True,default=0)