from django.urls import include, path
from rest_framework import routers

from payments.views import CheckoutSessionViewSet

payments_router = routers.DefaultRouter()
payments_router.register(
    "checkout-session", CheckoutSessionViewSet, basename="checkout-session"
)


urlpatterns = [path("", include(payments_router.urls))]
