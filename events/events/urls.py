"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from forms import contact

# admin.site.site_header = "MyClub Administration"
# admin.site.site_title = "MyClub Site Admin"
# admin.site.index_title = "MyClub Site Admin Home"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", contact.ContactUs.as_view(), name="contact"),
    path(
        "admin/password_reset/",
        auth_views.PasswordChangeView.as_view(),
        name="admin_password_reset",
    ),
    path(
        "admin/password_reset/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uid64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("", include("app.urls")),
]
