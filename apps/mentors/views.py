from django_filters import rest_framework
from rest_framework import filters

from rest_framework import viewsets, decorators, response

from apps.mentors.serializers import MentorSerializer, MentorCreateSerializer, MentorRetrieveSerializer
from apps.mentors.models import Mentor

from apps.groups.serializers import GroupSerializer

from utils.permissions import IsManager, IsMentor


class MentorAPIViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsMentor]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['direction']
    search_fields = ['full_name', 'username']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'patrial_update']:
            return MentorCreateSerializer
        if self.action == 'retrieve':
            return MentorRetrieveSerializer
        return self.serializer_class

    @decorators.action(methods=['GET'], url_path="groups", detail=True)
    def group_action(self, request, pk=None):
        obj = self.get_object()
        groups = obj.mentor_groups.all()

        serializer = GroupSerializer(data=[i.__dict__ for i in groups], many=True, instance=groups)
        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.data, status=200)

        