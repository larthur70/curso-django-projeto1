from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html',context={
        'nome': 'Luiz Arthur Lima'
    })

def recipe(request,id):
    return render(request, 'recipes/pages/recipe-view.html',context={
        'nome': 'Luiz Arthur Lima'
    })