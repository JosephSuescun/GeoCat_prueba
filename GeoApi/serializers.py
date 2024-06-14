from rest_framework import serializers
from .models import Municipality, Entity, Dependency, Producer

class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }
            
    def validate_name_municipality(self, value):
        if Municipality.objects.filter(name_municipality=value).exists():
            raise serializers.ValidationError("A municipality with this name already exists.")
        return value
    
class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }

    def validate_name_entity(self, value):
        if Entity.objects.filter(name_entity=value).exists():
            raise serializers.ValidationError("An entity with this name already exists.")
        return value

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
        }

    def validate_name_dependency(self, value):
        if Dependency.objects.filter(name_dependency=value).exists():
            raise serializers.ValidationError("A dependency with this name already exists.")
        return value

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'required': False}
            
        }

"""    def validate_email_producer(self, value):
        if Producer.objects.filter(email=value).exists():
            raise serializers.ValidationError("A dependency with this name already exists.")
        return value
"""