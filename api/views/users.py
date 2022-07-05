from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from core.models import User
from api.serializers import ShortUserSerializer
from api.permissions import UsersPermission


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ShortUserSerializer.Meta.fields + ('password', )


class UsersListView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, UsersPermission]
    serializer_class = ShortUserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        else:
            return self.serializer_class


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'
    queryset = User.objects.all()

    permission_classes = [IsAuthenticated, UsersPermission]
    serializer_class = ShortUserSerializer
