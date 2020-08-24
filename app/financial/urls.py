#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 10:24.
from django.urls import path, include

from .views import *

app_name = "financial"

invoice_patterns = ([
                        path('<int:spk>/create/', InvoiceCreate.as_view(), name='create'),
                        path('<int:spk>/<int:pk>/edit/', InvoiceEdit.as_view(), name='edit'),
                        path('<int:spk>/<int:pk>/delete/', InvoiceDel.as_view(), name='delete'),
                    ], 'invoice')

urlpatterns = [
    path('invoice/', include(invoice_patterns)),
]
