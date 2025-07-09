from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect

from .forms import TodoForm # importando do arquivo .py dos forms

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'appteste/post_list.html', {'posts': posts})

def get_tarefa(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TodoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TodoForm()

    return render(request, "todo.html", {"form": form})