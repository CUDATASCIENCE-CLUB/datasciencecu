from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('userdashboard/',views.Userdashboard, name='Userdashboard'),
    path('updateBio/',views.updatebio, name='updatebio'),
    path('redirecttoevents/', views.redr, name='eventredirect'),
    path('updateImage/', views.updateimage, name='updateimage')
]