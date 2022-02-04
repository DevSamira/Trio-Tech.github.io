from django.urls import path

from . import views

urlpatterns = [

    path('comments/create/<uuid:order_id>', views.CommentCreateView.as_view(),
         name='comments-create'),

    path('comments/<uuid:pk>/update/', views.CommentUpdateView.as_view(),
         name='comments-update'),

    path('comments/<uuid:pk>/delete/', views.CommentDeleteView.as_view(),
         name='comments-delete')
]
