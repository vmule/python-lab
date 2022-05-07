import os
import re

my_dir = '/Users/vmule/Python-Lab'

for root, dirs, files in os.walk(my_dir):
#    print(root, dirs, files)
    for i in files:
        if re.match(r'.*\.htm$', i):
        #if i.endswith('.htm'):
            print(i)
            old_path = os.path.join(root, i)
            new_path = os.path.join(root, (i.split(".")[0] + ".html"))
            os.rename(old_path, new_path)
            print(new_path)

