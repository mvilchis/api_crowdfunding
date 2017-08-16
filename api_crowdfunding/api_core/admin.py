# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  *
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'ID_Proyecto' )
class UserAdmin(admin.ModelAdmin):
    list_display = ('user','ID_usuario', 'Estado')
class FundingAdmin(admin.ModelAdmin):
    list_display = ('user', 'ID_Proyecto', 'ID_Usuario')


admin.site.register(ProjectDonation, ProjectAdmin)
admin.site.register(ProjectDeuda, ProjectAdmin)
admin.site.register(ProjectRecompesas, ProjectAdmin)
admin.site.register(ProjectCapital,ProjectAdmin)
admin.site.register(UserDonation,UserAdmin)
admin.site.register(UserRecompensas, UserAdmin)
admin.site.register(UserDeuda,UserAdmin)
admin.site.register(UserCapital,UserAdmin)
admin.site.register(FundingDonation,FundingAdmin)
admin.site.register(FundingCapital,FundingAdmin)
admin.site.register(FundingDeuda,FundingAdmin)
admin.site.register(FundingRecompensas,FundingAdmin)
