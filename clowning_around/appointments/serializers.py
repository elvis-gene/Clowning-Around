from emoji.models import Emoji
from rest_framework import serializers
from clowning_around.appointments.models import Appointment, Issue, Rating, ClientContactRequest


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        depth = 1


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        depth = 2


class RatingSerializer(serializers.ModelSerializer):
    emoji_url = serializers.SerializerMethodField('get_emoji_url')

    class Meta:
        model = Rating
        fields = ['emoji_name', 'emoji_url', 'appointment']
        depth = 2

    def get_emoji_url(self, emoji_name: Rating):
        emojis = Emoji()
        url = emojis[emoji_name.emoji_name]
        return url


class ClientContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContactRequest
        fields = '__all__'
