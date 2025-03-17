from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from .models import usereg,product,doctoreg,doctor,Appoinment,Feedback,injury,drivereg,pharmacy,Cart,Transaction
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings



# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method=='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        image=request.FILES.get('image')
        usereg(firstName=firstName,lastName=lastName,contact=contact,address=address,username=username,email=email,password=password,confirmPassword=confirmPassword,image=image).save()
        return redirect('login')
    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=usereg.objects.filter(username=username,email=email,password=password).first()
        if user:
            request.session['email']=email
            if user.status=='approved':
                request.session['email']=user.email
                return redirect('home')
            else:
               return render(request,'login.html',
           {'error':'your account is not yet approved.please wait until the admin approves your registration'})
        else:
              return render(request,'login.html',{'error':'invalid email or password'})
        
    else:
            error_msg="Invalid Username or Password!"
            return render(request, 'login.html',{'error_msg':error_msg})
    
    
def profile(request):
    email=request.session.get('email')
    if email:
        user=usereg.objects.get(email=email)
        return render(request,'profile.html',{'user':user})
    return render(request,'login.html')

def pharmacypro(request):
    email=request.session.get('email')
    if email:
        user=pharmacy.objects.get(email=email)
        return render(request,'pharmacypro.html',{'user':user})
    return render(request,'login.html')
 
 
def edit_profile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')  # Redirect to login page if user is not logged in

    user = get_object_or_404(usereg, email=email)

    if request.method == "POST":
        user.firstName = request.POST.get("firstName")
        user.lastName = request.POST.get("lastName")
        user.contact = request.POST.get("contact")
        user.address = request.POST.get("address")
        user.username = request.POST.get("username")

        # Handle profile image upload
        if user.image:
            user.image = request.FILES.get('image')

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Redirect to the profile page after updating

    return render(request, 'edit_profile.html', {'user': user})

def addproduct(request):
    if request.method=="POST":
        productname=request.POST.get('productname')
        manufacturer=request.POST.get('manufacturer')
        category=request.POST.get('category')
        description=request.POST.get('description')
        price=request.POST.get('price')
        stock=request.POST.get('stock')
        image=request.FILES.get('image')
        sellername=request.POST.get('sellername')
        sellercontact=request.POST.get('sellercontact')
        sellermail=request.POST.get('sellermail')
        product(productname=productname,manufacturer=manufacturer,category=category,description=description,price=price,stock=stock,image=image,sellername=sellername,sellercontact=sellercontact,sellermail=sellermail).save()
        return redirect('adproductlist')
    return render(request,'product.html')

def profilelist(request):
    prof=usereg.objects.all()
    return render(request,'profilelist.html',{'prof':prof})

def productlist(request):
    prod=product.objects.all()
    return render(request,'productlist.html',{'prod':prod})

def logout(request):
    request.session.flush()
    return render(request,'index.html')

def delete(request,id):
    a=product.objects.get(id=id)
    a.delete()
    return redirect('productlist')

def doctor(request):
    if request.method=='POST':
        doctorname=request.POST.get('doctorname')
        specialist=request.POST.get('specialist')
        doctor(doctorname=doctorname,specialist=specialist)
        return redirect('home')
    return render(request,'doctor.html')

def doctorhome(request):
    email=request.session.get('email')
    doc=doctoreg.objects.get(email=email)
    return render(request,'doctorhome.html',{'doc':doc})
def doctoregister(request):
    if request.method=='POST':
        doctorname=request.POST.get('doctorname')
        specialization=request.POST.get('specialization')
        contact=request.POST.get('contact')
        licenseNumber=request.POST.get('licenseNumber')
        hospital=request.POST.get('hospital')
        image=request.FILES.get('image')
        print(image)
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        doctoreg(doctorname=doctorname,specialization=specialization,contact=contact,licenseNumber=licenseNumber,hospital=hospital,image=image,username=username,email=email,password=password,confirmPassword=confirmPassword).save()
        return redirect('doctorlogin')
    return render(request,'doctoregister.html')

# def doctorlogin(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         user=usereg.objects.filter(username=username,email=email,password=password).first()
#         if user:
#             request.session['email']=email
#             if user.status=='approved':
#                 request.session['email']=user.email
#                 return redirect('home')
#             else:
#                return render(request,'login.html',
#            {'error':'your account is not yet approved.please wait until the admin approves your registration'})
#         else:
#               return render(request,'doctorlogin.html',{'error':'invalid email or password'})
#     else:
#         error_msg="Invalid Username or Password!"
#         return render(request, 'doctorlogin.html',{'error_msg':error_msg})
#     return render(request, 'doctorlogin.html')

def doctorlogin(request):
    if request.method=='POST':
        doctorname=request.POST.get('doctorname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=doctoreg.objects.filter(doctorname=doctorname,email=email,password=password).first()
        if user:
            request.session['email']=user.email
            return redirect('doctorhome')
        else:
            alert="<script> alert('Invalid credentials'); window.location.href='/doctorlogin/'; </script>"
            return HttpResponse(alert) 
    else:
        return render(request,'doctorlogin.html')
    
def docprofile(request):
    email=request.session.get('email')
    if email:
        doc=doctoreg.objects.get(email=email)
        return render(request,'docprofile.html',{'doc':doc})
    return render(request,'doctorlogin.html')
    
def doctoreglist(request):
    doc = doctoreg.objects.all()
    return render(request, 'doctoreglist.html', {'doc': doc})

def adminindex(request):
    return render(request,'adminindex.html')

def productsearch(request):
    if request.method == "POST":
        m = request.POST.get('productname')
        if m:
            prod = product.objects.filter(productname__icontains=m)  # Use icontains for partial matches
            if not prod.exists():
                return render(request, 'productsearch.html', {'message': 'No product found', 'prod': []})
            return render(request, 'productsearch.html', {'prod': prod})
        else:
            return render(request, 'productsearch.html', {'message': 'Please enter a valid product name to search.'})
    else:
        return render(request, 'productsearch.html')

def driverhome(request):
    email = request.session.get('email')  # Get the logged-in driver's email
    if not email:
        return redirect('driverlogin')  # Redirect if not logged in

    try:
        driver = drivereg.objects.get(email=email)  # Fetch the driver by email
    except drivereg.DoesNotExist:
        return redirect('driverlogin')  # Redirect if driver not found

    return render(request, 'driverhome.html', {"driver": driver})
    
def driveregister(request):
    if request.method=='POST':
        drivername=request.POST.get('drivername')
        vehicle=request.POST.get('vehicle')
        contact=request.POST.get('contact')
        licenseNumber=request.POST.get('licenseNumber')
        image=request.FILES.get('image')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        location=request.POST.get('location')
        obj=drivereg(drivername=drivername,vehicle=vehicle,contact=contact,licenseNumber=licenseNumber,image=image,username=username,email=email,password=password,confirmPassword=confirmPassword,location=location)
        obj.save()
        return redirect('driverlogin')
    return render(request,'driveregister.html')

def driverlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=drivereg.objects.filter(username=username,email=email,password=password).first()
        if user:
            request.session['email']=email
            return redirect('driverhome')
        else:
            error_msg="Invalid Username or Password!"
            return render(request, 'driverlogin.html',{'error_msg':error_msg})
    return render(request, 'driverlogin.html')

def driversearch(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        driv = drivereg.objects.filter(location__iexact=location)  # Case-insensitive filtering
    else:
        driv = drivereg.objects.filter(availability_status=True)  
    
    return render(request, 'driversearch.html', {'driv': driv})

def adproductlist(request):
    prod=product.objects.all()
    return render(request,'adproductlist.html',{'prod':prod})


from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import usereg, product, Cart

def quantity_form(request, product_id):
    prod = get_object_or_404(product, id=product_id)
    return render(request, 'quantity_form.html', {'product': prod})

def add_cart(request, product_id):
    if 'email' not in request.session:
        return HttpResponse("<script>alert('Login Failed.'); window.location.href='/user_login/';</script>")

    semail = request.session['email']
    user = get_object_or_404(usereg, email=semail)
    prod = get_object_or_404(product, id=product_id)

    if request.method == 'POST':
        quantity_str = request.POST.get('quantity', '1')  # Default to 1
        if not quantity_str.isdigit():
            return HttpResponse("Invalid quantity value.")  # Handle invalid input

        quantity = int(quantity_str)

        if quantity > prod.stock:
            return HttpResponse("<script>alert('Invalid quantity.'); window.location.href='/productlist/';</script>")

        price = Decimal(prod.price)  # Ensure price is a Decimal
        total_price = price * quantity

        # Check if cart item exists, and update or create
        cart_item, created = Cart.objects.get_or_create(
            user=user, products=prod,
            defaults={'quantity': quantity, 'total': total_price}
        )

        if not created:  # If item already in cart, update it
            cart_item.quantity += quantity  # Increase quantity instead of replacing
            cart_item.total = cart_item.quantity * price
            cart_item.save()

        return redirect('my_cart')  # Redirect to cart page after adding item

    return HttpResponse("Invalid Request")

def my_cart(request):
    if 'email' in request.session:
        semail = request.session['email']
        user = usereg.objects.get(email=semail)  # Get the user from session email
        cart = Cart.objects.filter(user=user)  # Get the cart items for the logged-in user
        
        # Calculate the total price of the cart
        total_cart_price = sum(item.total for item in cart)
        
        return render(request, 'my_cart.html', {'cart': cart, 'total_cart_price': total_cart_price})
    else:
        alert = "<script> alert('Login Required.'); window.location.href='/home/'; </script>"
        return HttpResponse(alert)

def delete_cart(request,cart_id):
     if 'email' in request.session:
        cart=Cart.objects.get(id=cart_id)
        cart.delete()
        return redirect('my_cart')


#PAYMENT

import json
import razorpay
import logging
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction as db_transaction
from .models import Cart, Transaction, usereg, product

# Setup logging
logger = logging.getLogger(__name__)

# Razorpay API Keys
RAZOR_KEY_ID = 'rzp_test_X5OfG2jiWrAzSj'
RAZOR_KEY_SECRET = 'SsCovWWZSwB1TGd1rSoIiwF3'

def initiate_payment(request):
    """ Initiates payment by creating a Razorpay order """
    if 'email' not in request.session:
        return redirect('login')

    try:
        user = usereg.objects.get(email=request.session['email'])
        cart_items = Cart.objects.filter(user=user).select_related('products')

        if not cart_items.exists():
            logger.warning(f"Cart is empty for user {user.email}. Redirecting.")
            return redirect('home')  # Redirect if cart is empty

        total_amount = sum(item.products.price * item.quantity for item in cart_items)

        client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
        order_data = {
            "amount": int(total_amount * 100),  # Convert to paise
            "currency": "INR",
            "payment_capture": 1  # Auto capture payment
        }
        order = client.order.create(order_data)

        # Store cart details as JSON string
        cart_data_json = json.dumps([
            {
                "productname": item.products.productname,
                "manufacturer": item.products.manufacturer,
                "category": item.products.category,
                "quantity": item.quantity,
                "price": float(item.products.price)
            }
            for item in cart_items
        ])

        # Create a transaction entry
        with db_transaction.atomic():  # Ensure DB commit
            transaction = Transaction.objects.create(
                user=user,
                cart_details=cart_data_json,  # ✅ Save JSON string
                razorpay_order_id=order['id'],
                amount=total_amount,
                status="Pending"
            )
            logger.info(f"Transaction Created: {transaction}")

        context = {
            "razorpay_key": RAZOR_KEY_ID,
            "order_id": order['id'],
            "amount": int(total_amount * 100),  # Convert to integer
            "display_amount": total_amount,
            "currency": "INR",
            "cart_items": cart_items,
            "user": user,
        }
        return render(request, "checkout.html", context)

    except usereg.DoesNotExist:
        logger.error(f"User with email {request.session['email']} not found.")
        return redirect('login')

    except Exception as e:
        logger.error(f"Error in initiate_payment: {str(e)}")
        return redirect('my_cart')


def verify_payment(order_id, payment_id, signature):
    """ Verifies payment signature with Razorpay """
    client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
    params = {
        'razorpay_order_id': order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }
    try:
        return client.utility.verify_payment_signature(params)
    except Exception:
        return False


@csrf_exempt 
def payment_success(request):
    """ Handles successful payment callback from Razorpay """
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request."}, status=400)

    data = request.POST
    logger.info(f"Received Payment Data: {data}")

    razorpay_order_id = data.get('razorpay_order_id')
    razorpay_payment_id = data.get('razorpay_payment_id')
    razorpay_signature = data.get('razorpay_signature')

    if not all([razorpay_order_id, razorpay_payment_id, razorpay_signature]):
        logger.error("Missing required payment fields!")
        return JsonResponse({"error": "Missing required payment fields."}, status=400)

    if not verify_payment(razorpay_order_id, razorpay_payment_id, razorpay_signature):
        logger.error("Invalid payment signature!")
        return JsonResponse({"error": "Payment verification failed."}, status=400)

    try:
        transaction = Transaction.objects.get(razorpay_order_id=razorpay_order_id)
        user = transaction.user
        transaction.razorpay_payment_id = razorpay_payment_id
        transaction.razorpay_signature = razorpay_signature
        transaction.status = "Paid"

        with db_transaction.atomic():  # Ensure DB commit
            transaction.save()
            logger.info(f"✅ Transaction Updated: {transaction}")

            # Convert JSONField to Python list
            cart_details = json.loads(transaction.cart_details)  # ✅ Deserialize JSON

            # Reduce stock in product table
            for item in cart_details:
                product_name = item["productname"]  # Correct key
                quantity = item["quantity"]

                # Get the product and reduce stock
                prodt = product.objects.get(productname=product_name)
                if prodt.stock >= quantity:
                    prodt.stock -= quantity
                    prodt.save()
                else:
                    logger.warning(f"Insufficient stock for {product_name}. Skipping update.")

            # Clear user's cart after successful payment
            Cart.objects.filter(user=user).delete()
            logger.info(f"🛒 Cart cleared for user {user.email}")

        return JsonResponse({"message": "Payment successful! Stock updated and cart cleared."})

    except Transaction.DoesNotExist:
        logger.error(f"Transaction with order ID {razorpay_order_id} not found!")
        return JsonResponse({"error": "Transaction not found."}, status=400)

    except Exception as e:
        logger.error(f"Error processing payment: {str(e)}")
        return JsonResponse({"error": "An error occurred while processing payment."}, status=500)


    
def payhistory(request):
    transactions=Transaction.objects.all()
    return render(request,'payhistory.html',{'transactions':transactions})

def deltrans(request,id):
    tsn=Transaction.objects.get(id=id)
    tsn.delete()
    return redirect('payhistory')


import json

def trackorder(request):
    email = request.session.get('email')
    
    if email:
        try:
            user = usereg.objects.get(email=email)
            transactions = Transaction.objects.filter(user=user).order_by('-created_at')

            for transaction in transactions:
                # Ensure cart_details is in the correct format
                if isinstance(transaction.cart_details, str):  
                    try:
                        transaction.cart_details = json.loads(transaction.cart_details)  # Convert JSON string to Python list
                    except json.JSONDecodeError:
                        transaction.cart_details = []  # Handle JSON errors safely
                elif not isinstance(transaction.cart_details, list):
                    transaction.cart_details = []  # Default to an empty list if invalid data

            return render(request, 'trackorder.html', {'transactions': transactions})

        except usereg.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')

   
def userlist(request):
    user=usereg.objects.all()
    return render(request,'userlist.html',{'user':user})

def update_status(request):
    if request.method =="POST":
        email=request.POST.get('email')
        status=request.POST.get('status')
        if not email or not status:
            return redirect('userlist')
        if status not in['applied','approved','rejected']:
            return redirect('userlist')
        
        constr=get_object_or_404(usereg,email=email)
        constr.status=status
        constr.save()
        return redirect(userlist)
        

def doctorsearch(request):
    if request.method == 'POST':
        specialization = request.POST.get('specialization')
        doc = doctoreg.objects.filter(specialization__iexact=specialization)  # Case-insensitive filtering
    else:
        doc = doctoreg.objects.all()  # Optionally, show all doctors if no search is done
    
    return render(request, 'doctorsearch.html', {'doc': doc})


def appointment(request, id): 
    email = request.session.get('email')

    if not email:
        return redirect('login')  

   
    try:
        user = usereg.objects.get(email=email)
    except usereg.DoesNotExist:
        return redirect('login') 

  
    doc = get_object_or_404(doctoreg, id=id)

    if request.method == "POST":
        patientname = request.POST.get('patientname')
        date = request.POST.get('date')
        time = request.POST.get('time')
        diseasedetails = request.POST.get('diseasedetails')

        aobj = Appoinment(user=user, doc=doc, patientname=patientname, date=date, time=time, diseasedetails=diseasedetails)
        aobj.save()

        return HttpResponse("<script>alert('Appointment successful'); window.location.href='/doctorsearch/';</script>")

    return render(request, 'appointment.html', {'doc': doc})

def edit_docprofile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')  # Redirect to login page if user is not logged in

    user = get_object_or_404(doctoreg, email=email)

    if request.method == "POST":
        user.doctorname = request.POST.get("doctorname")
        user.specialization= request.POST.get("specialization")
        user.contact= request.POST.get("contact")
        user.licenseNumber= request.POST.get("licenseNumber")
        user.hospital = request.POST.get("hospital")
        user.username = request.POST.get("username")


        # Handle profile image upload
        if user.image:
            user.image = request.FILES.get('image')

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('docprofile')  # Redirect to the profile page after updating

    return render(request, 'edit_docprofile.html', {'user': user})

def edit_driverprofile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')  # Redirect to login page if user is not logged in

    user = get_object_or_404(usereg, email=email)

    if request.method == "POST":
        user.drivername = request.POST.get("drivername")
        user.vehicle= request.POST.get("vehicle")
        user.contact= request.POST.get("contact")
        user.licenseNumber= request.POST.get("licenseNumber")
        user.location = request.POST.get("location")
        user.username = request.POST.get("username")


        # Handle profile image upload
        if user.image:
            user.image = request.FILES.get('image')

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Redirect to the profile page after updating

    return render(request, 'edit_driverprofile.html', {'user': user})


def edit_pharmacyprofile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')  # Redirect to login page if user is not logged in

    user = get_object_or_404(pharmacy, email=email)

    if request.method == "POST":
        user.pharmacyname = request.POST.get("pharmacyname")
        user.ownername= request.POST.get("ownername")
        user.contact= request.POST.get("contact")
        user.licenseNumber= request.POST.get("licenseNumber")
        user.location = request.POST.get("location")

        # Handle profile image upload
        

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('pharmacypro')  # Redirect to the profile page after updating

    return render(request, 'edit_pharmacyprofile.html', {'user': user})





def feedback_rate(request):
    if request.method == 'POST':
        name = request.POST['name']
        feedback_text = request.POST['feedback_text']
        rating = int(request.POST['rating'])
        feedback = Feedback(name=name, feedback_text=feedback_text, rating=rating)
        feedback.save()
        return redirect('feedback_success')  # Redirect to the feedback list page after submission
    return render(request, 'feedback_rate.html')
def feedback_success(request):
    return render(request,'feedback_success.html')
def adminlog(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        u='admin@gmail.com'
        p='admin'
        if email==u:
            if password==p:
                return render(request,'adminindex.html')
    return render(request,'adminlog.html') 

def injuryinfo(request):
    if request.method=='POST':
        injuryname=request.POST.get('injuryname')
        injuryimg=request.FILES.get('injuryimg')
        procedure=request.POST.get('procedure')
        procedurevideo=request.FILES.get('procedurevideo')
        obj=injury(injuryname=injuryname,procedure=procedure,injuryimg=injuryimg,procedurevideo=procedurevideo)
        obj.save()
        return redirect('injurylist')
    return render(request,'injury.html')

def injurylist(request):
    user=injury.objects.all()
    return render(request,'injurylist.html',{'user':user})


def injuryinfolist(request):
    user=injury.objects.all()
    return render(request,'injuryinfolist.html',{'user':user})

def injurysearch(request):
    inj = []  # Default empty list for injuries to handle GET requests

    if request.method == 'POST':
        injury_name = request.POST.get('injury')
        print(f"Searching for injury: {injury_name}")  # Debugging line
        if injury_name:
            inj = injury.objects.filter(injuryname__icontains=injury_name)
        else:
            inj = injury.objects.all()

    else:
        inj = injury.objects.all()

    print(f"Found injuries: {inj}")  # Debugging line

    return render(request, 'injurys.html', {'inj': inj})

def pharmacyreg(request):  
    if request.method=='POST':
        pharmacyname=request.POST.get('pharmacyname')
        ownername=request.POST.get('ownername')
        contact=request.POST.get('contact')
        licenseNumber=request.POST.get('licenseNumber')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        location=request.POST.get('location')
        if password == confirmPassword:
            pharmacy(pharmacyname=pharmacyname,ownername=ownername,contact=contact,licenseNumber=licenseNumber,email=email,password=password,confirmPassword=confirmPassword,location=location).save()
            return redirect('pharmacylog')
        else:
            alert="<script> alert('Password Invalid!'); window.location.href='/pharmacyreg/'; </script>"
            return HttpResponse(alert)
    return render(request,'pharmacyreg.html')

def pharmacylist(request):
    user=pharmacy.objects.all()
    return render(request,'pharmacylist.html',{'user':user})

def pharmacylog(request):
    if request.method=='POST':
        ownername=request.POST.get('ownername')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=pharmacy.objects.filter(ownername=ownername,email=email,password=password).first()
        if user:
            request.session['email']=email
            if user.status=='approved':
                request.session['email']=user.email
                return  render(request, 'pharmacy.html')
            else:
               return render(request,'pharmacylog.html',
           {'error':'Your account is not yet approved. Please wait until the admin approves your registration'})
        else:
              return render(request,'pharmacylog.html',{'error':'invalid email or password'})
    else:
        error_msg="Invalid Username or Password!"
        return render(request, 'pharmacylog.html',{'error_msg':error_msg})


def updateStatus(request):
    if request.method =="POST":
        email=request.POST.get('email')
        status=request.POST.get('status')
        if not email or not status:
            return redirect('pharmacylist')
        if status not in['applied','approved','rejected']:
            return redirect('pharmacylist')
        
        constr=get_object_or_404(pharmacy,email=email)
        constr.status=status
        constr.save()
        return redirect('pharmacylist')

def pharma(request):
    return render(request,'pharmacy.html')

def feedbacklist(request):
    user=Feedback.objects.all()
    return render(request,'feedbacklist.html',{'user':user})

def deletefeed(request,id):
    a=Feedback.objects.get(id=id)
    a.delete()
    return redirect('feedbacklist')


def doctor_appointments(request):
    email=request.session.get('email')
    if email:
        doctor = get_object_or_404(doctoreg, email=email)
        appointments = Appoinment.objects.filter(doc=doctor).order_by('date', 'time')
        return render(request, 'docappointments.html', {'appointments': appointments})



def update_appointment_status(request, id):
    appointment = get_object_or_404(Appoinment, id=id)
    
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["Pending", "Confirmed", "Cancelled"]:
            appointment.status = new_status
            appointment.save()

            # Send email notification to the patient
            subject = "Appointment Status Update"
            message = f"Dear {appointment.patientname},\n\nYour appointment with Dr. {appointment.doc.doctorname} on {appointment.date} at {appointment.time} has been {new_status}.For any queries contact {appointment.doc.contact}\n\nBest Regards,\nClinic Team"
            recipient_email = appointment.user.email  # Assuming the user model has an email field
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            
            messages.success(request, "Appointment status updated and email sent successfully.")
    
    return redirect('docappointments')

def appointment_status(request):
    email=request.session.get('email')
    if email:
        obj = get_object_or_404(usereg, email=email)
        appointments = Appoinment.objects.filter(user=obj).order_by('date', 'time')
        return render(request, 'appointment_status.html', {'appointments': appointments})
def toggle_availability(request, id):
    email = request.session.get('email')
    if not email:
        return redirect('driverlogin')  # Redirect if not logged in

    try:
        dri = drivereg.objects.get(email=email, id=id)
         # Get driver by email & ID
        dri.availability_status = not dri.availability_status  # Toggle status correctly
        dri.save()
        return JsonResponse({"status": dri.availability_status})  # Return new status
    except drivereg.DoesNotExist:
        return JsonResponse({"error": "Driver not found"}, status=404)
    
def patient(request):
    email=request.session.get('email')
    if email:
        doctor = get_object_or_404(doctoreg, email=email)
        appointments = Appoinment.objects.filter(doc=doctor).order_by('date', 'time')
        return render(request, 'patient.html', {'appointments': appointments})
    
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
import random
from django.http import JsonResponse


otp_storage = {}  # Temporary storage for OTPs (Use cache or database in production)

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            usr = usereg.objects.get(email=email)
            otp = random.randint(100000, 999999)  # Generate 6-digit OTP
            
            otp_storage[email] = otp  # Store OTP temporarily
            
            # Send OTP via Email
            send_mail(
                "Password Reset OTP",
                f"Your OTP for password reset is {otp}",
                "newgrapes2025@gmail.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "OTP sent to your email.")
            return redirect("verify_otp")  # Redirect to OTP verification page
        except usereg.DoesNotExist:
            messages.error(request, "Email not found.")
    return render(request, "forgot_password.html")
def verify_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = int(request.POST.get("otp"))

        if otp_storage.get(email) == otp:  # Check if OTP matches
            messages.success(request, "OTP verified! You can reset your password.")
            return redirect("reset_password")  # Redirect to password reset page
        else:
            messages.error(request, "Invalid OTP.")
    return render(request, "verify_otp.html")
def reset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("password")

        try:
            usr = usereg.objects.get(email=email)
            usr.password = new_password  # Storing password as plain text (Use hashing in production)
            usr.save()
            messages.success(request, "Password reset successful. You can log in now!")
            otp_storage.pop(email, None)  # Remove OTP from storage
            return redirect("login")
        except usereg.DoesNotExist:
            messages.error(request, "Error resetting password.")
    return render(request, "reset_password.html")




#DOCTOR
def docforgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            usr = doctoreg.objects.get(email=email)
            otp = random.randint(100000, 999999)  # Generate 6-digit OTP
            
            otp_storage[email] = otp  # Store OTP temporarily
            
            # Send OTP via Email
            send_mail(
                "Password Reset OTP",
                f"Your OTP for password reset is {otp}",
                "newgrapes2025@gmail.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "OTP sent to your email.")
            return redirect("docverify_otp")  # Redirect to OTP verification page
        except doctoreg.DoesNotExist:
            messages.error(request, "Email not found.")
    return render(request, "docforgot_password.html")
def docverify_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = int(request.POST.get("otp"))

        if otp_storage.get(email) == otp:  # Check if OTP matches
            messages.success(request, "OTP verified! You can reset your password.")
            return redirect("docreset_password")  # Redirect to password reset page
        else:
            messages.error(request, "Invalid OTP.")
    return render(request, "docverify_otp.html")
def docreset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("password")

        try:
            usr = doctoreg.objects.get(email=email)
            usr.password = new_password  # Storing password as plain text (Use hashing in production)
            usr.save()
            messages.success(request, "Password reset successful. You can log in now!")
            otp_storage.pop(email, None)  # Remove OTP from storage
            return redirect("doctorlogin")
        except doctoreg.DoesNotExist:
            messages.error(request, "Error resetting password.")
    return render(request, "docreset_password.html")
