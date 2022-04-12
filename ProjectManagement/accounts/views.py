from urllib import response
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import User, HelpoUser, associationManager
from .forms import AssociationManagerUpdateform, AssociationManagerSignUpform, HelpoUserSignUpform
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect("index")

def login(request):
    login(request)
    return("index")

def pickType(response):
    return render(response,"registration/PickType.html",{})


class AssociationManagerSignUp(CreateView):
    model = User
    form_class = AssociationManagerSignUpform
    template_name = 'registration/ManagerSignup.html'

    def form_valid(self, form):  
        user = form.save()
        # login(self.request, user)
        return redirect('login')

class HelpoUserSignUp(CreateView):
    model = User
    form_class = HelpoUserSignUpform
    template_name = 'registration/HelpoUserSignup.html'

    def form_valid(self, form):  
        user = form.save()
        # login(self.request, user)
        return redirect('login')

    
@login_required
def updateAssociationManager(request, pk): # pk - primary key
    manager = associationManager.objects.get(user_id = pk)
    user_id = int(pk)
    form = AssociationManagerUpdateform(instance=manager,)
    # req_user = request.user

    if request.method == 'POST':
        form = AssociationManagerUpdateform(request.POST, instance=manager)
    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            messages.success(request, 'Your account updated successfully!')
            return redirect('index')
    # else:
        # form = AssociationManagerUpdateform(instance=req_user)
        
    context = {'form': form, 'user_id': user_id}
    return render(request, 'registration/updateAssociationManager.html', context)
