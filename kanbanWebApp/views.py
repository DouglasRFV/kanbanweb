from django.shortcuts import redirect, render

def home(request):
    return render(request, 'kanbanWebApp/index.html')
