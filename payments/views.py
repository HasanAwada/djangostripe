import stripe
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

from config.settings import STRIPE_SECRET_KEY, SITE_URL

# This is your test secret API key.
stripe.api_key = STRIPE_SECRET_KEY


class CheckoutSessionViewSet(GenericViewSet, mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1PDklpFx4fme3WfqrQfNvpmm',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=SITE_URL + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=SITE_URL + '?canceled=true',
            )
            return redirect(checkout_session.url)
        except Exception as e:
            return Response({'error': str(e)}, status=status)
