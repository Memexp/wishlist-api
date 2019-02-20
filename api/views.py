from django.shortcuts import render
from items.models import Item
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ItemListSerializer, ItemDetailSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import UserOrStaffPermission


class ItemListView(ListAPIView):
	queryset= Item.objects.all()
	serializer_class= ItemListSerializer
	filter_backends = [SearchFilter, OrderingFilter,]
	search_fields= ['image', 'name','description', 'added_by__first_name', ]
	permission_classes= [AllowAny, ]


class ItemDetailView(RetrieveAPIView):
	queryset= Item.objects.all()
	serializer_class= ItemDetailSerializer
	lookup_field= 'id'
	lookup_url_kwarg= 'item_id'
	permission_classes= [IsAuthenticated, UserOrStaffPermission, ]

