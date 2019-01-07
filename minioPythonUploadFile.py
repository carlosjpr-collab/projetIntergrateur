# coding=utf-8
from minio import Minio
from minio.error import ResponseError
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
minioClient = Minio('172.19.0.3:9000',
                  access_key='minio',
                  secret_key='minio123',
                  secure=False)
try:
       minioClient.make_bucket("images", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise
else:
        # Put an object 'test_RGB_0_10_25.npy' with contents from 'test_RGB_0_10_25.npy'.
        try:
               minioClient.fput_object('images', 'test_RGB_0_10_25.npy', '/home/hamid/Téléchargements/INSA_data_images/test_RGB_0_10_25.npy')
        except ResponseError as err:
               print(err)
