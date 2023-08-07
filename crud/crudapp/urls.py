from django.urls import path

from .views import Studentformview,Studentlist,StudentUpdateview,StudentDeleteView
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',Studentformview.as_view(),name='Studentformview'),
    path('studentlist',Studentlist.as_view(),name='studentlist'),
    path('StudentUpdateview/<int:id>',StudentUpdateview.as_view(),name='StudentUpdateview'),
    path('StudentDeleteView/<int:id>',StudentDeleteView.as_view(),name='StudentDeleteView'),
      
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)