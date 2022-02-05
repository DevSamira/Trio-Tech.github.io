from django.urls import path

from . import views

urlpatterns = [

    path('orders/status/<int:status_id>',
         views.OrderListView.as_view(), name='orders-list'),

    path('orders/create/', views.OrderCreateView.as_view(),
         name='orders-create'),

    path('orders/<uuid:pk>/update/', views.OrderUpdateView.as_view(),
         name='orders-update'),

    path('orders/<uuid:pk>/delete/', views.OrderDeleteView.as_view(),
         name='orders-delete'),

    path('orders/<uuid:pk>/', views.OrderDetailView.as_view(),
         name='orders-detail')
]
