from django.urls import path
from pycon import views

app_name = "pycon"
urlpatterns = [
    path("pycon/", views.PyconView.as_view(), name="welcome"),
]
