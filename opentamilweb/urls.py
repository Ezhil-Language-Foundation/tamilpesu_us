"""opentamilweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
import sys

if sys.version.find("2.6") >= 0:
    urlpatterns = [
        path("", include("opentamilapp.urls")),
        path("vennila/",include("vennila.urls"))
    ]
else:
    urlpatterns = [
        path("i18n/", include("django.conf.urls.i18n")),
    ]
    urlpatterns += i18n_patterns(
        # url(r'^admin/', admin.site.urls),
        re_path(_(r""), include("opentamilapp.urls")),
    )
    urlpatterns += i18n_patterns(
        re_path(_(r"vennila/"), include("vennila.urls")),
    )

