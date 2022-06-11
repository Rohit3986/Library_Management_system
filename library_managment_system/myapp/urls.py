from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.login,name="login"),
    path('menu',views.menu,name="menu"),
    path('add',views.add,name="add"),
    path('update',views.update,name="add"),
]
