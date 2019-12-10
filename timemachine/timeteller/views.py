from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time

from bs4 import BeautifulSoup
import requests



def home(request):
    res=requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup=BeautifulSoup(res.text,'html.parser')

    a=soup.select('ol a')
    names=[tag.string for tag in soup.select('ol a')]

    f=[]
    for items in a:
        f.append(items.getText())

    fune={
        'name':names
    }
    return render(request, 'index.html',fune)
    # d={
    #     'name':'milan'
    #     }

    # names=['milan','milan2','milan3']
    
    

    # z={
    #     'names':names
    # }
    # return HttpResponse('Greetings. Welcome to the time machine.')
    # return render(request, 'index.html',f)


def today(request):
    date = datetime.date.today()
    return HttpResponse("Today's date is: {}".format(date))


def timestamp(request):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))
