from django.shortcuts import render
import datetime
from django.http import HttpResponse
# from .models import UserManager


# Create your views here.

def index(request):
    classname = "Devops"
    books = ['python', 'Java', 'Django']
    user = {'name':'kk', 'age':18}
    userlist = [{'name':'kk', 'age':18}, {'name':'rock', 'age':18}, {'name':'mage', 'age':20}]
    return render(request, 'hello/hello.html', {'classname': classname, 'books':books, 'user':user, 'userlist':userlist})

def list1(request):
    users = [
        {'username':'kk1', 'name_cn': 'kk1', 'age':18},
        {'username':'kk2', 'name_cn': 'kk2', 'age':28},
        {'username':'kk3', 'name_cn': 'kk3', 'age':38},
    ]
    return render(request, 'hello/list.html', {'users':users})

def list2(request):
    messages = 'a'
    testvalue = False
    testlist = ['a', 'b', 'c', 'd']
    valuedate = datetime.datetime.now()
    value1="<a href="">点击</a>"
    users = [
        {'username':'kk1', 'name_cn': 'kk1', 'age':18},
        {'username':'kk2', 'name_cn': 'kk2', 'age':28},
        {'username':'kk3', 'name_cn': 'kk3', 'age':38},
    ]
    return render(request, 'userlist.html',
                  {'users':users,
                   'messages':messages,
                   'testvalue':testvalue,
                   'testlist':testlist,
                   'valuedate':valuedate,
                   'value1':value1,
                   }
                  )

def User(request):
    users = UserManager.objects.all()
    return render(request, 'usermanager.html', {'users':users})

def Select(request):
    select = UserManager.objects.get(id=1)
    print(select.username, select.sex, select.password)
    return render(request, 'select.html', {'select':select})

def Useradd(request):
    msg = {}
    if request.method == "POST":
        request.POST.dict()

    return HttpResponse('Add successful')