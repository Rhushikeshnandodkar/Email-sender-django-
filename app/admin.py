from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(GroupModel)
admin.site.register(LableModel)
admin.site.register(SectorModel)
class customer_list(resources.ModelResource):
    class Meta:
        model = SubscribersModel
        fields = ('id', 'first_name', 'last_name', 'email', 'label', 'group', 'sector', 'subscription')
class UserAdmin(ImportExportModelAdmin):
    resource_class = customer_list
admin.site.register(SubscribersModel, UserAdmin)
admin.site.register(CampaignsModel)
