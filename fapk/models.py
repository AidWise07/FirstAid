from django.db import models

# Create your models here.
class usereg(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
    confirmPassword=models.CharField(max_length=10)
    status=models.CharField(max_length=50)
    check_password=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',blank=True,null=True)

class product(models.Model):
    productname=models.CharField(max_length=50)
    manufacturer=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    image=models.ImageField(upload_to='productimage/',blank=True,null=True)
    sellername=models.CharField(max_length=50)
    sellercontact=models.IntegerField()
    sellermail=models.CharField(max_length=100)
    

class doctor(models.Model):
    doctorname=models.CharField(max_length=100)
    contact=models.IntegerField()
    specialization=models.CharField(max_length=100)

    

class doctoreg(models.Model):
    doctorname=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    contact=models.IntegerField()
    licenseNumber=models.CharField(max_length=50)
    hospital=models.CharField(max_length=250)
    image=models.ImageField(upload_to='doctorimage/',blank=True,null=True)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    confirmPassword=models.CharField(max_length=10)
    
class drivereg(models.Model):
    drivername=models.CharField(max_length=100)
    vehicle=models.CharField(max_length=100)
    contact=models.IntegerField()
    licenseNumber=models.CharField(max_length=50)
    image=models.ImageField(upload_to='driverimage/',blank=True,null=True)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    confirmPassword=models.CharField(max_length=10)
    location=models.CharField(max_length=10,blank=True,null=True)
    availability_status=models.BooleanField(default=False)

    
    
    def __str__(self):
        return self.drivername
    

class RideRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(usereg,on_delete=models.CASCADE)
    driver = models.ForeignKey(drivereg, on_delete=models.SET_NULL, null=True, blank=True)  
    location = models.CharField(max_length=255) 
    contact = models.CharField(max_length=15)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  # Request status
    requested_at = models.DateTimeField(auto_now_add=True)  # Time when the request was made

    def __str__(self):
        return f"{self.name} - {self.location} ({self.status})"
    
class Appoinment(models.Model):
    user=models.ForeignKey(usereg,on_delete=models.CASCADE,null=False)
    doc=models.ForeignKey(doctoreg,on_delete=models.CASCADE)
    patientname=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    diseasedetails=models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],default='Pending')

    def __str__(self):
        return f"{self.user.firstName} - Dr. {self.doc.doctorname} on {self.date}"

class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'), 
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
class injury(models.Model):
    injuryname=models.CharField(max_length=100)
    injuryimg=models.ImageField(upload_to='injuryimg/',null=True,blank=True)
    procedure=models.CharField(max_length=2000)
    procedurevideo = models.FileField(upload_to='injuryprocvideo/',null=True,blank=True)

    

class pharmacy(models.Model):
    pharmacyname=models.CharField(max_length=100)
    ownername=models.CharField(max_length=100)
    licenseNumber=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirmPassword=models.CharField(max_length=100)
    status=models.CharField(max_length=50,null=True,blank=True)



class Cart(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(usereg,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    total=models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True) 
    

class Transaction(models.Model):
    user = models.ForeignKey(usereg, on_delete=models.CASCADE)
    cart_details = models.JSONField(blank=True, null=True)
    razorpay_order_id = models.CharField(max_length=100, unique=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Pending")  # Pending, Paid, Failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.razorpay_order_id} - {self.status}"