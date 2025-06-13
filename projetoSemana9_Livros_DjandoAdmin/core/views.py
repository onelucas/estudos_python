from django.shortcuts import redirect, render
from .models import Livro

def index(request):
    livro = Livro.objects.all()
    context = {
        'livro': livro
    }
    return render(request, 'index.html', context)

def livro(request, pk):
    livro = Livro.objects.get(id=pk)
    context = {
        'livro' : livro
    }
    return render(request, 'livro.html', context)

def apagar_livro(request, pk):
    livro = Livro.objects.get(id=pk)

    if request.method == 'POST':
        livro.delete()
        return redirect('indext.html')

    context = {
        'livro': livro
    }
    return render(request, 'confirmar-apagar.html', context)