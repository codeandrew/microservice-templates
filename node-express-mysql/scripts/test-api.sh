#!/bin/bash

# API endpoint
API_ENDPOINT="http://localhost:3000"

echo "Testing Node.js API with MySQL"

# Testing POST (Create User)
echo "Creating a new user..."
curl -X POST "$API_ENDPOINT/users" -H "Content-Type: application/json" -d '{"username":"john_doe","password":"password123","name":"John Doe","age":30,"email":"johndoe@example.com"}'
echo -e "\n"

# Testing GET (Get All Users)
echo "Fetching all users..."
curl -X GET "$API_ENDPOINT/users"
echo -e "\n"

# Replace with a valid user ID for further tests
USER_ID=1

# Testing GET (Get Specific User)
echo "Fetching user with ID $USER_ID..."
curl -X GET "$API_ENDPOINT/users/$USER_ID"
echo -e "\n"

# Testing PUT (Update User)
echo "Updating user with ID $USER_ID..."
curl -X PUT "$API_ENDPOINT/users/$USER_ID" -H "Content-Type: application/json" -d '{"username":"john_doe_updated","password":"newpassword123","name":"John Updated","age":31,"email":"johnupdated@example.com"}'
echo -e "\n"

# Testing DELETE (Delete User)
echo "Deleting user with ID $USER_ID..."
curl -X DELETE "$API_ENDPOINT/users/$USER_ID"
echo -e "\n"
