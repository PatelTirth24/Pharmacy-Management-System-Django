from django.urls import path
from Chemist_Master.views import *
urlpatterns = [
    # signin,signup,indexpage
    path('signin/',chemist_signin,name="ch_signin"),
    path('signup/',chemist_signup,name="ch_signup"),
    path('',chemist_index,name="ch_index"),
    #Chemist interactions with medicines
    path('uploade_Medi/',Uploade_Medi,name='Uploaded_Medi'),
    path('order-medicine/',order_medicine,name='order-medicine'),
    path('dashboard/', Dashboard, name='Dashboard'),

    path('editproduct/<int:id>', EditProduct, name='editproduct'),
    
    #Logout
    path('logout/',logout,name='logout'),
    


    
]