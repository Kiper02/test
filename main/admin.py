from django.contrib import admin

from main.models import Cards, CardsBig



admin.site.register(CardsBig)

@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
