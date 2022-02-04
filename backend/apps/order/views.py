from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView

from .models import Order

from apps.comment.models import Comment


class OrderListView(ListView):

    model = Order


class OrderDetailView(DetailView):

    model = Order

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        # context["comments"] = CommentListView().get_queryset()
        context["comments"] = Comment.objects.filter(order=self.object.pk)

        return context


class OrderCreateView(CreateView):

    model = Order
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('order:orders-list', current_app='order')

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        return super().form_valid(form)


class OrderUpdateView(UpdateView):

    model = Order
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('order:orders-list', current_app='order')


class OrderDeleteView(DeleteView):

    model = Order
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('order:orders-list', current_app='order')
