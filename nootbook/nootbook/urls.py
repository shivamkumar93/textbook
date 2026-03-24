
from django.contrib import admin
from django.urls import path
from book.views import *
from django.conf import settings
from django.conf.urls.static import static
from book.admin_views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="homepage"),


# Admin urls Here
    path("dashboard/", dashboard, name="admin_dashboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
