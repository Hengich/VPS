from django.contrib import admin

from .models import VPS


class VPSAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке
    list_display = ('uid', 'cpu', 'ram', 'hdd', 'status')

    # Поля, по которым доступен поиск
    search_fields = ('uid', 'status')

    # Фильтры в панели админки
    list_filter = ('status', 'cpu', 'ram', 'hdd')

    # Поля, которые можно редактировать в списке
    list_editable = ('status',)

    # Поля для детальной формы редактирования
    fields = ('cpu', 'ram', 'hdd', 'status')


admin.site.register(VPS, VPSAdmin)
