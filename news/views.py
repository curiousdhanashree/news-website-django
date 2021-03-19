from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=95df434d0c7e4d1984cc49552fb4537e')
    api = json.loads(news_api_request.content)
    return render(request,'index.html',{'api':api})

def tech(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=95df434d0c7e4d1984cc49552fb4537e')
    api = json.loads(news_api_request.content)
    return render(request,'tech.html',{'api':api})

def business(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=95df434d0c7e4d1984cc49552fb4537e')
    api = json.loads(news_api_request.content)
    return render(request,'business.html',{'api':api})

def entertainment(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=95df434d0c7e4d1984cc49552fb4537e')
    api = json.loads(news_api_request.content)
    return render(request,'entertainment.html',{'api':api})

def health(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=95df434d0c7e4d1984cc49552fb4537e')
    api = json.loads(news_api_request.content)
    return render(request,'entertainment.html',{'api':api})

def science(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=95df434d0c7e4d1984cc49552fb4537e')
    api = json.loads(news_api_request.content)
    return render(request,'science.html',{'api':api})

def about_us(request):
    return render(request,'about_us.html')