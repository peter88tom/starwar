# Starwar API
A GraphQL API wrap around https://swapi.dev/ hosted at https://morning-castle-64844.herokuapp.com/

Tech stack used for this API is Python, Django, GraphQL and Django-graphene

You can clone this repo and run in your local machine and install the project requirement listed on project requirements.txt with `` pip install -r requirements.txt``

Once you install the project requirements, configure your environment variables. Create ``.env`` file inside admin folder with the following variables
```bazaar
SECRET_KEY=your_app_key
DATABASE_NAME=your_database_name
DATABASE_PASSWORD=your_database_password
DATABASE_USERNAME=your_database_username
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Once you configure your environment variable make migrations while your virtualenvironment is activated using the following command ``` python manage.py migrate``` this will create the project database schemas

Once the tables are created you can now load sample data from the ``` fixtures directory``` startign with platenet sample data  and following with people sample data. Use this commands:
```
python manage.py loaddata api/fixture/planets.json
```

```
python manage.py loaddata api/fixture/people.json
```


# Available Query And Mutation as shown below
```bazaar
# 1. CREATE A NEW USER
mutation {
  createUser(username: "john.doe", password:"12345", email:"john.doe@gmail.com") {
    user {
      id
      username
      email
    }
  }
}




# 2. QUERY TO GET ALL USERS
Query to get all users
query{
  allUser{
    username
    password
  }
}


# 3. MUTATION TO GET JWT TOKEN
mutation{
  tokenAuth(username:"user_name_created_above",password:"password_created_above"){
    token
  }
}




# 4. QUERY ALL PEOPLE
query{
  allPeople{
    name
    height
    mass
		gender
    homeworld {
      id,
      name
    }
  }
}



#5. QUERY TO SEARCH BY NAME
query{
  allPeople(search:"Tion"){
    name
    height
    mass
		gender
    homeworld {
      id,
      name
    }
  }
}


# 6 QUERY TO FILTER AND PAGINATE
query{
  allPeople(first: 5, skip: 1){
    name
    height
    mass
		gender
    homeworld {
      id,
      name
    }
  }
}


```

