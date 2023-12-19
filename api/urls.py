from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import BlacklistTokenUpdateView, AnalyticsAPIView, UserActivityView
from votes.views import VoteViewSet
from posts.views import PostViewSet
from users.views import UserViewSet
from user_profile.views import ProfileViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name="blacklist"),
    path('analytics/', AnalyticsAPIView.as_view(), name='analytics'),
    path('user-activity/', UserActivityView.as_view(), name='user-activity'),
]

router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = urlpatterns+router.urls
