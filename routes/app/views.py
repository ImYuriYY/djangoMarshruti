from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse

def main(request):
    userLogin = request.GET.get("login", "No login")
    userPassword = request.GET.get("pass", "No password")
    return HttpResponse('<h1>Главная страница</h1>'
                        f'Login: {userLogin}<br>Password: {userPassword}')

def top(request):
    userComment = request.GET.get("comment", "No comment")
    userLikes = request.GET.get("likes", "No likes")
    return HttpResponse('<h1>Популярные посты</h1>'
                        f'Comment: {userComment}<br>Likes: {userLikes}')

def last(request):
    userComment = request.GET.get("comment", "No comment")
    userLikes = request.GET.get("likes", "No likes")
    return HttpResponse('<h1>Последние опубликованные посты</h1>'
                        f'Comment: {userComment}<br>Likes: {userLikes}')

def all(request):
    userComment = request.GET.get("comment", "No comment")
    userLikes = request.GET.get("likes", "No likes")
    return HttpResponse('<h1>Все посты</h1>'
                        f'Comment: {userComment}<br>Likes: {userLikes}')

def about(request):
    return HttpResponse(f'<h1>О нас</h1>')

def contacts(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')

def access(request):
    userLogin = request.GET.get("login")
    userPassword = request.GET.get("pass")
    if(userLogin and userPassword == "admin"):
        return HttpResponse(f'<h1>Админ страница</h1>')
    return HttpResponseRedirect('/')

def error_404(request):
    # return HttpResponse('jnjnj')
    return HttpResponseNotFound("Загрузка страницы была завершена ошибкой")

def set(request):
    username = request.GET.get("username", "noname")
    response = HttpResponse(f'<h1>Hello {username}</h1>')

    response.set_cookie("username", username)
    return response


def get(request):
    username = request.COOKIES["username"]
    return HttpResponse(f'Hello {username}')

def json(request):
    username = request.GET.get("name", "noname")
    userage = request.GET.get("age", "no age")
    return JsonResponse({'name': username, 'age': userage})
