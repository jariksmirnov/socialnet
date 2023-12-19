from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.db.models import Count, DateField
from django.db.models.functions import TruncDay
from votes.models import Vote
from user_profile.models import UserProfile
from django.utils import timezone


class BlacklistTokenUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print('Error processing posting:', e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AnalyticsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        # convert date_to to a datetime object and add one day
        date_to_datetime = timezone.datetime.fromisoformat(date_to)
        date_to = date_to_datetime + timezone.timedelta(days=1)

        # filter for upvotes only
        votes = Vote.objects.filter(created_at__range=[date_from, date_to], up_vote_by__isnull=False)

        # aggregate upvotes by day
        analytics = votes.annotate(
            date=TruncDay('created_at', output_field=DateField())
        ).values('date').annotate(
            up_votes=Count('id')
        ).order_by('date')

        return Response(analytics)


class UserActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user

        # ensure that the UserProfile exists for the user
        profile, created = UserProfile.objects.get_or_create(owner=user)

        data = {
            'last_login': user.last_login,
            'last_request': profile.last_request
        }
        return Response(data)
