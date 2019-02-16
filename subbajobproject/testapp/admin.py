from django.contrib import admin
from testapp.models import Hydjobs,Bangjobs,Chennaijobs,Punejobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eiligibility','address','email','phonenumber']

class BangjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eiligibility','address','email','phonenumber']
class ChennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eiligibility','address','email','phonenumber']
class PunejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eiligibility','address','email','phonenumber']

admin.site.register(Hydjobs,HydjobsAdmin)
admin.site.register(Bangjobs,BangjobsAdmin)
admin.site.register(Chennaijobs,ChennaijobsAdmin)
admin.site.register(Punejobs,PunejobsAdmin)