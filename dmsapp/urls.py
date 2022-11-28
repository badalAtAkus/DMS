from django.urls import path
from dmsapp import views

urlpatterns = [
    path('login/', views.login,name='login'),
    path('forgot/', views.forgot,name='forgot'),
    path('createlog/', views.createlog,name='createlog'),
    path('', views.index,name='index'),
    path('table/', views.table,name='table'),
    path('chart/', views.chart,name='chart'),

]