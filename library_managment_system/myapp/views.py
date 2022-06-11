from django.shortcuts import redirect, render
from datetime import datetime
from django.db.models import Max
from matplotlib.style import context
from myapp.models import bookrecords
def login(request):
    context={"authorized":1,"isadmin":1,"logout":0}
    if request.method=="POST":
        logout=request.POST.get("logout")
        if logout!=None:
            context["logout"]=1
        email=request.POST.get("email")
        pass_=request.POST.get("pass")
        print("email id is ",email)
        print("pass is ",pass_)
        if email == None:
            return render(request,"login.html",context)
        if email!="rohitkashyap8925@gmail.com":
            context["isadmin"]=0
            return render(request,"menu.html",context)
        elif email=="rohitkashyap8925@gmail.com" and pass_!="1234":
            context["authorized"]=0
            context["logout"]=0
            return render(request,"login.html",context)
        else:
            return render(request,"menu.html",context)
    return render(request,"login.html",context)
# Create your views here.
def menu(request):
    book_data=bookrecords.objects.all().values("book_id","book_title","book_type","author_name","recent_transaction_date")
    print("book data is ",book_data)
    context={"book_data":book_data}
    if request.method=="POST":
        delete_val=request.POST.get("delete")
        update_val=request.POST.get("update")
        if delete_val is not None:
            bookrecords.objects.filter(book_id=delete_val).delete()
        if update_val is not None:
            context={"book_id":update_val}
            return render(request,"update.html",context)
        return redirect("/menu")
    return render(request,"menu.html",context)

def update(request):
    if request.method=="POST":
        book_id=request.POST.get("book_id")
        book_title=request.POST.get("book_title")
        book_type=request.POST.get("book_type")
        author_name=request.POST.get("author_name")
        date_val=datetime.now().strftime("%d-%m-%y %H:%M:%S")
        print(book_title,book_type,author_name,date_val)
        current_data=bookrecords.objects.get(book_id=book_id)
        print("current_data_is ",current_data)
        current_data.book_title=book_title
        current_data.book_type=book_type
        current_data.author_name=author_name
        current_data.recent_transaction_date=date_val
        current_data.save()
        return redirect("/menu")
    return render(request,"update.html")

def add(request):
    if request.method=="POST":
        print("here")
        book_title=request.POST.get("book_title")
        book_type=request.POST.get("book_type")
        author_name=request.POST.get("author_name")
        date_val=datetime.now().strftime("%d-%m-%y %H:%M:%S")
        book_data=bookrecords(book_title=book_title,book_type=book_type,author_name=author_name,recent_transaction_date=date_val)
        book_data.save()
        print(book_title,book_type,author_name,date_val)
        return redirect("/menu")
    return render(request,"add.html")