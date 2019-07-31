from django.shortcuts import render

# Create your views here.
def cart_list(request):
    return render(request,'df_cart/cart.html')