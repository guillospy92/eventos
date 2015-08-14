from django.contrib import admin
from .models import User




@admin.register(User)
class UserAdmin(admin.ModelAdmin):

	fieldsets = (

		('User',{'fields' :('username','password')}),
		('personal info',{'fields' : ('first_name','last_name','email','avatar')}),
		('permisos',{'fields': ('is_active','is_staff','groups','is_superuser','user_permissions')}),
		)

	list_display = ('id','username','email','first_name','last_name','avatar')
	list_display_links = ('username','email','first_name','last_name','avatar')
	search_fields = ('username','first_name')
	filter_horizontal = ('user_permissions','groups')
	list_filter = ('is_superuser',)
	