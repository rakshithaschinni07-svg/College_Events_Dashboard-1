from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),

    path(
        'register/<int:event_id>/',
        views.register_event,
        name='register_event'
    ),

    path(
        'registration-success/',
        views.registration_success,
        name='registration_success'
    ),

    path(
        'detail/<int:event_id>/',
        views.event_detail,
        name='event_detail'
    ),

    path(
        'participants/',
        views.participants,
        name='participants'
    ),

    path(
        'analytics/',
        views.analytics,
        name='analytics'
    ),

    path(
        'notifications/',
        views.notifications,
        name='notifications'
    ),

    path(
        'settings/',
        views.settings,
        name='settings'
    ),

    path(
        'admin-profile/',
        views.admin_profile,
        name='admin_profile'
    ),
]