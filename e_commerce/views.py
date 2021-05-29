from django.shortcuts import render
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
    context = {
        'title': 'Página de contato',
        'content': 'Bem-vindo a página de contato!'
    }
    return render(request, 'contact/view.html', context)