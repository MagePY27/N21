# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse,QueryDict
from .models import User

from django.shortcuts import get_object_or_404
from django.http import Http404

import traceback

def useradd(request):
    """
    添加用户
    request: 获取表单提交的数据有多种方式：
    1.request.POST.get————适用于获取单个变量进行处理的场景
    2.request.POST.dict()————适用于将表单所有数据整体处理的场景
    3.Form(request.POST)————适用于表单类验证的场景（生产中最常用）
    """
    msg = {}
    if request.method == 'POST':
        try:
            print(request.POST)
            # name = request.POST.get('name', '')
            # password = request.POST.get('password', '')
            # sex = request.POST.get('sex', '')
            # print(name)
            # u = User()
            # u.name = name
            # u.password = password
            # u.sex = int(sex)
            # u.save()
            data = request.POST.dict()
            print(data)
            User.objects.create(**data)
            msg = {'code': 0, 'result':'用户添加成功'}
        except:
            msg = {'code': 1, 'errmsg':'添加用户失败：%s' %traceback.format_exc()}
    return render(request, 'hello/useradd.html', {'msg': msg})

def userlist(request):
    """
    用户列表&&姓名搜索
    :param request:
    :return:
    """
    users = User.objects.all()
    keyword = request.GET.get('keyword', '')
    print(keyword)
    if keyword:
        users = User.objects.filter(name__icontains=keyword)
    print(users)
    return render(request, 'hello/userlist.html', {'users': users}, {'keyword': keyword})


def modify(request, **kwargs):
    """
    用户更新
    1.通过ID拿到药更新数据，并传到前端进行渲染
    2.将修改后的数据提交到后端
    :param request:
    :param kwargs:
    :return:
    """
    msg = {}
    print(kwargs)
    pk = kwargs.get('pk')
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        try:
            data = request.POST.dict()
            print(data)
            User.objects.filter(pk=pk).update(**data)
            msg = {'code': 0,'result':'用户更新成功'}
        except:
            msg = {'code': 1,'errmsg':'用户更新失败：%s' %traceback.format_exc()}

    return render(request, 'hello/modify.html', {'user': user, 'msg': msg})


def userdel(request, **kwargs):
    """
    用户删除
    :param request:
    :param kwargs:
    :return:
    """
    msg = {}
    pk = kwargs.get('pk')
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        try:
            User.objects.get(pk=pk).delete()
            msg = {'code': 0, 'result': '删除用户成功'}
        except:
            msg = {'code': 1, 'errmsg': '用户删除失败 %s' %traceback.format_exc()}
    return render(request, 'hello/userdel.html', {'user': user, 'msg': msg})