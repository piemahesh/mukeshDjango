from django.shortcuts import render,redirect
from . import db
# Create your views here.

# function
def homePage(req):
    if(req.method=="POST"):
        query = req.POST
        userName = query.get("userName")
        password = query.get("password")
        user = db.userCol.find_one({"username":userName, "password":password})
        print(user,"this is user")
        return redirect("aboutPage")
    print(req,"this is request")
    print("im called")
    
    return render(req, 'index.html')


def register(req):
    if(req.method=="POST"):
        query = req.POST
        userName = query.get("userName")
        password = query.get("password")
        confirmPassword = query.get("confirmPassword")
        if(confirmPassword == password):
            db.userCol.insert_one({"username":userName,"password":password})
            return redirect("homePage")
    return render(req,'register.html')

def aboutPage(req):
    print("im about page")
    return render(req, 'about.html')