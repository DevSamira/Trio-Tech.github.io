from django.views.generic import CreateView

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model


class CreateUser(CreateView):

    model = get_user_model()
    form_class = UserCreationForm
