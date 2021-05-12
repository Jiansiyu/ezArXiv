from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests  # get query result from search server
import json

# Create your views here.

import logging
logger = logging.getLogger(__name__)

def homepage(request):
    # if request.method == "POST":
    #     queryString = request.POST['search']
    #     if len(queryString) > 0:
    #         print(queryString)
    return render(request, 'home.html')


def results(request):
    if request.method == "POST":
        queryString = request.POST['search']
        result = request.POST.get('search')
        logger.info("The Query String is : {}".format(result))

        searchRespond = requests.get("http://127.0.0.1:8001/ezserver/api",params={'querystring':queryString})
        jsonstring = searchRespond.json()
        logger.debug(jsonstring)
        return render(request, 'result.html',{'searchList':jsonstring, 'queryString':queryString})

    return render(request, 'home.html')
