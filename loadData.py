from minio import Minio
from minio.error import ResponseError
from elasticsearch import Elasticsearch
from tempfile import NamedTemporaryFile
import numpy as np

array_test_images = np.load('test_RGB_0_10_25.npy')
array_test_labels = np.load('test_labels_0_10_25.npy')

minioClient = Minio('172.17.0.2:9000', access_key='EJEMO14TO3F0SXYK3ZCQ', secret_key='8TttYU3freg4Yv0D49UqNThjU+KOf4i3CvsU6563', secure = False)

es = Elasticsearch('172.17.0.3',port=9200)

if not minioClient.bucket_exists('images'):
  try:
    minioClient.make_bucket('images',location='us-east-1')
  except ResponseError as err:
    print(err)

print(array_test_images[0])

def returnLabel(label):
  if(label[0] == 1):
    return 'urban area'
  elif(label[1] == 1):
    return 'agricultural territory'
  elif(label[2] == 1):
    return 'forests'
  elif(label[3] == 1):
    return 'wetlands'
  elif(label[4] == 1):
    return 'surfaces with water'

for i in range(5):
  tempfile = NamedTemporaryFile()
  np.save(tempfile, array_test_images[i])
  tempfile.seek(0)
  name = 'img' + str(i)
  minioClient.fput_object('images', name, tempfile.name)
  url = '172.17.0.2/images/' + str(name)
  label = returnLabel(array_test_labels[i])
  jsonBody = { 'url' : url, 'label' : label}
  res = es.index(index='images_index',doc_type='image', id=name, body=jsonBody)
  print(res['result']) 
  
