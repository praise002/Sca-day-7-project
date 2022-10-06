from django.urls import path
from . import views

app_name = 'cores'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
]