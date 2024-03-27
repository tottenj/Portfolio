from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.aboutMe, name="about"),
    path("projects",views.projects,name="projects"),
    path("contact",views.contact,name="contact")
]
