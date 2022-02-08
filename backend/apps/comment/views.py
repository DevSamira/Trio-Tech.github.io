from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView

from .models import Comment

from apps.order.models import Order
from project.custom_mixins import HasCommentPermissionMixin


class CommentCreateView(LoginRequiredMixin, CreateView):

    model = Comment
    fields = ['comment']

    def get_success_url(self):
        return reverse('order:orders-detail', kwargs={'pk': self.object.order.pk}, current_app='order')

    def form_valid(self, form):

        # duas maneiras de fazer a mesma coisa (a segunda é melhor)

        # order_id = self.request.path.split('/comments/create/')[1]
        order_id = self.kwargs["order_id"]

        order = Order.objects.get(id=order_id)

        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.order = order

        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, HasCommentPermissionMixin, UpdateView):

    model = Comment
    fields = ['title']
    success_url = reverse_lazy('comments-list')


class CommentDeleteView(LoginRequiredMixin, HasCommentPermissionMixin, DeleteView):

    model = Comment
    success_url = reverse_lazy('comments-list')
    template_name = 'confirm_delete.html'
