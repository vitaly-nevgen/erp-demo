from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from core.models import User
from api.permissions import SupervisorPermission
from api.serializers import ShortUserSerializer


class UserSupervisorSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'supervisor': ShortUserSerializer(instance.supervisor).data
        }

    class Meta:
        model = User
        fields = ('supervisor', )


class UserSupervisorView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, SupervisorPermission]
    serializer_class = UserSupervisorSerializer
