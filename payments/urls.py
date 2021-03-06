"""utils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('user-profile/', CustomUserView.as_view(), name="custom_profile_url"),
    path('accounts/', include('allauth.urls')),
    path('', OrganizationList.as_view(), name="organization_list_url"),
    path('create-organization/', OrganizationCreate.as_view(), name="organization_create_url"),
    path('organization/<str:slug>', OrganizationDetail.as_view(), name="organization_detail_url"),
    path('update/<str:slug>/', OrganizationUpdate.as_view(), name="organization_update_url"),
    path('organization/delete/<str:slug>', OrganizationDelete.as_view(), name="organization_delete_url"),
    path('new-payment/<str:slug>', PaymentCreate.as_view(), name="payment_create_url"),
    path('archive/<str:slug>', PaymentArchive.as_view(), name="payment_archive_url"),
    path('payment/<int:pk>', PaymentDetail.as_view(), name="payment_detail_url"),
    path('payment/delete/<int:pk>', PaymentDelete.as_view(), name="payment_delete_url"),
    path('cart/add/<int:pk>', CartAdding.as_view(), name="cart_adding_url"),
    path('cart/delete/', CartItemDelete.as_view(), name="cart_delete_url"),
    path('checkout/', Checkout.as_view(), name="checkout_url"),
    path('profile-settings/', ProfileSettings.as_view(), name="profile_settings_url"),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order_detail_url"),
    path('icon_select/', IconSelect.as_view(), name="icon_select_url"),


]
