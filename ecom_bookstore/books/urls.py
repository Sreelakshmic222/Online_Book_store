from django.urls import path
from .views import BookListView,BookDetailView,BookCheckoutView
urlpatterns=[
    path('book_list/',BookListView.as_view(),name='list'),
    path('details/<int:pk>/',BookDetailView.as_view(),name='detail-view'),
path('checkout/<int:pk>/',BookCheckoutView.as_view(),name='checkout-view')

]