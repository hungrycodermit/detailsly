from django.shortcuts import redirect, render
from .forms import registrationForm
from .models import customerDetails
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# view for main page and Create and Read Operation
def index(request):
    number = 0
    if request.method == 'POST':
        fm = registrationForm(request.POST)

        if fm.is_valid():
            assignee = request.POST['Assignto']
            address = request.POST['address']
            number = request.POST['number']

            try:
                validUser = User.objects.get(username = assignee)
            except User.DoesNotExist:
                validUser = None

            if validUser is not None:
                detailData = customerDetails.objects.create(user = validUser, Assignto = assignee, address = address, number = number)
                messages.success(request, 'Successfully assigned')


            else:
                messages.error(request, 'The user you are tring to assign details doesnt exist or check username you entered again!')
            
            return redirect('/')
    else:
        fm = registrationForm()
        data = None
        if request.user.is_authenticated:
            dataset = request.user.customerdetails_set.all()
            for data in dataset:
                number += 1 
    return render(request, 'index.html', {'form': fm, 'number': number})

# view for deleting data

def delete_data(request, id=0):
    if id != 0:
        objDel = customerDetails.objects.get(pk=id)
        objDel.delete()
        return redirect('/details')

# view for updating data

def update_data(request, id=0):

    if request.user.is_authenticated:

        update_request = False
        if id != 0:
            if request.method == 'POST':
                customerDetails.objects.filter(pk=id).update(address=request.POST['address'], number = request.POST['number'])
                return redirect('/')
            # update_request = True
            # upd_obj = customerDetails.objects.get(pk=id)
            # data = customerDetails.objects.all()
            # fm = registrationForm(instance=upd_obj)
            else:
                upd_obj = customerDetails.objects.get(pk=id)
                return render(request, 'update.html', {'update': update_request, 'iddata': id, 'obj': upd_obj})

    else:
        return render(request, '404.html')


def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if len(username) > 10:
            messages.error(request,'Username must be below 10 characters')
            return redirect('/')

        if password != cpassword:
            messages.error(request,'Password doesnt match')
            return redirect('/')

        newUser = User.objects.create_user(username, email, password)
        newUser.first_name = fname
        newUser.last_name = lname
        newUser.save()
        messages.success(request,'Your account has successfully been created!')
        return redirect('/')
    
    else:
        return redirect('/')

def login_process(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'you are successfully logged in')
            return redirect('/')

        else:
            messages.error(request, 'Please enter valid credentials')
            return redirect('/')

    return redirect('/')

def logout_process(request):
    logout(request)
    return redirect('/')

def details_page(request):
    data = None
    if request.user.is_authenticated:
        data = request.user.customerdetails_set.all()
        return render(request, 'datagrid.html', {'data': data})
    else:
        return render(request, '404.html')



 