from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # para campos especificos: ['name','last_name'...]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    email = serializers.EmailField(max_length = 255)

    #Validaciones personalizadas
    def validate_name(self,value):
        if 'develop' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        return value
    
    def validate_email(self,value):
        if self.validate_name(self.context['name'])  in value:
            raise serializers.ValidationError('El email no puede contener el nombre')
        return value
    
    def validate(self,data):
        if data['name'] in data['email']:
            raise serializers.ValidationError('El email no puede contener el nombre')
        return data
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
        #Se debe retornar un objeto
        #El unico creado hasta ahora es User