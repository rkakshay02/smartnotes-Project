from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<pk>',views.detail),
    path('popularnotes',views.PopularNotesListView.as_view())
    

]