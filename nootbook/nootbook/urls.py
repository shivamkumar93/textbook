
from django.contrib import admin
from django.urls import path
from book.views import *
from django.conf import settings
from django.conf.urls.static import static
from book.admin_views import *
from book.auth_views import *
from book.checkout_views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="homepage"),
    path("filter/", filterbook, name="filter"),
    path("filter/<slug:slug>/", filterbook, name="category_filter"),
    path("bookview/<slug:slug>/", bookview, name="bookview"),
    path("cart/", cart, name='cart'),



# Admin urls Here
    path("dashboard/", dashboard, name="admin_dashboard"),
    path("manage-author/", manageAuthor, name="manageAuthor"),
    path("manage-book/", manageBooks, name="manageBook"),
    path("manage-Genere/", manageGeneres, name="manageGenere"),
    path("insert-book/", insertBook, name="insertBook"),
    path("update-book/<int:id>/", updateBook, name="updatebook"),
    path("update-genere/<int:id>/", updateGenere, name="updategenere"),
    path("update-author/<int:id>/", updateAuthor, name="updateauthor"),
    path("delete-book/<int:id>/", deleteBook, name="deletebook"),
    

# Auth Urls Here
    path("auth-login/", authlogin, name="authlogin"),
    path("auth-register/", register, name="authregister"),
    path("auth-logout/", authlogout, name="authlogout"),

# checkout urls here
    path("checkout/addTocart/<slug:slug>/", addTocart, name="addTocart"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
