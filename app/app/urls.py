#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/09/2020 11:29.
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('config/', include('config.urls')),
    path('service/', include('service.urls')),
    path('financial/', include('financial.urls')),
    path('business/', include('business.urls')),
]

# only for debug mode?
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Handling errors, but only if debug is set to False and there is another server to serve staticfiles
handler400 = 'frontend.views.error_400'
handler401 = 'frontend.views.error_401'
handler403 = 'frontend.views.error_403'
handler404 = 'frontend.views.error_404'
handler500 = 'frontend.views.error_500'
handler503 = 'frontend.views.error_503'
