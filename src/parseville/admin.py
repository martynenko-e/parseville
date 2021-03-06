# Register your models here.
from django.contrib import admin
from .models import *


class AdminCity(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show')
    list_editable = ('show',)


class AdminCountry(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show')
    list_editable = ('show',)


class AdminProgram(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show')
    list_editable = ('show',)


class AdminLink(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show', 'url', 'date')
    list_editable = ('show',)


class AdminCompany(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show', 'show_on_main', 'url', 'has_logo', 'extra', 'date')
    list_editable = ('show', 'show_on_main')

    def has_logo(self, obj):
        return obj.logo != ""

    has_logo.boolean = True


class AdminVacancy(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show', 'company', 'extra')
    list_editable = ('show',)


class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'office', 'date')


class AdminNews(admin.ModelAdmin):
    list_display = ('name', 'date')


class AdminOffice(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'company', 'city', 'phone')


admin.site.register(Country, AdminCountry)
admin.site.register(City, AdminCity)
admin.site.register(UsefulLink, AdminLink)
admin.site.register(Company, AdminCompany)
admin.site.register(Vacancy, AdminVacancy)
admin.site.register(ProgrammingLanguage, AdminProgram)
admin.site.register(Event, AdminEvent)
admin.site.register(Office, AdminOffice)
admin.site.register(News, AdminNews)
