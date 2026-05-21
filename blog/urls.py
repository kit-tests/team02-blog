from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name ="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/new/", views.post_create, name="post-create-page"),
    path("posts/<slug:slug>", views.post_details, name="post-details-page"), #/posts/my-first-post
    path("posts/<slug:slug>/edit/", views.post_edit, name="post-edit-page"),
    path("posts/<slug:slug>/delete/", views.post_delete, name="post-delete-page"),
    path("chat/api/global/messages/", views.global_chat_messages, name="global-chat-messages"),
    path("chat/api/post/<slug:slug>/messages/", views.post_chat_messages, name="post-chat-messages"),
    path("restricted/", views.restricted, name="restricted"),
    path("about/", views.about, name="about-page"),
    path("about/edit/", views.about_edit, name="about_edit"),
    path("logout/", views.custom_logout, name="logout"),
    path("api/calendar/", views.calendar_data_json, name="calendar-data-json"),
    path("api/calendar-grid/", views.calendar_grid_html, name="calendar-grid-html"),
]
