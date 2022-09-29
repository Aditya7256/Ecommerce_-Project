from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from .models import Customer, Cart, Product, OrderPlaced, Mobile


def contact(request):
    return render(request, 'contact.html')


def my_account(request):
    return render(request, 'my_account.html')


def checkout(request):
    return render(request, 'checkout.html')


# def shop(request):
#     return render(request, 'shop.html')


def Add_Cart(request):
    if request.method == "POST":
        user = request.user
        product_id = request.POST.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user, product=product).save()
        return redirect('show_cart')
    return redirect('show_cart')


def Show_Cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = Cart.objects.filter(user=user)
        # cart_products = [cart.product for cart in carts]
        # print(cart_products)
        return render(request, 'cart.html', {'carts': carts})
    return redirect("show_cart")


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# def delete_iteam(request, id):
#     if request.method == "POST":
#         product_id = request.POST.get('prod_id')
#         product_id.delete()
#         return redirect('/')
        
# def remove(self, product):
#     """
#     Remove a product from the cart.
#     """
#     product_id = str(product.id)
#     if product_id in self.cart:
#         # Subtract 1 from the quantity
#         self.cart[product_id]['quantity'] -= 1
#         # If the quantity is now 0, then delete the item
#         if self.cart[product_id]['quantity'] == 0:
#             del self.cart[product_id]
#         self.save()

# For Signup:
def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrates!! Your Account has been sign_up Successfully!!!! ')
        else:
            pass
            # get_messages(request)[errors]
            # return HttpResponse('invailid signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# For Login:
def Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                # print('This is working', uname)
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    # messages.success(request, 'Logged in Successfully!!!!!!!!!!!')
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('invailid login..!!!!!!!!!')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/')
    messages.success("Please Login First.")
    


class Productview(View):
    def get(self, request):
        samsung = Product.objects.filter(category='Sm')
        sony = Product.objects.filter(category='S')
        lg = Product.objects.filter(category='L')
        return render(request, 'index.html', {'name': request.user, 'samsung': samsung, 'sony': sony, 'lg': lg})


class Product_details_Views(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        mobile = Mobile.objects.get(pk=pk)
        return render(request, 'product_details.html', {'product': product, 'mobile': mobile})
