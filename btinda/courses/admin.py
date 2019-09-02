from django.contrib import admin
from .models import Course, Livreur

class CourseAdmin(admin.ModelAdmin):
   list_display   = ('exp_nom', 'exp_tel','dest_nom','dest_tel','dest_adresse','dest_colis','livreur', 'date')
   list_filter    = ('livreur','date',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('dest_adresse', 'dest_colis')

# Register your models here.

admin.site.register(Course,CourseAdmin)
admin.site.register(Livreur)

