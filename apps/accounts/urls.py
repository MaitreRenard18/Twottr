from django.urls import include, path

from .views import account_view, login, signup

urlpatterns = [
    path('<str:username>/', account_view, name="account_view"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
]
