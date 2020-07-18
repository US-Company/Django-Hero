from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Table
from .models import Color
from .models import Label
from .models import Item
from .models import CheckList

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    readonly_fields = ('pre_background',)
    fields = ('name_table', 'background_table', 'pre_background',)

    def pre_background(self, obj):
        background_resize = mark_safe(
            '<img class="responsive-img" src="{url}" width="{width}" \
            height={height} />'.format(
                url = obj.background_table.url,
                width= int(obj.background_table.width) * 0.2,
                height= int(obj.background_table.height) * 0.2,
            )
        )
        return background_resize

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    readonly_fields = ('pre_color',)
    fields = ('name_color', 'code_color', 'pre_color')

    def pre_color(self, obj):
        color_div = mark_safe(
            '<div style="background-color:{color_code}; width:100px;\
            height:100px;"></div>'.format(
                    color_code = obj.code_color
                )
        )
        return color_div

# admin.site.register(Table)
# admin.site.register(Color)
admin.site.register(Label)
admin.site.register(Item)
admin.site.register(CheckList)
