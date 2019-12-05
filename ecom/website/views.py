from django.shortcuts import render,redirect
from .models import customer,men_dress,women_dress,boys_dress,girls_dress,check_out,order
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from itertools import chain
from django.http import HttpResponseRedirect

# Create your views here.
@csrf_exempt
def index(request):
    user1 = customer()
    if request.method == 'POST':
       
        user1.name = request.POST['Name']
        user1.email = request.POST['Email']
        user1.password = request.POST['Password']
        password2 = request.POST['Confirm Password']
       
            

        if user1.password == password2 :
            
            if User.objects.filter(username = user1.name).exists():
                #messages.info(request,'Username Taken')
                return redirect(' ')
            
            elif User.objects.filter(email=user1.email).exists():
                #messages.info(request,'Email Taken')
                return redirect(' ')

            else:   
                user2 = User.objects.create_user(username=user1.name, password=user1.password, email=user1.email)
                user2.save();
                user1.save()
                print('user created')
                return render(request,'home.html',{'name':user1.name})


       
        




        
        else:
            #messages.info(request,'password not matching..')    
            print('not working')
            return redirect('index')


            


    else:
        return render(request,'index.html')



@csrf_exempt
def about(request):
    return render(request,'about.html')
@csrf_exempt
def search(request):
    return render(request,'search.html')
@csrf_exempt
def blog(request):
    return render(request,'blog.html')

@csrf_exempt
def contact(request):
        return render(request,'contact.html')




@csrf_exempt
def home(request):
    if request.method =='POST':
        username = request.POST['Name2']
        password = request.POST['Password2']

        user3 = auth.authenticate(username=username,password=password)

        if user3 is not None:
            auth.login(request, user3)
            return render(request,'home.html',{'name':username})
        else:
            messages.info(request,'invalid credentials')
            return HttpResponseRedirect(request.path_info)
                
    else:   
     return render(request,'home.html')


@csrf_exempt
def men(request):
    
    dress = men_dress.objects.all()
    
    if request.method == 'POST':
        check0 = check_out()       
        check0.name = request.POST['zayanto']
        #check0.email = request.POST['Email']
        check0.title = request.POST['Title']
        #check0.description = request.POST['Description']
        check0.price = request.POST['Price']
        check0.image1 = request.POST['Image']
        check0.save()
        return  render(request,'men.html',{'dress':dress})

    
    else:
        dress = men_dress.objects.all()
        return render(request,'men.html',{'dress':dress})



@csrf_exempt
def mens(request):
    if request.method == 'POST' :
        productname = request.POST['titlez']
        print(str(productname))
        try:
            search = men_dress.objects.get(title=str(productname))
            print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz:',str(search))
        except:
            search = women_dress.objects.get(title=str(productname))

       
        
        description = str(search.description)
        print(description)
        price = str(search.price)
        print(price)
        
        img = search.image1
        return render(request,'mens.html',{'title':productname,'description':description,'price':price,'img':img})
    
    else:
        return render(request,'mens.html')



@csrf_exempt
def women(request):
    dress0 = women_dress.objects.all()
    if request.method == 'POST':
        check0 = check_out()       
        check0.name = request.POST['zayanto']
        #check0.email = request.POST['Email']
        check0.title = request.POST['Title']
        #check0.description = request.POST['Description']
        check0.price = request.POST['Price']
        check0.image1 = request.POST['Image']
        check0.save()
        return  render(request,'women.html',{'dress':dress0})

    
    else:
        dress = men_dress.objects.all()
        return render(request,'women.html',{'dress':dress0})



@csrf_exempt
def womens(request):
    if request.method == 'POST' :
        productname = request.POST['titlez']
        print(str(productname))
        search = women_dress.objects.get(title=str(productname))
        description = str(search.description)
        print(description)
        price = str(search.price)
        print(price)
        
        img = search.image1
        return render(request,'womens.html',{'title':productname,'description':description,'price':price,'img':img})
    
    else:
        return render(request,'womens.html')

@csrf_exempt
def boys(request):
    dress1 = boys_dress.objects.all()
    if request.method == 'POST':
        check0 = check_out()       
        check0.name = request.POST['zayanto']
        #check0.email = request.POST['Email']
        check0.title = request.POST['Title']
        #check0.description = request.POST['Description']
        check0.price = request.POST['Price']
        check0.image1 = request.POST['Image']
        check0.save()
        return  render(request,'boys.html',{'dress':dress1})

    
    else:
        dress = men_dress.objects.all()
        return render(request,'boys.html',{'dress':dress1})
@csrf_exempt
def boy(request):
    if request.method == 'POST' :
        productname = request.POST['titlez']
        print('result = ',str(productname))
        search = boys_dress.objects.get(title=str(productname))
        description = str(search.description)
        print(description)
        price = str(search.price)
        print(price)
        
        img = search.image1
        return render(request,'boy.html',{'title':productname,'description':description,'price':price,'img':img})
    
    else:
        return render(request,'boy.html')


@csrf_exempt
def girls(request):
    dress2 = girls_dress.objects.all()
    if request.method == 'POST':
        check0 = check_out()       
        check0.name = request.POST['zayanto']
        #check0.email = request.POST['Email']
        check0.title = request.POST['Title']
        #check0.description = request.POST['Description']
        check0.price = request.POST['Price']
        check0.image1 = request.POST['Image']
        check0.save()
        return  render(request,'girls.html',{'dress':dress2})

    
    else:
        dress = men_dress.objects.all()
        return render(request,'girls.html',{'dress':dress2})


@csrf_exempt
def girl(request):
    if request.method == 'POST' :
        productname = request.POST['titlez']
        print('result = ',str(productname))
        search = girls_dress.objects.get(title=str(productname))
        description = str(search.description)
        print(description)
        price = str(search.price)
        print(price)
        
        img = search.image1
        return render(request,'girl.html',{'title':productname,'description':description,'price':price,'img':img})
    
    else:
        return render(request,'girl.html')





@csrf_exempt
def checkout(request):
    if request.user.is_authenticated:
        
        user = request.user
        name = check_out.objects.all().filter(Q(name__icontains = user))
        return render(request,'checkout.html',{'name':name})
    else:
        return render(request,'checkout.html')

@csrf_exempt
def remove(request):
    if request.user.is_authenticated:
      if request.method == 'POST':
        title = request.POST['data']
        user = request.user
        name = check_out.objects.all().filter(Q(name__icontains = user))
        product = check_out.objects.all().filter(Q(title__icontains = title , name__icontains = user))
        product.delete()
        return render(request,'checkout.html',{'name':name})
    else:
        return render(request,'checkout.html')


@csrf_exempt
def search(request):
    if request.method =='POST' :
        keyword = request.POST['search']
        dress1 = men_dress.objects.all().filter(Q(title__icontains = keyword)) 
        dress2 = women_dress.objects.all().filter(Q(title__icontains = keyword)) 
        dress3 = boys_dress.objects.all().filter(Q(title__icontains = keyword)) 
        dress4 = girls_dress.objects.all().filter(Q(title__icontains = keyword))

        dress = list(chain(dress1, dress2, dress3,dress4))
        return render(request,'search.html',{'dress':dress})

    else:
        return render (request,'search.html')

@csrf_exempt
def orders(request):
    order0 = order()
    
    if request.method == 'POST':
        
        order0.username = request.user.username
        order0.full_name = request.POST['name']
        order0.mobile = request.POST['mobile']
        order0.landmark = request.POST['landmark']
        order0.address = request.POST['address']
        check_out.objects.filter(name=request.user.username).update(address=request.POST['address'])
        check_out.objects.filter(name=request.user.username).update(full_name=request.POST['name'])
        check_out.objects.filter(name=request.user.username).update(mobile=request.POST['mobile'])
        check_out.objects.filter(name=request.user.username).update(address_type=request.POST['address_type'])
        check_out.objects.filter(name=request.user.username).update(landmark=request.POST['landmark'])
        #check_out.objects.filter(name=request.user.username).update(address=request.POST['address'])
        #,full_name = request.POST['full_name'],mobile = request.POST['mobile'])
        order0.address_type = request.POST['address_type']
        order0.save()
        return render (request,'order.html')
    else:
        return render (request,'search.html')





def logout(request):
    auth.logout(request)
    return redirect('/')     
    
