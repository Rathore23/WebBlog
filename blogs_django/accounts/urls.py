from django.urls import path
from django.contrib.auth import views as auth_views
from blogs_django.accounts import views

urlpatterns = [
    # path("register", UserRegisterView, name="register"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path(
        'password-reset-send-mail/',
        views.CustomForgotPasswordView.as_view(),
        name='password_reset'
    ),
    path(
        'reset/<uidb64>/<token>/',
        # views.CustomPasswordResetConfirmView.as_view(),
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/custom_password_reset_confirm.html'
        ),
        name='reset_password_confirm'
    ),
    path(
        'password-reset-done/',
        views.CustomPasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_confirm.html'
        ),
        name='password_reset_complete'
    ),
]

urlpatterns += [
    # # Due to mail not send we create custom view for this
    # path(
    #     'password-reset-send-mail/',
    #     AccountPasswordResetView.as_view(),
    #     name='password_reset'
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(
    #         template_name='accounts/custom_password_reset_confirm.html'
    #     ), name='password_reset_confirm'
    # ),
    # path(
    #     'password-reset-done/',
    #     auth_views.PasswordResetDoneView.as_view(
    #         template_name='accounts/password_reset_done.html'
    #     ),
    #     name='password_reset_done'
    # ),
]
