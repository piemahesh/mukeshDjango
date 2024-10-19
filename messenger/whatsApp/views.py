from django.shortcuts import render

# Create your views here.

# function
def homePage(req):
    print("im called")
    return render(req, 'index.html')

def aboutPage(req):
    print("im about page")
    return render(req, 'about.html')