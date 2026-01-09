from django.contrib import admin
from django.urls import path , include
from .views import home , salvar , editar , deletar , api_hello , api_test
from . import views

from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>/', editar , name='editar'),
    path('deletar/<int:id>/', deletar , name='deletar'),

    # API URLs
    path('api/pessoas/', views.pessoa_list_create),
    path('api/pessoas/<int:id>/', views.pessoa_detail),
    path('api/hello/', views.api_hello),
    path('api/teste/', views.api_test),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
