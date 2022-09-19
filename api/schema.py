import graphene
from graphene_django import DjangoObjectType, DjangoListField
from django.contrib.auth import get_user_model
import graphql_jwt
from api.models import People, Planet
from django.db.models import  Q


"""
User Type
"""
class UserType(DjangoObjectType):
  class Meta:
    model = get_user_model()
    fields = ('id','username', 'password')


"""
Planet Type
"""
class PlanetType(DjangoObjectType):
  class Meta:
    model = Planet
    fields = "__all__"


"""
People Type
"""
class PersonType(DjangoObjectType):
  class Meta:
    model = People
    fields = ['id','name', 'height', 'mass', 'gender', 'homeworld']

"""
The Query class defines the GraphQL queries that the API will provide to the clients.
"""
class Query(graphene.ObjectType):
  all_user = graphene.List(UserType)
  user = graphene.Field(UserType,user_id=graphene.Int())
  all_planets = graphene.List(PlanetType)
  all_people = graphene.List(PersonType)


  # Query django model to return all users
  def resolve_all_user(self, info, **kwargs):
    user_qs = get_user_model().objects.all()
    return user_qs

  # Query all planets
  def resolve_all_planets(self, info, **kwargs):
    planet_qs = Planet.objects.all()
    return planet_qs

  # Resolve all people
  def resolve_all_people(self, info, **kwargs):
    people_qs = People.objects.all()
    return people_qs


# Register mutation to graphQL
class Mutation(graphene.ObjectType):
  # jwt authentication
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()

# Register query to graphQL
schema = graphene.Schema(query=Query, mutation=Mutation)

