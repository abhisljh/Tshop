from django.shortcuts import render , redirect
from django.http import HttpResponse 
from store.forms.authforms import CustomerCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser
from django.contrib.auth import logout
from store.models import Tshirt, SizeVariant , Cart
from math import floor
# Create your views here.



def show_product(request, slug):
    tshirt = Tshirt.objects.get(slug=slug)
    size = request.GET.get('size') #holding the size on click of size 


    if size is None:
        size = tshirt.sizevariant_set.all().order_by('price').first()#retriving the size from tshirt model
    
    else:
        size = tshirt.sizevariant_set.get(size=size) #holding the size on click of size 

    size_price = floor(size.price) #holding teh size price
    
    sell_price = size_price - (size_price *(tshirt.discount/100)) #fundinto for discount
    sell_price = floor(sell_price)#price which is coming on details page
    
    context = {'tshirt': tshirt, 'price': size_price,'sell_price': sell_price,'active_size': size} #passing all the value in dictionary
    return render(request, template_name ='store/product_details.html', context = context)



def home(request):
    tshirts = Tshirt.objects.all()
    print(tshirts)
    print(len(tshirts))
    cart = request.session.get('cart')
    print(cart)

    


    context = {
        "tshirts": tshirts 
        
    }

    return render(request, template_name='store/home.html', context = context)


def cart(request):
    cart = request.session.get('cart')
    if cart is None:
        cart = []  #asigning empy list
    
    for c in cart:
        tshirt_id = c.get('tshirt')
        tshirt = Tshirt.objects.get(id=tshirt_id)
        c['size'] = SizeVariant.objects.get(tshirt=tshirt_id, size=c['size'])
        c['tshirt'] = tshirt

    print(cart)
      
    return render(request, template_name='store/cart.html' , context ={'cart': cart })


def orders(request):
    return render(request, template_name='store/orders.html')

def login(request):
    if request.method == 'GET':
         form = AuthenticationForm() #created object 
         return render(request, template_name='store/login.html', context={
        'form' :  form
    })
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user:
                loginUser(request, user)

                #{ size, tshirt, quantity}
                cart = Cart.objects.filter(user = user)
                session_cart =[]
                for c in cart:
                    obj = {
                        'size': c.sizeVariant.size,
                        'tshirt': c.sizeVariant.tshirt.id
                        ,'quantity': c.quantity

                    }
                    session_cart.append(obj)
                request.session['cart'] = session_cart
                return redirect('homepage')
        else:
            return render(request, template_name='store/login.html', context={
        'form' :  form
            })

   




#staring of signup form
def signup(request):
    if(request.method == 'GET'):
      form = CustomerCreationForm()
      context = {
          "form": form
      }
      return render(request, template_name='store/signup.html', context=context)

    else:
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save();
            user.email = user.username
            user.save()
            print(user)
            return render(request, template_name='store/login.html')
        context = {
          "form": form
        }
        return render(request, template_name='store/signup.html', context=context)

def signout(request):
    logout(request)
    return render(request, template_name='store/home.html')


def add_to_cart(request, slug, size):
   
    user  = None
    if request.user.is_authenticated:
        user = request.user
    cart = request.session.get('cart')
    if cart is None:
        cart = []
    tshirt = Tshirt.objects.get(slug = slug)
    size_temp = SizeVariant.objects.get(size = size , tshirt = tshirt) #we are storing the size and tshirt in size_temp variable
    flag = True
    for cart_obj in cart:
        t_id = cart_obj.get('tshirt')
        size_short = cart_obj.get('size')
        if t_id == tshirt.id and size == size_short:
            flag = False
            cart_obj['quantity'] = cart_obj['quantity']+1

    if flag:

         cart_obj = {
        'tshirt': tshirt.id,
        'size': size,
        'quantity': 1 
    }

    cart.append(cart_obj)

    if user is not None:
       existing  = Cart.objects.filter(user = user, sizeVariant = size_temp)
          
    if len(existing) > 0:
            obj = existing[0]
            obj.quantity = obj.quantity+1
            obj.save()

     
    else:
            c = Cart()
            c.user = user
            c.sizeVariant =  size_temp
            c.quantity = 1
            c.save()
        
    
   
         
   



    request.session['cart'] = cart
    return_url = request.GET.get('return_url')
    

    print(slug, size)
    return redirect(return_url )