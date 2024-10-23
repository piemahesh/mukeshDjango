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
        if(not user):
            return redirect("register")
        else:
            id = str(user['_id'])
            req.session['accessKey'] = id
            return redirect("view")
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
            return redirect("login")
    return render(req,'register.html')
def aboutPage(req):
    print("im about page")
    return render(req, 'about.html')

def viewPage(req):
    print("trigger")
    users = db.userCol.find()
    if(not req.session):
        return redirect("login")
    return render(req, 'view.html', {"users": users})
    

def logout(req):
    del req.session["accessKey"]
    print(req.session.keys())
    return redirect("login")