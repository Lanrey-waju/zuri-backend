from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_me, name="home-page"),
    # path("", views.go_to_zuri, name="zuri"),
]
