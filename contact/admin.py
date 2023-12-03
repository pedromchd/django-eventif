from django.contrib import admin

from contact.models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'created_at',
        'updated_at',
        'replied',
    ]
    date_hierarchy = 'created_at'
    search_fields = [
        'name',
        'email',
        'phone',
        'message',
        'created_at',
        'reply',
        'updated_at',
    ]
    list_filter = ['created_at', 'updated_at', 'replied']


admin.site.register(Contact, ContactModelAdmin)
