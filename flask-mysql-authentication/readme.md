# FLASK MYSQL AUTHENTICATION 

## GOAL 
scenario of how an API gateway can handle a user's post request for authentication and pass it on to an authentication server, and then authorize requests to a profile API using a JWT token:

- The user sends a POST request to the API gateway with a JSON payload containing the fields "username" and "password".
- The API gateway receives the request and validates the payload to make sure that it contains the required fields.
- The API gateway then forwards the request to the authentication server, which verifies the username and password against the appropriate database or service.
- The authentication server responds to the API gateway with a JSON Web Token (JWT) that contains information about the authenticated user.
- The API gateway receives the JWT and adds it to the response that it sends back to the user.
- The user receives the JWT and includes it in the "Authorization" header of subsequent requests to the API gateway.
- When the user sends a request to the profile API, the API gateway checks the incoming request for a valid JWT in the "Authorization" header.
- If the JWT is valid, the API gateway forwards the request to the profile API, along with the user's information from the JWT.
- The profile API can then use the user's information to retrieve the appropriate profile data and respond back to the API Gateway
- The API gateway then forwards the profile data back to the user.

You can use JWT libraries in python like PyJWT, or Authlib to handle the JWT tokens.
In the API Gateway you can use Flask or FastAPI to handle the incoming requests and forward them to the appropriate service, and you can use middlewares to handle the JWT validation and add the user information to the request

## SETUP
in linux
```bash
docker volume rm mysql_data 
mkdir -p $HOME/mysql/users
docker volume create --driver local --opt type=none --opt device=$HOME/mysql/users --opt o=bind mysql_data
```


in mac
```bash
docker volume rm mysql_data 
mkdir -p /Users/$USER/database/mysql_data
docker volume create --driver local --opt type=none --opt device=/Users/$USER/database/mysql_data --opt o=bind mysql_data
```

## TERMS

- Authentication/AuthN: identify who is making the request
- Authorization/AuthZ: what the user can do
