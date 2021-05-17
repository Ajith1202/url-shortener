from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url
from .forms import UrlForm

def encode(request):

    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    form = UrlForm()
    short_url = ""
    if request.method == 'POST':
        long_url = request.POST['long_url']
        form = UrlForm(request.POST)
        if form.is_valid():
           obj = Url.objects.create(long_url=long_url)

           base_ten = obj.id
           short_url = ""
           base_sixtytwo = []

           while base_ten:
               base_sixtytwo.insert(0, base_ten % 62)
               base_ten = base_ten // 62

           for i in base_sixtytwo:
               short_url += string[i]
    form = UrlForm()
    print(short_url)
    if short_url:
        context = {
            'form':form,
            'short_url':short_url,
        }
    else:
        context = {
            'form':form,
        }

    return render(request, 'app/home.html', context)

def decode(request, code):

    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    idx = []

    for i in range(len(code)):
        idx.append(string.index(code[i]))

    for i in range(len(idx)):
        idx[i] *= (62 ** (len(idx) - i - 1))
    obj = Url.objects.get(id=sum(idx))

    return redirect(obj.long_url)
