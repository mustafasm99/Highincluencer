from multiprocessing import context
from django import template
from ..models import*


register = template.Library()
@register.simple_tag(takes_context=True)
def user_type(context):
    user = context['request'].user
    inf = Influencer.objects.all()
    brand = Brand.objects.all()
    for i in brand:
        if user == i.user:
            print("brand")
            return "brand"
    for i in inf:
        if user == i.user:
            print("inf")
            return "Influencer"


def type(user):
    inf = Influencer.objects.all()
    brand = Brand.objects.all()
    for i in brand:
        if user == i.user:
            return "brand"
    for i in inf:
        if user == i.user:
            return "Influencer"

register.filter('type',type)


def Replace(string,x):
    new = str(string).replace(x,'-')
    return new
    

register.filter('replace',Replace)


def index(obj,i):
    return obj[int(i)]

register.filter('index',index)