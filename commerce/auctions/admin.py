from django.contrib import admin
from auctions.models import WatchList
# Register your models here.
from .models import Listings, Comments, Bids, WatchList, CloseListing

admin.site.register(Listings)

admin.site.register(Comments)

admin.site.register(Bids)

@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['id', 'listing', 'user']


admin.site.register(CloseListing)