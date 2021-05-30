from django.urls import path,include
from .views import home,note_detail,note_list
urlpatterns = [
    path('message/',home,name="home"),
    path("",note_list,name="note_list"),
    path("<int:pk>/",note_detail,name="note_detail")


]