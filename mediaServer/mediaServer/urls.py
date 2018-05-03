
from django.contrib import admin
from django.urls import path,include
import RemoteFileViewer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('RemoteFileViewer.urls'))
]
