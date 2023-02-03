from django.contrib import admin
from django.urls import path ,include
from .views import *
from .login import *
from .Brand import *
from .stor import *
from .influencer import*
from .offers import *

urlpatterns = [
   path('',main,name='main'),
   #path('item<str:code>',main,name='main'),
   path('influencer',Influencer_descovery,name='inf'),
   # path('Userinfluencer',influencer,name="infl"),
   path('influencer/<str:username>',influencerpage,name="influencerpage"),
   path('login',User_login,name='login'),
   path('logout',Logout,name='logout'),
   path('BrandDashboard',dashboard,name='branddashboard'),
   path('MYITEMS',Item_work_with,name="iww"),
   path('InfluencerAccount',InfAccount,name='infacc'),
   path('InfluencerUpdata',updateInf,name='updateInf'),
   path('analysis/<int:id>',analysis,name='an'),
   ######### Brand and stor paths ########################
   
   path('CStore',CStor,name='CStore'),
   path('STOR',store,name='stor'),
   path('delteItem/<int:id>',deleteItem,name='deleteitem'),
   path('influncerDashbord',infDashboard,name='influncerDashboard'),
   path('Brand-invoce',invoice,name='inv'),
   path('CreateSlist',create_Slist,name='csl'),
   #save list ###
   path('Save_Influncer/<int:id>',save_inList,name='saveinfol'),
   path('List_Management',list_management,name="listM"),
   # Brand request influnecre 
   path('RequestInfluncer',RequestInfluncer,name='BRI'),
   ########## offers paths ###################

   path('alloffers',offer,name="alloffers"),
   path('makeoffer',makeoffers,name="makeoffers"),
   path('deleteOffers/<int:id>',deleteoffer,name='deleteoffer'),
   path('updateoffers/<int:id>',updateoffer,name='updateoffer'),
   path('makeitemoffer',maike_item_offer,name="mioffer"),
   path('itemOffers',item_offers,name="itemoffers"),

   ############################# OFFERS ############3
   path('sendRequest',send_request,name='sendRequest'),
   path('deleteRequest/<int:id>',delete_request,name='deleteRequest'),
   path('accepterequest',Accept_request,name="accept_request"),

   ############################## Category ###########3
   path('NewCat',Create_category,name='newcat'),
   ############################### ITEM #############3
   path('item/<int:id>',s_item,name='sitem'),
   path('item/<int:id>,<str:code>',s_item,name='Sitem'),
   ################## cart #########################
   path('addToCart',addToCart,name='atc'),
   path('CART',Cart,name="cart"),
   path('byNow',byNow,name="byNow"),
   path('get_post',get_post,name="PI")
]  
