from django.urls import path
from .views import AuthAppLoginView


app_name='auth_app'

urlpatterns = [
    path('login/', AuthAppLoginView.as_view(), name='login'),

]

