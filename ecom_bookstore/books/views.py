import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Book, Order
from django.views.generic import ListView,DetailView
from django.db.models import Q

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'list.html'

class BookDetailView(DetailView):
    model=Book
    template_name='detail.html'

class BookCheckoutView(DetailView):
    model=Book
    template_name = 'checkout.html'

def PaymentComplete(request):
    body = json.loads(request.body)
    print('BODY:',body)
    product=Book.objects.get(id=body['productId'])
    Order.objects.create(product=product)
    return JsonResponse('payment completed',safe=False)

class SearchResultsView(ListView):
    model=Book
    template_name= 'search.html'

    def get_queryset(self):
        query =self.request.GET.get('q')
        return Book.objects.filter(Q(title=query)|Q(author=query))