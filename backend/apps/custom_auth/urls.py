from django.urls import path, include

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/login/',
         auth_views.LoginView.as_view(template_name="login_form.html"), name="login"),

    path('accounts/logout/',
         auth_views.LogoutView.as_view(), name="logout"),

    path('accounts/create/',
         views.CreateUser.as_view(template_name='create_user.html'), name='create-user')
]
