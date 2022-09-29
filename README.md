# Starwar API
A GraphQL API wrap around https://swapi.dev/ hosted at https://morning-castle-64844.herokuapp.com/
# Available Query And Mutation as shown below
```
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

