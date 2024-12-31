from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from base.models import User, Court
from .serializers import UserSerializer, CourtSerializer
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import action

stripe.api_key = settings.STRIPE_SECRET_KEY

class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        sport = request.data.get('sport')
        num = request.data.get('num')
        token = request.data.get('token')
        amount = request.data.get('amount')

        try:
            user = User.objects.get(username=username)
            if user.is_manager:
                # Process payment
                charge = stripe.Charge.create(
                    amount=int(amount * 100),  # Amount in cents
                    currency='usd',
                    source=token,
                    description='Court Reservation Payment'
                )

                court = Court.objects.create(user=user, sport=sport, num=num)
                return Response({'message': 'Court created successfully', 'court_id': court.id, 'charge_id': charge.id}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Only managers can create courts'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)
        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        is_manager = request.data.get('is_manager', False)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create(
            username=username,
            password=make_password(password),
            is_manager=is_manager
        )
        
        return Response({'message': 'User created successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return Response({'message': 'Login successful', 'user_id': user.id, 'is_manager': user.is_manager}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)

class UserCourtsView(generics.ListAPIView):
    serializer_class = CourtSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        user = User.objects.get(id=user_id)
        return Court.objects.filter(user=user) | Court.objects.filter(user__isnull=True)

class ManagerCourtsView(generics.ListAPIView):
    serializer_class = CourtSerializer

    def get_queryset(self):
        return Court.objects.all()

class ReserveCourtView(generics.UpdateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

    def patch(self, request, *args, **kwargs):
        court_id = request.data.get('court_id')
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            court = Court.objects.get(id=court_id, user__isnull=True)
            court.user = user
            court.save()
            return Response({'message': 'Court reserved successfully'}, status=status.HTTP_200_OK)
        except Court.DoesNotExist:
            return Response({'error': 'Court is already reserved or does not exist'}, status=status.HTTP_400_BAD_REQUEST)

class CancelReservationView(generics.UpdateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

    def patch(self, request, *args, **kwargs):
        court_id = request.data.get('court_id')
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            court = Court.objects.get(id=court_id, user=user)
            court.user = None
            court.save()
            return Response({'message': 'Reservation canceled successfully'}, status=status.HTTP_200_OK)
        except Court.DoesNotExist:
            return Response({'error': 'Reservation does not exist or you do not have permission to cancel it'}, status=status.HTTP_400_BAD_REQUEST)

class ManagerUserView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        try:
            user = User.objects.get(username=username)
            if user.is_manager:
                users = User.objects.all()
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Only managers can view all users'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)

class PaymentView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            amount = request.data.get('amount')
            currency = request.data.get('currency', 'usd')
            token = request.data.get('token')

            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Amount in cents
                currency=currency,
                source=token,
                description='Court Reservation Payment'
            )

            return Response({'message': 'Payment successful', 'charge_id': charge.id}, status=status.HTTP_200_OK)
        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)