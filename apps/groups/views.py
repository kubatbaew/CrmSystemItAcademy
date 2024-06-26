from django_filters import rest_framework
from rest_framework import filters

from rest_framework.viewsets import ModelViewSet

from apps.groups.models import Group
from apps.groups.serializers import GroupSerializer, GroupCreateSerializer, GroupListSerializer

from utils.permissions import IsMentor, IsManager
from utils.paginations import GroupsPagination


class GroupAPIViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsManager, IsMentor]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['direction']
    search_fields = ['title']
    pagination_class = GroupsPagination

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'patrial_update']:
            return GroupCreateSerializer
        if self.action == 'list':
            return GroupListSerializer
        return self.serializer_class
