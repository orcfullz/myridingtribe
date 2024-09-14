# myridingtribe/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    # Redirect the root URL to the quiz start page
    path('', lambda request: HttpResponseRedirect('/quiz/')),
]
