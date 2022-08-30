from rest_framework import serializers
from ...models.actor import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'gender']
