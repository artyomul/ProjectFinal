from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Vocab
from django.contrib.auth.models import User
from PyDictionary import PyDictionary


# Create your views here.
def index(request):
    user_id=request.session.get('_auth_user_id')
    if user_id:
        vocab = Vocab.objects.filter(user_id=user_id)
        user = User.objects.get(id=user_id)
        if request.method == 'POST':
            new_todo = Vocab(
                title=request.POST['title'],
                user_id=user
            )
            new_todo.save()
            return redirect('/')

        return render(request, 'index.html', {'vocabulary': vocab})
    return redirect('welcome/')


def welcome(request):
    return render(request,'welcome.html')


def delete(request, pk):
    vocab = Vocab.objects.get(id=pk)
    vocab.delete()
    return redirect('/')


def login(request):
    return render(request, '../templates/registration/login.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
