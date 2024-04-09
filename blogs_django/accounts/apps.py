from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = "blogs_django.accounts"
    name = __name__.rpartition('.')[0]
