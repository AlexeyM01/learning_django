from django.contrib import admin
from django.urls import include, path
# from mysite.polls.views import page_not_found

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("products/", include("products.urls")),
    path("admin/", admin.site.urls),
    path("", include('home_page.urls')),
]

# handler404 = page_not_found
