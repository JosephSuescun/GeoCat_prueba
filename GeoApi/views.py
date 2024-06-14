from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Municipality, Entity, Dependency, Producer
from .serializers import MunicipalitySerializer, EntitySerializer, DependencySerializer, ProducerSerializer

#MUNICIPIOS 

# Clase para crear un municipio(POST) y listar todos los municipios(GET)
class MunicipalityListView(generics.ListCreateAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer

# Listar datos de un municipio por su nombre
@api_view(['GET'])
def get_municipality_by_name(request, name):
    try:
        municipality = Municipality.objects.get(name_municipality=name)
        serializer = MunicipalitySerializer(municipality)
        return Response(serializer.data)
    except Municipality.DoesNotExist:
        return Response(status=404)

# Actualizar un municipio por su id
class MunicipalityUpdateView(generics.UpdateAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    lookup_field = 'id'

# Borrar municipio por id
class MunicipalityDeleteView(generics.DestroyAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    lookup_field = 'id'


#ENTIDADES

# Clase para crear una entidad (POST) y listar todas las entidades (GET)
class EntityListView(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

# Listar datos de una entidad por su nombre
@api_view(['GET'])
def get_entity_by_name(request, name):
    try:
        entity = Entity.objects.get(name_entity=name)
        serializer = EntitySerializer(entity)
        return Response(serializer.data)
    except Entity.DoesNotExist:
        return Response(status=404)

# Actualizar una entidad por su id
class EntityUpdateView(generics.UpdateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    lookup_field = 'id'

# Borrar entidad por id
class EntityDeleteView(generics.DestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    lookup_field = 'id'


#DEPENDECIA

# Clase para crear y listar dependencias (Dependency)
class DependencyListView(generics.ListCreateAPIView):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer

# Listar datos de una dependencia por su nombre
@api_view(['GET'])
def get_dependency_by_name(request, name):
    try:
        dependency = Dependency.objects.get(name_dependency=name)
        serializer = DependencySerializer(dependency)
        return Response(serializer.data)
    except Dependency.DoesNotExist:
        return Response(status=404)

# Actualizar una dependencia por su id
class DependencyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer
    lookup_field = 'id'

# Borrar dependencia por id
class DependencyDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer
    lookup_field = 'id'



#PRODUCTORES

# Clase para crear y listar productores (Producer)
class ProducerListView(generics.ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

# Listar datos de un productor por su nombre
@api_view(['GET'])
def get_producer_by_name(request, name):
    try:
        producer = Producer.objects.get(name=name)
        serializer = ProducerSerializer(producer)
        return Response(serializer.data)
    except Producer.DoesNotExist:
        return Response(status=404)

# Actualizar un productor por su id
class ProducerUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    lookup_field = 'id'

# Borrar productor por id
class ProducerDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    lookup_field = 'id'

# Listar productores por ID de dependencia
class ProducerListByDependencyView(generics.ListAPIView):
    serializer_class = ProducerSerializer

    def get_queryset(self):
        dependency_id = self.kwargs['dependency_id']
        return Producer.objects.filter(dependency_id=dependency_id)

# Listar productores por ID de entidad
class ProducerListByEntityView(generics.ListAPIView):
    serializer_class = ProducerSerializer

    def get_queryset(self):
        entity_id = self.kwargs['entity_id']
        return Producer.objects.filter(entity_id=entity_id)

# Listar dependencias por entidad
class DependencyListByEntityView(generics.ListAPIView):
    serializer_class = DependencySerializer

    def get_queryset(self):
        entity_id = self.kwargs['entity_id']
        return Dependency.objects.filter(entity_id=entity_id)

# Listar entidades por municipio
class EntityListByMunicipalityView(generics.ListAPIView):
    serializer_class = EntitySerializer

    def get_queryset(self):
        municipality_id = self.kwargs['municipality_id']
        return Entity.objects.filter(municipality_id=municipality_id)
