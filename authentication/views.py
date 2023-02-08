from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib import auth
from .forms import UserForm



class RegistrationView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html',{'form': form})

    def post(self, request):
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # if not User.objects.filter(username=username).exists():
        #     if not User.objects.filter(email=email).exists():
        #         user = User.objects.create_user(username=username, email=email)
        #         user.set_password(password)
        #         user.is_active = False
        #         user.save()
        #         messages.success(request, 'Account successfully created')
        #         return redirect(request, 'login.html')
        form = UserForm(request.POST)
        if form.is_valid():
            # if not User.objects.filter(username=form.user_name).exists():
            #     if not User.objects.filter(email=form.email).exists():
            #         user = User.objects.create_user(username=form.user_name, email=form.email)
            #         user.set_password(form.password)
            #         user.is_active = False
            #         user.save()
            #         messages.success(request, 'Account successfully created')
            #         return redirect(request, 'login.html')
            return render(request, 'register.html')
            # user = fomr.save()
            # user.is_active = False
            # user.save()
            # return redirect('/')

        return render(request, 'register.html')



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' + user.username+' you are now logged in')
                    return redirect('expenses')
                messages.error(request, 'Account is not active,please check your email')
                return render(request, 'login.html')
            messages.error(request, 'Invalid credentials,try again')
            context = {'username':username}
            return redirect('/')

        messages.error(request, 'Please fill all fields')
        return render(request, 'login.html')



class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')

