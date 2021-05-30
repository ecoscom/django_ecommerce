from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        'title': 'Página principal',
        'content': 'Bem-vindo!'
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title': 'Página sobre',
        'content': 'Bem-vindo a página Sobre!'
    }
    return render(request, 'about/view.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Página de contato',
        'content': 'Bem-vindo a página de contato!',
        'form': contact_form,
    }
    if request.method == 'POST':
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
    return render(request, 'contact/view.html', context)