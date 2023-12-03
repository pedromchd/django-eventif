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

    def save_model(self, request, obj, form, change):
        if not obj.replied and 'reply' in form.changed_data:
            obj.replied = True
            form.changed_data.append('replied')

        obj.save(update_fields=form.changed_data)


admin.site.register(Contact, ContactModelAdmin)
