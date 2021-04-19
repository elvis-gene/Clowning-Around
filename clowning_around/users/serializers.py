from rest_framework import serializers
from clowning_around.users.models import Client, Clown, TroupeLeader


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clown
        fields = '__all__'
        depth = 1


# Not needed so far
class TroupeLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TroupeLeader
        fields = '__all__'
        depth = 1
