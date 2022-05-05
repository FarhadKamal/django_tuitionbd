from django.urls import path
from .views import  contact,filter, postview,postview2,postview3, postcreate, subjectview,search, ContactView,PostCreateView,PostListView, PostDetailsView,PostEditView,PostDeleteView
from .forms import ContactFormtwo
#  path('contact/', contact , name="contact"),
app_name= 'tuition'
urlpatterns = [
    path('search/', search , name="search"),
    path('filter/', filter , name="filter"),
    path('contact3/', contact , name="contact3"),
    path('contact/', ContactView.as_view() , name="contact"),
    path('contact2/', ContactView.as_view(form_class=ContactFormtwo,template_name='contact2.html') , name="contact2"),
    path('posts/', postview , name="posts"),
    path('postview/', postview2 , name="postview"),
    path('pid/<int:id>/', postview3 , name="postview3"),
    path('postlist/', PostListView.as_view() , name="postlist"),
    path('create/', postcreate , name="create"),
    path('create2/', PostCreateView.as_view() , name="create2"),
    path('edit/<int:pk>', PostEditView.as_view() , name="edit"),
    path('delete/<int:pk>', PostDeleteView.as_view() , name="delete"),
    path('postdetails/<int:pk>/', PostDetailsView.as_view() , name="postdetails"),
    path('subjects/', subjectview , name="subjects"),

    path('posts/', postview , name="posts"),
    
]