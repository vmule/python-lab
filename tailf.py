import time
import os

file = open('/home/vmule/file')

st_results = os.stat('/home/vmule/file')
st_size = st_results[6]
file.seek(st_size)

lines_num = 5
buffer = 5
position = st_size - buffer

while lines_num > 1:
  file.seek(position)
  lines = file.readlines()
  for i in lines:
    if len(i) <= 1:
      pass
    elif lines_num > 1:
      position -= len(i)
      lines_num -= 1
    else:
      break

file.seek(position)

while 1:
  where = file.tell()
  #print where
  line = file.readline()
  if line:
    print line.strip('\n')
  else:
    time.sleep(1)
    file.seek(where)


  
