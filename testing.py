import subprocess
import re
import os
PATH =r'/home/chandrahas/CS/Computer E-Books A-Z'
currentpath=PATH
comprehensive_list=[]

'''pathing=  "/fa/dg/gfd/ddsfd.chm"
pathx= re.search(r'(\S+).chm',pathing)
actualpathx= pathx.group(1)+'.pdf'
print(actualpathx)
print(pathx.group(1))
'''

'''list = os.listdir(currentpath)
for a in range(len(list)):
    list[a]= currentpath + list[a]
print(list)
'''

'''for dir_name, subdirlist, filelist in os.walk(PATH):
        for f in filelist:
            print(dir_name)
            print(f)
'''

for dir_name, subdirlist, filelist in os.walk(PATH):
    for f in filelist:

        comprehensive_list.append(dir_name+'/'+fx)

print(comprehensive_list)