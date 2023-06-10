from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Profile, RapidProfile

from django.shortcuts import render, redirect
from .models import Profile, RapidProfile

from django.views.generic import View
from allauth.socialaccount.providers.google import GoogleAccount
from rest_framework.authtoken.models import Token


class GoogleOauth2View(View):

    def get(self, request):
        # Get the social account for the current user
        social_account = GoogleAccount.objects.get(user=request.user)

        # Get the access token from the social account
        token = social_account.access_token

        # Create a token object
        token_obj = Token()
        token_obj.user = request.user
        token_obj.token = token
        token_obj.save()

        # Return the token
        return Response({'token': token})


def specify_username_rapid_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        player_name = request.POST.get('player_name')

        # Check if the fields are already filled
        if Profile.objects.filter(user=request.user).exists() and RapidProfile.objects.filter(
                profile__user=request.user).exists():
            return redirect('/rapid/planets/')  # Redirect to /rapid/planets/ if fields are already filled

        # Create or update the profile and rapid profile
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile.user_name = username
        profile.save()

        rapid_profile, _ = RapidProfile.objects.get_or_create(profile=profile)
        rapid_profile.player_name = player_name
        rapid_profile.save()

        # Return a JSON response with the username and player name
        return JsonResponse({'username': username, 'player_name': player_name})
