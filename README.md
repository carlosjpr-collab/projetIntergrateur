# projetIntergrateur
- Install docker compose
- Create directory and put inside it the DistributedMinioDockerCompose.yaml file.
- Excute docker-compose pull
- Excute docker-compose up 
- You can access http://127.0.0.1:X/ where X represents the number of port or use can use the address showed after executing docker-compose up.
- To connect to minio and uplade a file inside it using python, excute 
   -  pip3 install minio
   -  Download minioPythonUploadFile.py
   -  Change the Configuration inside it like file name and minio ip adress
   -  excute python3.6 minioPythonUploadFile.py

- install spark  https://www.roseindia.net/spark/install-spark-on-ubuntu-18.04.shtml
