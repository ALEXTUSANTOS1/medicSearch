from django.contrib import admin

from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birthday')
    empty_value_display = '-empty-'
    list_display_links = ('user','role')
    list_filter = ('user__is_active', 'role')
    fields = ('user', ('role',), 'image', 'birthday', 'specialities', 'addresses',)
    exclude = ('favorites', 'created_at', 'updated_at',)
    readonly_fields = ('user',)
    search_fields = ('user__username',)








admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
