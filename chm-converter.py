#Program accepts a filesystem finds all chm files and converts them to pdf.
import subprocess
import re
import os
PATH=r'/home/chandrahas/CS/Computer E-Books A-Z'            #Absolute path
comprehensive_list=[]                                       #final list of all paths to all files
chm_list=[]                                                 #final list to only chm files

#Converts chm file to pdf given a list,(file_path is path of chm file) and deletes the file
def converter(list):
    for file_path in list:
        pathx = re.search(r'(\S+).chm', file_path)
        actualpathx = pathx.group(1) + '.pdf'
        subprocess.call(['chm2pdf', file_path, actualpathx])
        os.remove(file_path)

for dir_name, subdirlist, filelist in os.walk(PATH):
    for f in filelist:
        fx=re.sub(r'\s','\ ',f)
        dir_namex = re.sub(r'\s', '\ ', dir_name)
        comprehensive_list.append(dir_namex+'/'+fx)

for x in comprehensive_list:
    m= re.search('\S*.chm',x)
    if m:
        chm_list.append(x)




print(comprehensive_list)
print(chm_list)
#converter(chm_list)
