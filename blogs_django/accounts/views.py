from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordContextMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode
from django.views import generic, View
from django.utils.encoding import force_bytes
from django.views.generic import FormView, TemplateView
# pip install django-templated-email
from templated_email import send_templated_mail

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
    # form_class = UserCreationForm
    """
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                email = 'gedate7904@picdv.com'

                # pip install django-templated-email
                email = 'user2@yopmail.com'

                # try:
                #     send_templated_mail(
                #         template_name="send_templated_mail.html",
                #         from_email=settings.EMAIL_HOST_USER,
                #         recipient_list=[email],
                #         bcc=None,
                #         context={
                #             'email': email,
                #             'username': 'Email',
                #             'base_url': 'http://127.0.0.1:8000/',
                #             'protocol': 'https' if getattr(settings, 'FRONTEND_USE_HTTPS', False) else 'http',
                #         }
                #     )
                # except Exception as e:
                #     print('Error while sending mail :', e)

                return redirect('home')

        messages.error(request, 'Invalid Credentials.')
        return render(
            request,
            self.template_name,
            context={
                'form': form,
            }
        )


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class CustomForgotPasswordView(FormView):
    template_name = 'accounts/password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            token = default_token_generator.make_token(user)
            print('urlsafe_base64_encode(force_bytes(user.pk)), :', urlsafe_base64_encode(force_bytes(user.pk)),)
            reset_link = self.request.build_absolute_uri(
                reverse_lazy(
                    'reset_password_confirm',
                    kwargs={
                        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': token
                    }
                )
            )

            print('reset_link :-', reset_link)

            try:
                send_mail(
                    'Password Reset',
                    f'Please click the following link to reset your password: {reset_link}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                print('Error in CustomForgotPasswordView :', e)
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/password_reset_confirm.html'


class CustomPasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = "accounts/password_reset_done.html"
    title = "Password reset sent"


# class AccountPasswordResetView(PasswordResetView):
#     template_name = 'accounts/password_reset.html'
#
#     def post(self, request, *args, **kwargs):
#         email = self.request.POST.get('email')
#         user = User.objects.filter(email=email, is_active=True,).first()
#
#         if user:
#             return super().post(request, *args, **kwargs)
#         else:
#             error_message = "Invalid email address"
#             return render(
#                 request,
#                 self.template_name,
#                 {'error_message': error_message, 'email': email}
#             )
