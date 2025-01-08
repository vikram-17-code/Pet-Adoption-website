from django.contrib import admin
from .models import breed,pet,adoption,Profile
from django.contrib.auth.models import User


admin.site.register(breed)
admin.site.register(pet)
admin.site.register(adoption)
admin.site.register(Profile)


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
#extend user model
class UserAdmin(admin.ModelAdmin):
    model = User 
    field = ["username","first_name","last_name","email"]
    inlines = [ProfileInline]
#unregister and re register the admin model
admin.site.unregister(User)
#
admin.site.register(User,UserAdmin)