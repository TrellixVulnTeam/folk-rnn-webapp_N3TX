from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from archiver.models import User, Tune, TuneAttribution, TuneRecording, TuneEvent, Setting, Comment, Recording, Event

class TuneAttributionInline(admin.StackedInline):
    model = TuneAttribution

class SettingInline(admin.StackedInline):
    model = Setting
     
class CommentInline(admin.StackedInline):
    model = Comment

class TuneRecordingInline(admin.StackedInline):
    model = TuneRecording

class TuneEventInline(admin.StackedInline):
    model = TuneEvent

@admin.register(Tune)
class TuneAdmin(admin.ModelAdmin):
    inlines = [ TuneAttributionInline, SettingInline, CommentInline, TuneEventInline, TuneRecordingInline ]

@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):
    inlines = [ TuneRecordingInline ]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ TuneEventInline ]

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Define admin model for User with email address as username
    """

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)