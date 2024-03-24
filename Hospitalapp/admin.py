from django.contrib import admin
from .models import Homes,Branch,Gallery,Blog,Package
# Register your models here.
class HomesAdmin(admin.ModelAdmin):
    list_display=['name','image']
admin.site.register(Homes,HomesAdmin)




class BranchAdmin(admin.ModelAdmin):
    list_display=['image','name']
admin.site.register(Branch,BranchAdmin)





class GalleryAdmin(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Gallery,GalleryAdmin)



class BlogAdmin(admin.ModelAdmin):
    list_display=['image','name']
admin.site.register(Blog,BlogAdmin)



class PackageAdmin(admin.ModelAdmin):
    list_display=['image','price','name','ln1','ln2','ln3','ln4','ln5','ln6','ln7','ln8','ln9','ln10','ln11','ln12','ln13']
admin.site.register(Package,PackageAdmin)





