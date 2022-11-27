from django.urls import path,re_path
from requestapp import views

urlpatterns = [
    path('',views.index),
    path('error',views.error),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/(?P<postp>\D+)/(?P<postnum>\d+)',views.user),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/(?P<postp>\D+)',views.user),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)',views.user),
    re_path(r'^user/(?P<name>\D+)', views.user),
    re_path(r'^user',views.user),

]
