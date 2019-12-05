
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('index', views.index,name = 'index'),
    path('about', views.about,name = 'about'),
    path('blog', views.blog,name = 'blog'),
    path('contact', views.contact,name = 'contact'),
    path('home',views.home,name = 'home'),
    path('men',views.men,name = 'men'),
    path('women',views.women,name = 'women'),
    path('boys',views.boys,name = 'boys'),
    path('girls',views.girls,name = 'girls'),
    path('mens',views.mens,name = 'mens'),
    path('womens',views.womens,name = 'womens'),
    path('boy',views.boy,name = 'boy'),
    path('girl',views.girl,name = 'girl'),
    path('checkout.html',views.checkout,name ='checkout'),
    path('logout',views.logout,name ='logout'),
    path('search',views.search,name ='search'),
    path('order',views.orders,name ='order'),
    path('remove',views.remove,name ='remove')



]

