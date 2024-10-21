from django.shortcuts import render

# Create your views here.

def instHome(req):
    return render(req,"instaLogin.html")