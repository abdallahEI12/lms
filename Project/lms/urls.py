from tkinter.font import names
from django.urls import path, include
from lms import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name = "index"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name = 'register'),
]
