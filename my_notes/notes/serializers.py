from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    notes = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Note.objects.none())

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'notes']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'label',
        )


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'content',
            'tags',
            'owner',
            'created_at',
        )
