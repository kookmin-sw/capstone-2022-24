from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'providers'


class ChargeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'charges'


class SubscriptionTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscription_types'
