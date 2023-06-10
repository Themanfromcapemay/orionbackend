from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, unique=True)
    gold_amount = models.PositiveIntegerField(default=1000)
    email_address = models.EmailField()

    def __str__(self):
        return self.user.username


class RapidProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=50, unique=True)
    games_played = models.PositiveIntegerField(default=0)
    games_won = models.PositiveIntegerField(default=0)
    games_abandoned = models.PositiveIntegerField(default=0)
    player_elo = models.PositiveIntegerField(default=1000)
    raider_medals = models.PositiveIntegerField(default=0)
    defender_medals = models.PositiveIntegerField(default=0)
    attacker_medals = models.PositiveIntegerField(default=0)
    population_medals = models.PositiveIntegerField(default=0)

    # Game specific details
    total_population = models.PositiveIntegerField(default=0)
    total_raid_points = models.PositiveIntegerField(default=0)
    total_atk_points = models.PositiveIntegerField(default=0)
    total_def_points = models.PositiveIntegerField(default=0)

    player_type = models.CharField(max_length=50)

    def __str__(self):
        return self.profile.user.username + " - Rapid"


class ClassicalProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=50)
    games_played = models.PositiveIntegerField(default=0)
    games_won = models.PositiveIntegerField(default=0)
    games_abandoned = models.PositiveIntegerField(default=0)
    player_elo = models.PositiveIntegerField(default=1000)
    raider_medals = models.PositiveIntegerField(default=0)
    defender_medals = models.PositiveIntegerField(default=0)
    attacker_medals = models.PositiveIntegerField(default=0)
    population_medals = models.PositiveIntegerField(default=0)

    # Game specific details
    total_population = models.PositiveIntegerField(default=0)
    total_raid_points = models.PositiveIntegerField(default=0)
    total_atk_points = models.PositiveIntegerField(default=0)
    total_def_points = models.PositiveIntegerField(default=0)

    player_type = models.CharField(max_length=50)

    def __str__(self):
        return self.profile.user.username + " - Classical"

