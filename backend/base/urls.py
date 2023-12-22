from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("protected/", views.protected_view, name="protected_view"),
    path("api/events/", views.get_events, name="get-events"),
    path("api/custom_support_links/", views.get_support_links_view, name="custom_support_links"),
    path("api/scraped-data/", views.get_scraped_data, name="get-scraped-data"),
    path("api/register/", views.register, name="register"),
    path("api/login/", views.login, name="login"),
    path('api/verify-user-details/', views.verify_user_details, name='verify_user_details'),
    path('api/reset-password/', views.reset_password, name='reset_password'),
    path("api/mood-choices/", views.get_mood_choices, name="mood-choices"),
    path("api/get-mood-causes/", views.get_mood_causes, name="get-mood-causes"),
    path("api/moods/", views.post_mood, name="post-mood"),
    path("api/user-moods/<str:user_id>/", views.get_user_moods, name="get_user_moods"),
    path('api/moods/<str:mood_id>/update/', views.update_mood, name='update_mood'),
    path('api/moods/<str:mood_id>/delete/', views.delete_mood, name='delete_mood'),
    path("api/get-csrf-token/", views.get_csrf_token, name="get-csrf-token"),
    path('api/friends/', views.get_friends_list_view, name='friends_list'),
    path('api/send-friend-request/<str:username>/', views.send_friend_request, name='send_friend_request'),
    path('api/accept-friend-request/<str:username>/', views.accept_friend_request, name='accept_friend_request'),
    path('api/reject-friend-request/<str:username>/', views.reject_friend_request, name='reject_friend_request'),
    path('api/remove-friend/<str:username>/', views.remove_friend, name='remove_friend'),
    path('api/friend-requests/', views.get_friend_requests, name='get_friend_requests'),
    path('api/mood-statistics/', views.mood_statistics, name='mood-statistics'),
    path('api/save-broadcast-message/', views.save_broadcast_message, name='save_broadcast_message'),
    path('api/get-latest-broadcast-message/', views.get_latest_broadcast_message, name='get_latest_broadcast_message'),
    path('api/users/', views.get_users, name='get_users'),
    path('api/check-staff-status/', views.check_staff_status, name='check_staff_status'),
    path('api/user/profile/', views.update_user_profile, name='update_user_profile'),
    path('api/user/<str:username>/get-profile/', views.get_user_profile, name='get_user_profile'),
    path('api/user/update-preferences', views.update_show_mood_preference, name='update_show_mood_preference'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

