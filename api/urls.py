from django.urls import path

from api.views.auth import AuthView
from api.views.structure import StructureView
from api.views.users import UsersListView, UserDetailView
from api.views.subordinates import UserSubordinatesView
from api.views.supervisor import UserSupervisorView


urlpatterns = (
    path('auth/', AuthView.as_view()),
    path('user/', UsersListView.as_view()),
    path('user/<int:user_id>/', UserDetailView.as_view()),
    path('user/<int:user_id>/subordinates/', UserSubordinatesView.as_view()),
    path('user/<int:user_id>/supervisor/', UserSupervisorView.as_view()),
    path('structure/', StructureView.as_view()),
)
