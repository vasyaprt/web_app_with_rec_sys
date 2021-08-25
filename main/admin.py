from django.contrib import admin
from .models import Tour, Guide, Rating, Order, Views

class TourAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'guide', 'price', 'type', 'duration', 'group')
admin.site.register(Tour,TourAdmin)

class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')
admin.site.register(Guide,GuideAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('user','tour', 'rating')
admin.site.register(Rating, RatingAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'order', 'time', 'msg')
admin.site.register(Order,OrderAdmin)

class ViewsAdmin(admin.ModelAdmin):
    list_display = ('user','tour')
admin.site.register(Views, ViewsAdmin)


