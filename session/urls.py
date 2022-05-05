from django.urls import path
from .views import loginuser,logoutuser,register,changepass,UserProfile,ownprofile

#  path('contact/', contact , name="contact"),
app_name= 'session'
urlpatterns = [
 path('login/', loginuser , name="login"),
 path('logout/', logoutuser , name="logout"),
 path('signup/', register , name="signup"),
 path('password/', changepass , name="password"),
 path('userpro/', UserProfile , name="UserProfile"),
 path('ownerprofile/', ownprofile , name="ownprofile"),
 
]