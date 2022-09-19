import graphene
from graphene_django import DjangoObjectType, DjangoListField
from django.contrib.auth import get_user_model


"""
User Type
"""
class UserType(DjangoObjectType):
  class Meta:
    model = get_user_model()
    fields = ('id','username', 'password')


"""
The Query class defines the GraphQL queries that the API will provide to the clients.
"""
class Query(graphene.ObjectType):
  all_user = graphene.List(UserType)
  user = graphene.Field(UserType,user_id=graphene.Int())


  # Query django model to return all users
  def resolve_all_user(self, info, **kwargs):
    return get_user_model().objects.all()


# Register query to graphQL
schema = graphene.Schema(query=Query)

