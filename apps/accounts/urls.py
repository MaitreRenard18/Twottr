from django.urls import include, path

from .views import account_view, login, signup

urlpatterns = [
    path('<str:username>/', account_view),
    path('login/', login),
    path('signup/', signup),
]
