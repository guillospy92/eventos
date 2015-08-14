from django.contrib import admin
from .models import Event, Category, Assistant, Comentario

# Register your models here.
#admin.site.register(Event)
#admin.site.register(Category)
#admin.site.register(Assistant)
#admin.site.register(Comentario)

class StackedItemInline(admin.StackedInline):
    classes = ('grp-collapse grp-open',)

class TabularItemInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)


class comentario(admin.TabularInline):
    model = Comentario



@admin.register(Event)
class EventAdmin(admin.ModelAdmin ):



	fieldsets = ( 


		('informacion del evento',{'fields':('name','summary','content','category','imagen')}),
		('lugares y fechas',{'fields':('place','start','finish')}),
		('organizador y precios',{'fields':('orginazer','is_free','amount','views')}),



		)


	inlines = [
        comentario,
    ]


     


	list_display = ('category','id','name','summary','content','start','finish')
	list_display_links = ('name','summary','content','start','finish',)
    
	search_fields = ('name','summary','content')

	


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','name',)
	list_display_links = ('name',)



@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
	list_display = ('attended','has_paid')
	list_display_links = ('attended','has_paid')
	filter_horizontal = ('event',)





@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('user','nombre','event','content')
	list_display_links = ('user','nombre','event','content')
	list_filter = ('user__first_name',)
	search_fields = ('nombre',)
	#list_editable  = ('content',)
