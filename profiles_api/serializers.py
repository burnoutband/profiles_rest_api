from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""


    name = serializers.CharField(max_length=10)
    # nid = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""


    # meta class 는 모델에서 무슨 field를 뽑아 사용할지를 DRF에게 말해주는 것.
    # password 필드는 no read, no see!! 시리얼라이저로 단지 write만 가능.
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    # Override create function
    # why overriding? to encrypt password with hash.
    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        # save() 은 user 오브젝트를 DB에 저장.
        user.save()

        return user



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed item."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}} # login 한 유저만 자기 프로파일 편집가능하다.
