from django.contrib import admin
# from loginpage.models import userdetail
from loginpage.models import signdetail
from loginpage.models import contactdetail
from loginpage.models import bookingdetail
from loginpage.models import feedback
from loginpage.models import registerdetail
from loginpage.models import supplierdetail
from loginpage.models import contractordetail
# class useradmin(admin.ModelAdmin):
#     list_display=('email','password')
    # admin.site.register(userdetail,useradmin)
class book(admin.ModelAdmin):
    list_display=('name','email','phone','appointmentDate','services','timeSlot')
admin.site.register(bookingdetail,book)

class contact(admin.ModelAdmin):
    list_display=('name','email','text')
admin.site.register(contactdetail,contact)




class signup(admin.ModelAdmin):
    list_display=('Name','Email','Password','Cpassword')
    
admin.site.register(signdetail,signup)

class feed(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(feedback,feed)


class register4(admin.ModelAdmin):
    list_display=('name','email','pass1')
admin.site.register(registerdetail,register4)


class supplier(admin.ModelAdmin):
    list_display=('name','email','phone','address')
admin.site.register(supplierdetail,supplier)


class contractor(admin.ModelAdmin):
    list_display=('name','email','phone','address')
admin.site.register(contractordetail,contractor)

# Register your models here.








