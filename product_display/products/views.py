from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from .forms import ClientForm

def product_list(request):
    products = Product.objects.all()[0:10]
    return render(request, 'products/product_list.html', {'products': products})




def inscription_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirige vers une page de succès
    else:
        form = ClientForm()
    return render(request, 'products/inscription.html', {'form': form})



def page_success(request):
    return render(request, 'products/success.html')


def log_button_view(request):
    return render(request, 'log_button.html')


def chatbot_view(request):
    return render(request, 'chatbot.html')
