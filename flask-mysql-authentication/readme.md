# FLASK MYSQL AUTHENTICATION 

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

