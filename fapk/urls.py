from .import views
from django.urls import path
urlpatterns = [
    
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('product/',views.addproduct,name='addproduct'),
    path('profilelist/',views.profilelist,name='profilelist'),
    path('productlist/',views.productlist,name='productlist'),
    path('logout/',views.logout,name='logout'),
    path('doctors/',views.doctor,name='doctor'),
    path('edit_docprofile/',views.edit_docprofile, name='edit_docprofile'),
    path('edit_driverprofile/',views.edit_driverprofile, name='edit_driverprofile'),
    path('edit_pharmacyprofile/',views.edit_pharmacyprofile, name='edit_pharmacyprofile'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('doctorhome/',views.doctorhome,name='doctorhome'),
    path('doctoregister/',views.doctoregister,name='doctoregister'),
    path('docprofile/',views.docprofile,name='docprofile'),
    path('doctoreglist/',views.doctoreglist,name='doctoreglist'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('doctorlogin/',views.doctorlogin,name='doctorlogin'),
    path('productsearch/',views.productsearch,name='productsearch'),
    path('driverlogin/',views.driverlogin,name='driverlogin'),
    path('driveregister/',views.driveregister,name='driveregister'),
    path('adproductlist/',views.adproductlist,name='adproductlist'),
    path('userlist/',views.userlist,name='userlist'),
    path('update_status/',views.update_status,name='update_status'),
    path('add_cart/<int:product_id>/',views.add_cart,name="add_cart"),
    path('quantity_form/<int:product_id>/', views.quantity_form, name='quantity_form'),
    path('my_cart/',views.my_cart,name='my_cart'),
    path('delete_cart/<int:cart_id>/',views.delete_cart,name='delete_cart'),
    path('doctorsearch/',views.doctorsearch,name='doctorsearch'),
    path('appointment/<int:id>/',views.appointment,name='appointment'),
    path('feedback_rate/',views.feedback_rate,name='feedback_rate'),
    path('feedback_success/',views.feedback_success,name='feedback_success'),
    path('feedbacklist/',views.feedbacklist,name='feedbacklist'),
    path('adminlog/',views.adminlog,name='adminlog'),
    path('injury/',views.injuryinfo,name='injury'),
    path('injurys/',views.injurysearch,name='injurys'),
    path('injurylist/',views.injurylist,name='injurylist'),
    path('injuryinfolist/',views.injuryinfolist,name='injuryinfolist'),
    path('driverhome/',views.driverhome,name='driverhome'),
    path('driversearch/',views.driversearch,name='driversearch'),
    path('pharmacy/',views.pharma,name='pharmacy'),
    path('pharmacyreg/',views.pharmacyreg,name='pharmacyreg'),
    path('pharmacylist/',views.pharmacylist,name='pharmacylist'),
    path('pharmacypro/',views.pharmacypro,name='pharmacypro'),
    path('pharmacylog/',views.pharmacylog,name='pharmacylog'),
    path('updateStatus/',views.updateStatus,name='updateStatus'),
    path('deletefeed/<int:id>/',views. deletefeed, name='deletefeed'),
    path('docappointments/',views. doctor_appointments, name='docappointments'),
    path('update-appointment/<int:id>/',views.update_appointment_status, name='update_appointment_status'),
    path('appointment_status/',views.appointment_status, name='appointment_status'),
    path('patient/',views.patient,name='patient'),

    #payment
    path("checkout/",views.initiate_payment, name="checkout"),
    path("payment_success/",views.payment_success, name="payment_success"),

    path('payhistory/',views.payhistory,name='payhistory'),
    path('deltrans/<int:id>/',views.deltrans,name='deltrans'),
    path('trackorder/',views.trackorder,name='trackorder'),
    path("toggle_availability/<int:id>/",views.toggle_availability, name="toggle_availability"),

    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("reset-password/", views.reset_password, name="reset_password"),

    path("docforgot-password/", views.docforgot_password, name="docforgot_password"),
    path("docverify-otp/", views.docverify_otp, name="docverify_otp"),
    path("docreset-password/", views.docreset_password, name="docreset_password"),

]