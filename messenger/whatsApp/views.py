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
    # addedd
    sessionId = req.session.get("accessKey")
    if(not sessionId):
        return redirect("login")
    return render(req, 'view.html', {"users": users})
    
def addUser(req):
    if(req.method=="POST"):
        print("im hitted")
        userId = req.session.get("accessKey")
        
        query = req.POST
        username = query.get("username")
        age = query.get("age")
        phoneNumber = query.get("phoneNumber")
        print(phoneNumber, username, age)
        db.customerCol.insert_one({"username":username,"age":age,"phoneNumber":phoneNumber,"userId":userId})
        print("user added successfully")
        return redirect("viewUser")
    return render(req,"addUser.html")

def viewUser(req):
    customers = db.customerCol.find()
    return render(req,"viewUser.html",{"customers":customers})

def logout(req):
    del req.session["accessKey"]
    print(req.session.keys())
    return redirect("login")