# FLASK MONGO CRUD 

## PRE REQUISITE


in linux
```bash
docker volume rm mongo_crud 
mkdir -p $HOME/mongo/crud
docker volume create --driver local --opt type=none --opt device=$HOME/mongo/crud --opt o=bind mongo_crud
```


in mac
```bash
docker volume rm mongo_crud 
mkdir -p ~/database/mongo 
docker volume create --driver local --opt type=none --opt device=/Users/$USER/database/mongo --opt o=bind mongo_crud
```

also to be accurate you can do this to your docker-compose
```yaml
volumes:
  mongo_crud:
    external: true
    driver: local
    driver_opts:
        type: none
        o: bind
        device: /Users/<your username>/database/mongo

```