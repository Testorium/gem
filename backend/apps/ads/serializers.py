from apps.ads.models import Ads
from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from apps.users.models import User
from rest_framework import serializers


class AdSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ads
        fields = "__all__"
