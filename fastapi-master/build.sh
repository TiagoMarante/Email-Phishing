docker stop fast-api
docker rmi -f fast-api

docker build -t fast-api:latest .
docker run -d --name fast-api -p 8000:8000 fast-api
