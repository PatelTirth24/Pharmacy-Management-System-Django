from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth import update_session_auth_hash

from .models import UserRegister,cart,UserQuery
from .forms import UserRegisterForm,UserQueryForm
from Chemist_Master.models import StoreDetails,ProductDetails,StockDetails,SK_Bills,ChemistRegister



import pytz



def createGraph(request):
    return render(request, 'admin/newgraph.html')


# User signin 
def signin(request):
    return render(request,'signin1.html')

#User logout
def logout(request):
    return redirect('user:index')

#User index
def index(request):
    return render(request,'index.html')

#User Index{This indexpage will open after doing signin}
def index1(request):
        return render(request,'index1.html')



# User register
def signup(request):
    obj=UserRegisterForm(request.POST)
    return render(request,'signup.html',{'obj':obj})
    

# User can search for medicines using this function
def search(request):
    return render(request,'search1.html')




def add_to_cart(request):
        return render(request,'cart.html')




def adminDashboard(request):
        return render(request, 'dashboard.html')
    

def viewstore(request):
    return render(request, 'admin/storedetails.html')
    


def editstore(request):
    return render(request, 'admin/editstore.html')
   






def Confirm_Orders(request):
    return render(request, 'admin/Confirm_orders.html')



def Create_Pdf(request, dt):
    if request.session.has_key('user'):
        tz = pytz.timezone('Asia/Kolkata')
        # time_now = datetime.datetime.now(timezone.utc).astimezone(tz)
        # millis = int(time.mktime(time_now.timetuple()))
        # order_id = 'SKBill_Id'+str(millis)
        order_id = 'SKBill_Id'
        print(order_id)

        # request.session['Order_id'] = order_id

        Bill_timestamp_no = order_id
        print(Bill_timestamp_no)

        sp = str(dt)
        print(sp)
        SD = ChemistRegister.objects.get(chemistfname=str(sp))
        print("======================")
        print(SD)
        Order_Data = {}

        obj_data = ProductDetails.objects.filter(status=True, store_person=SD)

        prod_price = 0
        prod_qty = 0
        qty = 0
        new = {}
        grand_tot = 0
        for i in obj_data:
            recd_data = {}
            print(i)
            qty += 1
            print(qty)

            prod_qty += int(i.productquantity)
            print(prod_qty)

            data = StockDetails.objects.get(productName=i.productname)
            print(data, i.productquantity)
            print(data.price)
            rec = float(data.price * i.productquantity)
            print(rec)
            prod_price += rec
            print(prod_price)

            print("=============")
            # recd_data['prod_nm'] = data
            recd_data["prod_price"] = prod_price
            grand_tot += prod_price
            recd_data["prod_qty"] = prod_qty
            recd_data['real_price'] = data.price
            new[str(data.productName)] = recd_data
            print(new)

            skObj = SK_Bills()
            skObj.store_person = SD
            skObj.Bill_No = str(Bill_timestamp_no)
            skObj.pd_nm = i.productname
            skObj.pd_price = data.price
            skObj.pd_qty = prod_qty
            skObj.pd_tot = prod_price
            skObj.date_data = i.date
            skObj.save()
            i.delete()
        Order_Data[SD] = new
        print(Order_Data)
        print("======================")
        data = {'data': Order_Data, 'grand_tot': grand_tot}
        pdf = render_to_pdf('admin/Create_Pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
