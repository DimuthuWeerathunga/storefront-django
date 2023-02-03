from django.shortcuts import render

from store.models import Customer, Collection


# Create your views here.
def say_hello(request):
    queryset = Collection.objects.all()
    return render(request, 'hello.html', {'name': 'Dimuthu', 'customers': list(queryset)})
