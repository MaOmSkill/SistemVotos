from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("", views.principal, name="principal"),
  path("campeon/<int:id>", views.campeon, name='campeon'),
  path("mostrar/<int:id>", views.mostrar, name='mostrar'),
  path("muybueno/<int:id>", views.muybueno, name='muybueno'),
  path("bueno/<int:id>", views.bueno, name='bueno'),
  path("suficiente/<int:id>", views.suficiente, name='suficiente'),
  path("deficiente/<int:id>", views.deficiente, name='deficiente'),
  path("pdf", views.pdf, name='pdf'),
   
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
