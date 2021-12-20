from django.urls import path



from . import views



urlpatterns = [
    path('hello', views.hello_endpoint, name='hello_endpoint'),
    path('version', views.version_endpoint, name='version_endpoint'),
    path('events/create', views.list_create_event_api_endpoint, name="list_create_event_api_endpoint"),
    path('events', views.list_create_event_api_endpoint, name="list_create_event_api_endpoint"),
    path('login', views.login_endpoint, name="login_endpoint"),
    path('register', views.register_endpoint, name="register_endpoint"),
    path('event/<id>', views.retrieve_update_delete_event_endpoint, name="retrieve_update_delete_event_endpoint"),
]
