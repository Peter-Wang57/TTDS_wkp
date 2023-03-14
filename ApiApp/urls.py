# from django.conf.urls import re_path

from django.urls import path
from ApiApp import views
from django.urls import re_path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',views.home),
    path('my_view',views.my_view),
    # re_path(r'^department$',views.departmentApi),
    # re_path(r'^department/([0-9]+)$',views.departmentApi),

    # re_path(r'^employee$',views.employeeApi),
    # re_path(r'^employee/([0-9]+)$',views.employeeApi),

    # re_path(r'^employee/savefile',views.SaveFile)
]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



