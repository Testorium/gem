from apps.ads.models import Ads
from apps.ads.serializers import AdSerializer
from apps.offers.models import Offer
from apps.users.serializers import UserSerializer
from rest_framework import serializers


class OfferCreateSerializer(serializers.ModelSerializer):
    user_sender = UserSerializer(read_only=True)
    user_receiver = UserSerializer(read_only=True)
    ad_sender = AdSerializer(read_only=True)
    ad_receiver = AdSerializer(read_only=True)

    ad_sender_id = serializers.PrimaryKeyRelatedField(
        source="ad_sender", queryset=Ads.objects.all(), write_only=True
    )
    ad_receiver_id = serializers.PrimaryKeyRelatedField(
        source="ad_receiver", queryset=Ads.objects.all(), write_only=True
    )

    class Meta:
        model = Offer
        fields = [
            "id",
            "user_sender",
            "user_receiver",
            "ad_sender",
            "ad_receiver",
            "ad_sender_id",
            "ad_receiver_id",
            "comment",
            "created_at",
        ]

    def create(self, validated_data):
        ad_sender = validated_data["ad_sender"]
        validated_data["user_sender"] = self.context["request"].user
        validated_data["user_receiver"] = ad_sender.user
        return super().create(validated_data)


class OfferUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Offer.STATUS_CHOICES)

    class Meta:
        model = Offer
        fields = ["status"]
