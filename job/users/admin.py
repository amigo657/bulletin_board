from django.contrib import admin
from users.models import User

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ("username", "is_staff", "is_active") #указывает какие поля отображать на странице списка объектов
    # readonly_fields = ("username", "last_login") #Поля указанные в этой настройке будут отображаться значение без возможности редактировать
    list_filter = ("is_staff", "is_active") #активация фильтров на правой боковой панели страницы списка изменений администратора
    search_fields = ("username",) #отображает панель поиска, которая производит поиск по полям
    fieldsets = (   #Позволяет изменить макет страниц добавления и редактирования объекта
        (
            None,
            {
                "fields": ("username", "password", "is_staff", "last_login",)
            },
        ),
    )


admin.site.register(User, AdminUser) #Зарегистрировать модель User с настройками AdminUser