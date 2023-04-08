
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from my_profile.views import HomePageView,AboutUsView,ContactUsView,AuthorView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(),name='home'),
    path('about_me',AboutUsView.as_view(),name='about_me'),
    path('contact_us',ContactUsView.as_view(),name='contact_us'),
    path('author',AuthorView.as_view(),name='author'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)