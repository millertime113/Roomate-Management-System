from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from myModels import dbAccess
from forms import AddTransaction

def index(request):
    return render_to_response('home.html')

def home(request):
    return render_to_response('home.html')

def dashboard(request):
    return render_to_response('dashboard.html')
    
def add(request, reason=""):

    if request.method == 'POST':
        form = AddTransaction(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            id = data['user']
            
            status = "Transaction added."
            form = AddTransaction()
            return render_to_response('addTransaction.html', {'status': status, 'form': form})
    else:
        form = AddTransaction()
    return render_to_response('addTransaction.html', {'form': form})
    
''' TODO: dont forget to implement CSRF cookie session stuff for forms '''
        

   