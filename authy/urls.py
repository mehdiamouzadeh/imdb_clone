from django.urls import path
from movie.views import index,paginate,movieDetails,genres
from authy.views import Signup , PasswordChange
from django.contrib.auth.views import PasswordChangeView,LoginView ,LogoutView ,PasswordChangeDoneView

app_name = "authy"
urlpatterns = [
    
    path('signup/',Signup,name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('password_change/',PasswordChange.as_view(),name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
    
]