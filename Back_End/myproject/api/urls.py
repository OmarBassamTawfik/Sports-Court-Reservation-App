from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, SignupView, LoginView, UserCourtsView, ManagerCourtsView, ReserveCourtView, CancelReservationView, ManagerUserView

router = DefaultRouter()
router.register(r'courts', CourtViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-courts/', UserCourtsView.as_view(), name='user-courts'),
    path('manager-courts/', ManagerCourtsView.as_view(), name='manager-courts'),
    path('reserve-court/', ReserveCourtView.as_view(), name='reserve-court'),
    path('cancel-reservation/', CancelReservationView.as_view(), name='cancel-reservation'),
    path('manager-users/', ManagerUserView.as_view(), name='manager-users'),
]