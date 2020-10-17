from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("<int:id>/", views.show_listing, name="show_listing"),
    path("add_to_watchlist/<int:id>/", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<int:id>/", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("watchlist", views.show_watchlist, name="show_watchlist"),
    path("close_auction/<int:id>/", views.close_auction, name="close_auction")
]
