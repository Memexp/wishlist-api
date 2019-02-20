from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]

class FavSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = FavoriteItem
        fields = ['user']


class ItemListSerializer(serializers.ModelSerializer):
    favorited = serializers.SerializerMethodField()

    detail= serializers.HyperlinkedIdentityField(
        view_name='api-detail',
        lookup_field= 'id',
        lookup_url_kwarg= 'item_id'
        )

    added_by = UserSerializer()

    def get_favorited(self, obj):
        return obj.items.count()

    class Meta:
        model = Item
        fields = ['image', 'name','description', 'detail', 'added_by','favorited',]



class ItemDetailSerializer(serializers.ModelSerializer):
    
    items = FavSerializer(many=True)

    class Meta:
        model = Item
        fields = [ 'image', 'name', 'description', 'items', ]




