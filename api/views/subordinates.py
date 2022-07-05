from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from core.models import User
from api.permissions import SubordinatesPermission
from api.serializers import ShortUserSerializer


class UserSubordinatesSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'subordinates': ShortUserSerializer(
                instance.subordinates.all(),
                many=True
            ).data
        }

    class Meta:
        model = User
        fields = ('subordinates', )


class UserSubordinatesView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, SubordinatesPermission]
    serializer_class = UserSubordinatesSerializer
