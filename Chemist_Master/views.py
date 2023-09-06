from django.shortcuts import render,redirect
from Chemist_Master.models import *
#Chemist signin page
def chemist_signin(request):
    return render(request,'chemist_signin1.html')

# Showing uploaded medicines by chemist
def Uploade_Medi(request):
    return render(request,'test.html')
    

        
 

# Chemist module home page
def chemist_index(request):
    return render(request,'chemist_index.html')

        
# chemist signup
def chemist_signup(request):
    return render(request,'chemist_signup.html')

#chemist logout
def logout(request):
    return redirect('chemist:ch_signin')
def order_medicine(request):
    return render(request, 'store/addproduct.html')
    
  



def EditProduct(request):
    return render(request, 'store/editproduct.html')
    

def Dashboard(request):
        return render(request, 'store/dashboard.html')


