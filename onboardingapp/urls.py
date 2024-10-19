from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    path('register/', views.RegisterPage, name="RegisterPage"),
    path('register/<str:code>', views.RegisterReferredUser, name="RegisterReferredUser"),
    path('dashboard/', views.Dashboard, name="Dashboard"),
    path('viewreferrals/', views.ReferralTable, name="ReferralTable"),
    # path('studentLogin/', views.StudentLogin, name="StudentLogin"),
    # path('studentdashboard/', views.StudentDashboard, name="StudentDashboard"),
]


