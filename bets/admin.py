from django.contrib import admin
from bets.models import BetRoom, Option

# Register your models here.
class OptionsInline(admin.TabularInline):
	model = Option
	extra = 3

class BetRoomsAdmin(admin.ModelAdmin):
	list_display = ('room_name','date_created','url')
	list_filter = ['date_created']
	search_fields = ['room_name']
	fieldsets = [
		(None, 				 {'fields': ['room_name']}),
		('Date information', {'fields': ['date_created']}),
		('URL', 			 {'fields': ['url']})
	]
	inlines = [OptionsInline]

admin.site.register(BetRoom, BetRoomsAdmin)