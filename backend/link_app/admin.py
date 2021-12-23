from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.utils.translation import ngettext


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'is_teacher', 'is_student',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Additional info', {
            'fields': ('is_student', 'roll_no', 'is_teacher', 'faculty_code')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Additional info', {
            'fields': ('is_student',  'roll_no', 'is_teacher', 'faculty_code')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'year', 'category',
                    'material', 'isApproved')
    fieldsets = (
        (None, {
            'fields': ('subject_code', 'year', 'category', 'material', 'isApproved')
        }),
    )
    actions = ['approve_resources']
    readonly_fields = ('uploaded_at',)

    @admin.action(description='Approve selected resources')
    def approve_resources(self, request, queryset):
        updated = queryset.update(isApproved=True)
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)


class NotificationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Resource, ResourceAdmin)
admin.site.register(models.Notification, NotificationAdmin)
admin.site.register(models.Doubt)
admin.site.register(models.Solution)
