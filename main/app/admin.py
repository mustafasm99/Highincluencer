from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import *
from .views import telem

# Register your models here.

class MasterTable(admin.ModelAdmin):
    list_display = ['time', 'infl' ,'post_count', 'total_likes' , 'alike' ,'acommunt', 'er','communt_ratio','following','followers']
    list_filter = ['time','infl','total_likes','alike']
    search_fields = ['infl__user__username','time']


class usersinline(admin.StackedInline):
    model = Influencer
    extra = 1 
    fieldsets = (
        (None , {
            'fields':('user','image','following','followers','post_number','block','text')
        }),
    )

class brandinline(admin.StackedInline):
    model = Brand
    extra = 1
    fieldsets = (
        (None,{
            'fields':('user','block')
        }),
    )

class users(admin.ModelAdmin):
    list_display = ['username','email','first_name','last_name']
    fieldsets = (
        (None , {
            'fields':('password','first_name','last_name','email','username')
        }),
    )
    inlines = [usersinline,brandinline]

class infl(admin.ModelAdmin):
    list_display = ['user','teleuser','dimage','followers','following','code','block','post_number','tagss' , 'engagemantRate','location']
    search_fields = ['user__username','code']
    list_editable = ['block','teleuser']

class bran(admin.ModelAdmin):
    list_display = ['user','teleuser','block']
    list_editable = ['teleuser','block']
    search_fields = ['user__username']

class cat(admin.ModelAdmin):
    list_display = ['title',]
    list_display_links = None
    list_editable = ['title',]
    search_fields =['title',]

class itm(admin.ModelAdmin):
    list_display = ['name','price','quintity','shop','sell_num','itemimage']
    search_fields =['name','shop__Name']

class xitem(admin.StackedInline):
    model = item
    extra = 1
    
    
class xshops(admin.ModelAdmin):
    list_display = ['Name','woner']
    search_fields = ['Name','woner__user__username']
    inlines = [xitem]

class check(admin.ModelAdmin):
    list_display =['xitem','name','phone_number','email','locathion','quantity','copone','total_price','time','itemximage']
    search_fields = ['xitem__name','name','phone_number','email','copone__code']


class itemoffers(admin.ModelAdmin):
    list_display = ['s_item','itemimage','influencer','infimage','accept','admin_accept','time']
    search_fields = ['s_item__name','influencer__user__username']
    actions = ['admin_Accept']
    def admin_Accept(self,request,queryset):
        queryset.update(admin_accept = True)
        telem(queryset.get().influencer.teleuser,'Your offer to work with {} has been proved you can work with it now'.format(queryset.get().s_item.name))
        telem(queryset.get().s_item.shop.woner.teleuser,'Your influencer {} will start working for now'.format(queryset.get().influencer))
       
    
class offeres(admin.ModelAdmin):
    list_display = ['woner','title','text','startTime','endTime']
    search_fields = ['woner__user__username','title']
# admin accept 
class req(admin.ModelAdmin):
    list_display = ['offer','influencers','brands','time','Accept','admin_accept']
    search_fields = ['offer__title','time','influencer__user__username']
    actions = ['admin_Accept']
    def admin_Accept(self,request,queryset):
        queryset.update(admin_accept = True)
        telem(queryset.get().influencer.first().teleuser,"your Request is Prove by woner go to work")
        print(queryset.get().influencer.first().teleuser)
    
        


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User,users)
admin.site.register(Influencer,infl)
admin.site.register(Brand,bran)
admin.site.register(shops,xshops)
admin.site.register(item,itm)
admin.site.register(offers,offeres)
admin.site.register(category,cat)
admin.site.register(requests,req)
admin.site.register(item_offer,itemoffers)
admin.site.register(checkout,check)
admin.site.register(masterTable,MasterTable)
admin.site.register(tags)
admin.site.register(saveInfluncer)
admin.site.register(influncerRequest)