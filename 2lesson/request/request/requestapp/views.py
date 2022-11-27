from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]
    brow = request.META["HTTP_USER_AGENT"]
    ip = request.META["REMOTE_ADDR"]

    return HttpResponse(f""" 
        <h2>Host: {host}</h2>
        <h2>Browser info: {brow}</h2>
        <h2>IP: {ip}</h2>
""")
def error(request):
    return HttpResponse("К сожалению произошла ошибка",status=400,reason = "incorrect data")
def user(request,name = "Undefined",age = 0,postp = "Undefined",postnum = 0):
    return  HttpResponse(f"""
        <h2>Имя: {name}</h2>
        <h2>Возраст: {age}</h2>
        <h2>Имя папки с постами: {postp}</h2>
        <h2>Имя папки с постами: {postnum}</h2>
""")