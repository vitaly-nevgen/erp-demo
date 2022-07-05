from rest_framework import generics, serializers

from core.models import User
from rest_framework.permissions import IsAuthenticated
from api.permissions import StructurePermission


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'subordinates')

    def get_fields(self):
        fields = super(StructureSerializer, self).get_fields()
        fields['subordinates'] = StructureSerializer(many=True)
        return fields


class StructureView(generics.ListAPIView):
    serializer_class = StructureSerializer
    queryset = User.objects.filter(supervisor=None)
    permission_classes = [IsAuthenticated, StructurePermission]
