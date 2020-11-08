#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 10:43.

from django.urls import path, include

from .views import *

app_name = "homepage"

# testimonials_patterns = ([
#                              path('create/', TestimonialsCreate.as_view(), name='create'),
#                              path('<int:pk>/edit/', TestimonialsEdit.as_view(), name='edit'),
#                              path('<int:pk>/delete', TestimonialsDelete.as_view(), name='delete'),
#                          ], 'testimonials')
#
# clients_image_patterns = ([
#                               path('create/', ClientsImageCreate.as_view(), name='create'),
#                               path('<int:pk>/edit/', ClientsImageEdit.as_view(), name='edit'),
#                               path('<int:pk>/delete', ClientsImageDelete.as_view(), name='delete'),
#                           ], 'clientsimage')

homepage_patterns = ([
                         path('', homepage_view, name='view'),
                         path('<int:pk>/edit/', HomePageEdit.as_view(), name='edit'),
                     ], 'homepage')

urlpatterns = [
    path('homepage/', include(homepage_patterns)),
    # path('testimonials/', include(testimonials_patterns)),
    # path('clients/image/', include(clients_image_patterns)),
]
