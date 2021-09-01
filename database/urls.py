from django.urls import path
from .views import *

urlpatterns = [
    path('players/', PlayersList.as_view()),
    path('managers/', ManagersList.as_view()),
    path('coaches/', CoachesList.as_view()),
    path('staff/', StaffList.as_view()),
    path('fanclub-countries/', CountryList.as_view()),
    path('fanclub-photos/', media_albums('fanclub').as_view()),
    path('sponsors-general/', sponsors_and_social_media('general').as_view()),
    path('sponsors-regular/', sponsors_and_social_media('regular').as_view()),
    path('sponsors-MHL2019/', sponsors_and_social_media('MHL2019').as_view()),
    path('social-media/', sponsors_and_social_media('social-media').as_view()),
    path('contacts/', ContactsList.as_view()),
    path('seasons/', SeasonsList.as_view()),
    path('rules/', RulesList.as_view()),
]
