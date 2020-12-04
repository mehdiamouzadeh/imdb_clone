from django.urls import path
from movie.views import index,paginate,movieDetails,genres
from authy.views import Signup , PasswordChange  , EditProfile
from django.contrib.auth.views import (PasswordChangeView,LoginView ,
LogoutView ,PasswordChangeDoneView ,PasswordResetView
 , PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)

app_name = "authy"
urlpatterns = [
    path('edit/', EditProfile, name='edit-profile'),
    path('signup/',Signup,name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('password_change/',PasswordChange.as_view(),name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
]