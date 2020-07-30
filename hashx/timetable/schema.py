import graphene
import django_filters
from graphene_django import DjangoObjectType
from hashx.mixins import ViewAllAuthenticatedQuery, AuthenticatedNode
from .models import Holidays, Location, OnlineClass, OfflineClass


class HolidaysFilter(django_filters.FilterSet):
    class Meta:
        model = Holidays
        fields = '__all__'


class HolidaysNode(DjangoObjectType):
    class Meta:
        model = Holidays
        interfaces = (AuthenticatedNode, )


class ClassFilter(django_filters.FilterSet):
    class Meta:
        model = OnlineClass
        fields = '__all__'


class ClassNode(DjangoObjectType):
    class Meta:
        model = OnlineClass
        interfaces = (AuthenticatedNode, )


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = '__all__'


class LocationNode(DjangoObjectType):
    class Meta:
        model = Location
        interfaces = (AuthenticatedNode, )


class RelayQuery(graphene.ObjectType):

    all_holidays = ViewAllAuthenticatedQuery(
        HolidaysNode, filterset_class=HolidaysFilter)
    holidays = AuthenticatedNode.Field(HolidaysNode)
    all_locations = ViewAllAuthenticatedQuery(
        LocationNode, filterset_class=LocationFilter)
    location = AuthenticatedNode.Field(LocationNode)
    all_classes = ViewAllAuthenticatedQuery(
        ClassNode, filterset_class=ClassFilter)
    classes = AuthenticatedNode.Field(ClassNode)
    node = AuthenticatedNode.Field()
