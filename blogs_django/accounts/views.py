from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from blogs_django.accounts.forms import CustomUserRegisterForm, CustomLoginForm


# class UserRegisterView(generic.CreateView):
#     """
#     If we didn't create form then user field.
#     """
#     model = User
#     fields = ["first_name", "username", "password"]
#     template_name = 'accounts/registration.html'


class UserRegisterView(generic.CreateView):
    """
    This CreateView used to sign up user using
    CustomUserRegisterForm.
    """
    # form_class = UserCreationForm
    form_class = CustomUserRegisterForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('login')


class UserLoginView(View):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        context = {
            "form": self.form_class
        }
        return render(
            request=request,
            template_name=self.template_name,
            context=context
        )

    def post(self,  request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                # messages.success(request, 'Logged in successfully')
                return redirect('home')

        messages.error(request, 'Invalid Credentials.')
        return render(
            request,
            self.template_name,
            context={
                'form': form,
            }
        )

        return render(
            request=request,
            template_name=self.template_name,
            context=context
        )


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
