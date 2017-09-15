from rest_framework import serializers

from . import models


class SearchKeySerializer(serializers.ModelSerializer):
    """Search Key serializer"""

    class Meta:
        model = models.SearchKeys
        exclude = ['id',]


class UserSerializer(serializers.ModelSerializer):
    """Search Key serializer"""

    class Meta:
        model = models.User
        fields = ('login', 'url','avatar_url','score','type','user_id')