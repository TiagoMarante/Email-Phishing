clear 
docker build -t gecad_ml:0.1 . 
docker run -p 8000:8000 --name my_api gecad_ml:0.1