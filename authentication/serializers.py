from rest_framework import serializers
from authentication.models import Profile, RapidProfile, ClassicalProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class RapidProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapidProfile
        fields = '__all__'


class ClassicalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassicalProfile
        fields = '__all__'
