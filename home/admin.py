from django.contrib import admin
from home.models import*
# Register your models here.
@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone','subject','message',)

@admin.register(properties)
class productadmin(admin.ModelAdmin):
    pass
@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass
@admin.register(faq)
class faqadmin(admin.ModelAdmin):
    pass
