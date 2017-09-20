from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<id>[0-9]{1,})/destroy',views.destroy,name='destroy'),
    url(r'^addCourse',views.addCourse,name='addCourse'),
    url(r'^(?P<id>[0-9]{1,})/confirm',views.confirm,name='confirm')
]
