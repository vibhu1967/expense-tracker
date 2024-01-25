"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from expenses.views import Approved, Expense, Pending, Rejected

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense/', Expense.as_view()),
    path('expense/<int:id>', Expense.as_view()),
    path('expense/approved/', Approved.as_view()),
    path('expense/pending/', Pending.as_view()),
    path('expense/rejected/', Rejected.as_view())
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
