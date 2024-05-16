from django.contrib.auth.models import User
from .models import Book, Author, Review, BookBuddy
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

"""Serializers the models"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'author', 'series_num', 'genre', 'summary', 'publisher', 'published_date',
                  'page_total', 'title')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('birth_date', 'death_date', 'photo', 'name', 'auth_id')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('pk', 'book', 'user', 'title', 'text', 'rating',
                  'created_date', 'edited_date')

class BookBuddySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBuddy
        fields = ('pk', 'book', 'user', 'fav_status', 'read_status', 'read_later_status',
                  'currently_reading', 'current_page', 'last_read')


"""Serializes logging in and registering the user"""
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True, 'min_length': 6},
            'password2': {'write_only': True, 'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'first_name', 'last_name', 'email')