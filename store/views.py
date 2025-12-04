from django.shortcuts import render, redirect
from . models import mens, womens,accessoriess,cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
def home(request):
    womens_items = womens.objects.all()
    accessoriess_items = accessoriess.objects.all()
    mens_items = mens.objects.all()
    context = {
         'mens_items': mens_items,
         'womens_items': womens_items,
         'accessoriess_items': accessoriess_items
    }

    return render(request, 'home.html', context)
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user= User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('home')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
def logout(request):
    auth_logout(request)
    return redirect('home')
def get_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart_items = cart.objects.filter(user=request.user)
    total = sum(item.item_price * item.quantity for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total
    }

    return render(request, 'cart.html', context)
def add_to_cart(request, item_id, item_type):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Determine which model to use based on item_type
    if item_type == 'mens':
        item = mens.objects.get(id=item_id)
    elif item_type == 'womens':
        item = womens.objects.get(id=item_id)
    elif item_type == 'accessories':
        item = accessoriess.objects.get(id=item_id)
    else:
        return redirect('home')
    
    # Check if item already exists in cart
    cart_item, created = cart.objects.get_or_create(
        user=request.user,
        item_id=item_id,
        item_type=item_type,
        defaults={
            'item_name': item.name,
            'item_price': item.price,
            'quantity': 1
        }
    )
    
    # If item already exists, increment quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')