from django.shortcuts import redirect, render
from .forms import registrationForm
from .models import customerDetails

# Create your views here.


# view for main page and Create and Read Operation
def index(request):
    if request.method == 'POST':
        fm = registrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = registrationForm()
        data = customerDetails.objects.all()
    return render(request, 'index.html', {'form': fm, 'data': data})

# view for deleting data

def delete_data(request, id=0):
    if id != 0:
        objDel = customerDetails.objects.get(pk=id)
        objDel.delete()
        return redirect('/')

# view for updating data

def update_data(request, id=0):
    update_request = False
    if id != 0:
        if request.method == 'POST':
            upd_obj = customerDetails.objects.get(pk=id)
            fm = registrationForm(request.POST, instance=upd_obj)
            fm.save()
            return redirect('/')
        else:
            update_request = True
            upd_obj = customerDetails.objects.get(pk=id)
            data = customerDetails.objects.all()
            fm = registrationForm(instance=upd_obj)
            return render(request, 'index.html', {'formupdate' : fm, 'update': update_request, 'data': data, 'iddata': id})
        






 