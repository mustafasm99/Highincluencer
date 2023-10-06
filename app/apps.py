from django.apps import AppConfig


# class AppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'app'

#! thise code for work out the updater model 
class AppConfig(AppConfig):
    name = 'app'
    def ready(self):
        from updater import updater
        updater.start()
