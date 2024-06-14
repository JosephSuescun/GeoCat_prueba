from django.urls import path
from .views import (
    MunicipalityListView, get_municipality_by_name, MunicipalityUpdateView, MunicipalityDeleteView,
    EntityListView, get_entity_by_name, EntityUpdateView, EntityDeleteView,
    DependencyListView, get_dependency_by_name, DependencyUpdateView, DependencyDeleteView,
    ProducerListView, get_producer_by_name, ProducerUpdateView, ProducerDeleteView, 
    ProducerListByDependencyView, ProducerListByEntityView, DependencyListByEntityView, EntityListByMunicipalityView
)

urlpatterns = [

    #Municipios
    path('municipalities/', MunicipalityListView.as_view(), name='municipality-list'),
    path('municipalities/<str:name>/', get_municipality_by_name, name='municipality-detail'),
    path('municipalities/update/<int:id>/', MunicipalityUpdateView.as_view(), name='municipality-update'),
    path('municipalities/delete/<int:id>/', MunicipalityDeleteView.as_view(), name='municipality-delete'),

    # Entidades
    path('entities/', EntityListView.as_view(), name='entity-list'),
    path('entities/<str:name>/', get_entity_by_name, name='entity-detail'),
    path('entities/update/<int:id>/', EntityUpdateView.as_view(), name='entity-update'),
    path('entities/delete/<int:id>/', EntityDeleteView.as_view(), name='entity-delete'),

    # Dependencias
    path('dependencies/', DependencyListView.as_view(), name='dependency-list'),
    path('dependencies/<str:name>/', get_dependency_by_name, name='dependency-detail'),
    path('dependencies/update/<int:id>/', DependencyUpdateView.as_view(), name='dependency-update'),
    path('dependencies/delete/<int:id>/', DependencyDeleteView.as_view(), name='dependency-delete'),

    # Productores
    path('producers/', ProducerListView.as_view(), name='producer-list'),
    path('producers/<str:name>/', get_producer_by_name, name='producer-detail'),
    path('producers/update/<int:id>/', ProducerUpdateView.as_view(), name='producer-update'),
    path('producers/delete/<int:id>/', ProducerDeleteView.as_view(), name='producer-delete'),

     # Otros endpoints 
    path('producers/by-dependency/<int:dependency_id>/', ProducerListByDependencyView.as_view(), name='producer-list-by-dependency'),
    path('producers/by-entity/<int:entity_id>/', ProducerListByEntityView.as_view(), name='producer-list-by-entity'),
    path('dependencies/by-entity/<int:entity_id>/', DependencyListByEntityView.as_view(), name='dependency-list-by-entity'),
    path('entities/by-municipality/<int:municipality_id>/', EntityListByMunicipalityView.as_view(), name='entity-list-by-municipality'),
]
