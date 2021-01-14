from django.urls import path
from  .import views

urlpatterns = [
    path('',views.home, name="age"),
    path('age',views.age, name="age"),
]
