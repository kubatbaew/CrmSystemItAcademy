from rest_framework.viewsets import ModelViewSet

from apps.groups.models import Group
from apps.groups.serializers import GroupSerializer, GroupCreateSerializer, GroupListSerializer

from utils.permissions import IsMentor, IsManager


class GroupAPIViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsManager, IsMentor]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'patrial_update']:
            return GroupCreateSerializer
        if self.action == 'list':
            return GroupListSerializer
        return self.serializer_class
