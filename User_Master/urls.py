from django.urls import path
from  User_Master import views


urlpatterns = [

    #User Signin,Signup,Logout,IndexpagenIndexpage1
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name='logout'),
    path('',views.index,name="index"),
    path('Userindex/',views.index1,name="Userindex"),

    #User search function
    path('search/',views.search, name = "search"),
    
  
    #User Add to Cart
    path('cart/',views.add_to_cart, name="cart"),
    # -------------changes------
    path('adminDash/', views.adminDashboard, name='adminDashboard'),
    path('storeview/', views.viewstore, name='viewstore'),
    path('store_edit/', views.editstore, name='editstore'),
    path('Confirm_Orders/', views.Confirm_Orders, name="confirm_order"),  
    path('createGraph/', views.createGraph, name="createGraph"),

]