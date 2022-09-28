import pytest
from api.models import Planet
from graphene.test import Client
from api.schema import  schema

client = Client(schema)


@pytest.mark.django_db
def test_resolve_all_planets():
  Planet.objects.create(
    name="Moon",
    rotation_period="360 days",
    orbital_period=361,
    diameter=5999,
    climate="Cold",
    gravity=1000,
    terrain="Testing",
    surface_water="Testing",
    population=10000000
  )
  query = '''
    query {
      name
    }
  '''


  result = client.execute(query)
  assert result == {
    "data":{
      "allPlanets": {
        "name":"Moon"
      }
    }
  }

  assert 'errors' not in result

