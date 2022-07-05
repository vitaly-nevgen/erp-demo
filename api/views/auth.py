from django.contrib.auth import login
from rest_framework import response, status, renderers
from rest_framework.authtoken.views import ObtainAuthToken


class AuthView(ObtainAuthToken):
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(status=status.HTTP_200_OK)
