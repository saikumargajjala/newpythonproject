from django.contrib import admin
from django.urls import path
from webApp.views import *
from webApp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',register,name='register'),
    path('',homePage,name='index'),
    path('category/<str:category>/',categoryview,name="index"),
    # path('<int:id>/',categoryview,name="index"),
    path('category/<str:category>/<int:post_slug>',post_details,name="postdetails"),
    path('post/<int:post_id>/', single_post_details, name="single_post_details"),
    path('singleimage/<str:category>/<int:post_slug>/', singleimage, name="singleimage"),

    
    path('accounts/login/',Login,name='login'),
    path('logout/',logout,name='logout'),
    # path('category/',m,name="category"),
    path('b/',m1,name="contact"),
    # # path('',m2,name='index'),
    # path('d/',m3,name="single"),
    path('about/',about,name="about"),
    path('addcate/',addcategory,name="addcat"),
  
    path('dash_board/',dashBoard,name='dash_board'),

    path('managecategory/',managecategory,name="managecategory"),
    path('updatecategory/<int:pk>',Updatecategory,name="updatecategory"),
    path('deletecategory/<int:pk>',deletecategory,name="deletecategory"),
    path('showcategory/',showcategory,name="showcategory"),
    #=============subcategory==================
    path('addsubcategory/',addsubcategory,name="addsubcategory"),
    path('managesubcategory/',managesubcategory,name="managesubcategory"),
    path('updatesubcategory/<int:pk>',Updatesubcategory,name="updatesubcategory"),
    path('deletesubcategory/<int:pk>',deletesubcategory,name="deletesubcategory"),
    path('showcategory/',showcategory,name="showcategory"),
 
 #====================Posts=========================
    path('addpost/',addpost,name="addpost"),
    path('managepost/',managepost,name="managepost"),
    path('updatepost/<int:pk>',Updatepost,name="updatepost"),
    path('deletepost/<int:pk>',deletepost,name="deletepost"),
    path('delete/success/',deletesuccess,name="deletesuccess"),
    
    path('showcategory/',showcategory,name="showcategory"),

    # ====================upload====================
    path('addupload/',addupload,name="addupload"),
    path('manageupload/',manageupload,name="manageupload"),
    path('updateupload/<int:pk>',Updateupload,name="updateupload"),
    path('deleteupload/<int:pk>',deleteupload,name="deleteupload"),
    # path('singleupload/<int:pk>',singleupload,name="singleupload"),

    # ========================video=======================

    path('addvideo/',addvideo,name="addvideo"),
    path('managevideo/',managevideo,name="managevideo"),
    path('updatevideo/<int:pk>',Updatevideo,name="updatevideo"),
    path('deletevideo/<int:pk>',deletevideo,name="deletevideo"),
    # path('singlevideo/<int:pk>',singlevideo,name="singlevideo"),

    path('addlink/',addlink,name="addlink"),
    path('managelink/',managelink,name="managelink"),
    path('updatelink/<int:pk>',Updatelink,name="updatelink"),
    path('deletelink/<int:pk>',deletelink,name="deletelink"),

   path('changepassword/',change_password,name="changepassword"),
   path('password_reset/',auth_views.PasswordResetView.as_view(template_name='main/password_reset.html',html_email_template_name='main/pass_email.html'),name='reset_password'),
   path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='main/pass_done.html'),name="password_reset_done"),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='main/pass_conf.html'),name="password_reset_confirm"),
   path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='main/pass_complete.html'),name='password_reset_complete')
    
    



    
]