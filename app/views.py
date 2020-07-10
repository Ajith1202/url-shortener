from django.shortcuts import render
from .models import Url
from .forms import UrlForm

def encode(request):
    form = UrlForm()
    if request.method == 'POST':
        long_url = request.POST['long_url']
        form = UrlForm(request.POST)
        if form.is_valid():
           obj = Url.objects.create(long_url=long_url)
           decoded_url = decode(obj.long_url)
    form = UrlForm()

    context = {
        'form':form,
    }

    return render(request, 'app/home.html', context)

def decode(url):
    pass
