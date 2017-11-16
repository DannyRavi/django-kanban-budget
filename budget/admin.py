from django.contrib import admin

from .forms import TypeForm
from .models import Board, Column, Project, Tag, Type


class TypeAdmin(admin.ModelAdmin):
    form = TypeForm
    list_display = [
        'name',
        'swatch',
    ]


class ColumnAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'board',
        'position',
    ]
    ordering = ('position',)


class ColumnInlineAdmin(admin.TabularInline):
    model = Column
    extra = 0


class BoardAdmin(admin.ModelAdmin):
    inlines = [
        ColumnInlineAdmin,
    ]


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'name',
        'status',
        'position',
        'archive',
    ]
    ordering = (
        'status',
        'status__position',
    )
    list_editable = [
        'archive',
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Type, TypeAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Board, BoardAdmin)
