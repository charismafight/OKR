from django.contrib import admin
from .models import Objective, Action


# Register your models here.
class ActionInline(admin.TabularInline):
    model = Action


@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    inlines = [
        ActionInline,
    ]
# admin.site.register(Objective)
# admin.site.register(Action)
