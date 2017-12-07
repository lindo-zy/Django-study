from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddFroms


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddFroms(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddFroms()

    return render(request, 'blog/index.html', {'form': form})


def article(request):
    return render(request, 'blog/article.html')


def edit(request):
    return render(request, 'blog/edit.html')
