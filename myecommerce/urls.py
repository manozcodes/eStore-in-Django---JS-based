from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from myecommerce import settings
<<<<<<< HEAD
from . import views
=======
>>>>>>> 24802ca1dac3961a98947c235dfbc0f60ec727a7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
<<<<<<< HEAD
    path('', views.index),
=======
>>>>>>> 24802ca1dac3961a98947c235dfbc0f60ec727a7
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)