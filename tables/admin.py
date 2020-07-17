from django.contrib import admin
from .models import Table
from .models import Color
from .models import Label
from .models import Item
from .models import CheckList

# Register your models here.

admin.site.register(Table)
admin.site.register(Color)
admin.site.register(Label)
admin.site.register(Item)
admin.site.register(CheckList)
