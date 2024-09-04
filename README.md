
### build image
```
docker build -t dev-user-api:v1.0.0 .
```

### docker run
```
docker run --name dev-user-api -p 8000:80 -d dev-user-api:v1.0.0 
```

