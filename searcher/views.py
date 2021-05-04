from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests  # get query result from search server
# Create your views here.

def homepage(request):
    if request.method == "POST":
        queryString = request.POST['search']
        if len(queryString) > 0:
            print(queryString)

    return render(request, 'home.html')


def results(request):
    if request.method == "post":
        result = request.POST.get('search')
        response = requests.get('http://api.github.com')
        print(result)

    return redirect('Home')
