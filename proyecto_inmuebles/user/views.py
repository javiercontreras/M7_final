from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseForbidden
from .models import UserProfile
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            user = User.objects.get(username=request.user)
            tipo = request.POST.get("tipo_usuario")
            grupo = Group.objects.get(name='Arrendatario')
            # if tipo == 'A' and Group.objects.get(name='Arrendatario'):
            #     user.groups.remove('Propietario')
            #     user.groups.add('Arrendatario')
            # else:
            #     user.groups.remove('Arrendatario')
            #     user.groups.add('Propietario')

            
            print(user)
            print(tipo)
            print(grupo)
            return redirect("indice")
    else:
        # we populate the user form 
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "profile.html", {"u_form":user_form, "p_form": user_profile_form})

def log_out(request):
    logout(request)
    return redirect('indice')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect('indice')
            except:
                return HttpResponse("El usuario ya existe")
        return HttpResponse("Las contraseñas no coinciden")

def log_in(request):  
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm,'error':"El usuario o contraseña son incorrectos"})
        else:
            login(request,user)
            return redirect('indice')