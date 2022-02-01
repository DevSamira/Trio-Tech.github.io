from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create/',
         views.CreateUser.as_view(template_name='create_user.html'), name='create-user')
]
