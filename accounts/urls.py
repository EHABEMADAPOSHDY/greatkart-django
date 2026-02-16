from django.urls import path
from . import views

urlpatterns = [
    path('register/' , views.register , name='register'),
    path('login/' , views.login , name='login'),
    path('logout/' , views.logout , name='logout'),
    path('dahboard/' , views.dahboard , name='dahboard'),
    path('' , views.dahboard , name='dahboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validete/<uidb64>/<token>/', views.resetpassword_validete, name='resetpassword_validete'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),

]
