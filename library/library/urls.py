
from django.contrib import admin
from django.urls import path
from libraryapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Add/', Add_view),
    path('Display/', Display_view),
    path('Delete/', Delete_view),
    path('Update/', Update_view),
]
