from django.urls import path

from api import views

urlpatterns = [
    path("levels/", views.LevelsListView.as_view(), name="levels_list_view" ),
    path("levels/<id>", views.LevelsItemView.as_view(), name="levels_item_view"),


]

