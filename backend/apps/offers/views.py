from apps.offers.models import Offer
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import OfferCreateSerializer, OfferUpdateSerializer


class OfferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

    def get_queryset(self):
        user = self.request.user
        return Offer.objects.filter(Q(user_sender=user) | Q(user_receiver=user))

    def get_serializer_class(self):
        if self.action == "create":
            return OfferCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return OfferUpdateSerializer
        return OfferCreateSerializer

    def perform_create(self, serializer):
        ad_sender = serializer.validated_data["ad_sender"]
        serializer.save(
            user_sender=self.request.user,
            user_receiver=ad_sender.user,
        )
