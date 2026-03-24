
from django.contrib import admin
from django.urls import path
from book.views import *
from django.conf import settings
from django.conf.urls.static import static
from book.admin_views import *
from book.auth_views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="homepage"),
    path("filter/", filterbook, name="filter"),
    path("filter/<slug:slug>/", filterbook, name="category_filter"),
    path("bookview/<slug:slug>/", bookview, name="bookview"),


# Admin urls Here
    path("dashboard/", dashboard, name="admin_dashboard"),
    path("manage-author/", manageAuthor, name="manageAuthor"),
    path("manage-book/", manageBooks, name="manageBook"),
    path("manage-Genere/", manageGeneres, name="manageGenere"),
    path("insert-book/", insertBook, name="insertBook"),

# Auth Urls Here
    path("auth-login/", authlogin, name="authlogin"),
    path("auth-register/", register, name="authregister"),
    path("auth-logout/", authlogout, name="authlogout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
