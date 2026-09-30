from django.contrib import admin
from django.urls import path

from events.views import (
    dashboard,
    events,
    add_event,
    event_list,
    event_detail,
    register_event,
    registration_success,
    participants,
    analytics,
    notifications,
    settings,
    admin_profile,
)

urlpatterns = [

    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Dashboard
    path(
        "",
        dashboard,
        name="dashboard"
    ),

    # Events
    path(
        "events/",
        events,
        name="events"
    ),

    # Add Event
    path(
        "events/add/",
        add_event,
        name="add_event"
    ),

    # Event List
    path(
        "event-list/",
        event_list,
        name="event_list"
    ),

    # Event Detail
    path(
        "events/event/<int:event_id>/",
        event_detail,
        name="event_detail"
    ),

    # Register Event
    path(
        "events/register/<int:event_id>/",
        register_event,
        name="register_event"
    ),

    # Registration Success
    path(
        "registration-success/",
        registration_success,
        name="registration_success"
    ),

    # Participants
    path(
        "participants/",
        participants,
        name="participants"
    ),

    # Analytics
    path(
        "analytics/",
        analytics,
        name="analytics"
    ),

    # Notifications
    path(
        "notifications/",
        notifications,
        name="notifications"
    ),

    # Settings
    path(
        "settings/",
        settings,
        name="settings"
    ),

    # Admin Profile
    path(
        "admin-profile/",
        admin_profile,
        name="admin_profile"
    ),
]