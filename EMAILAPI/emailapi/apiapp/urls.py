from django.urls import path
from apiapp import views

urlpatterns = [
    path('send_mail/', views.MailView.as_view()),
    path('register/', views.RegisterView.as_view()),
]