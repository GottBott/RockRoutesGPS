import os
import sys
import re
rootdir = '/mtn_proj/www.mountainproject.com'
outputDir = '/output'
name =''
location=''
description=''
num=0


if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for root, subFolders, fileList in os.walk(rootdir):
    for filename in fileList:
        try:
            f = open(root +'/' + filename, 'r',encoding = "ISO-8859-1")
            fname = root +'/' + filename
            #for line in f.readline():
            stri = f.read()
            
            result = re.search(r'<em>.*&nbsp;<span', stri, flags=0)
            if result:
                name = result.group()
                name = name.replace("<em>", "")
                name = name.replace("&nbsp;<span", "")
                #print name
                #output.write(name +',')

    
            result = re.search(r'\d\d\.\d*,\s.\d\d\.\d*', stri, flags=0)
            if result:
                location = result.group()
                #print location
                #output.write(location+',')
                location = location.replace(",", "")
                location =location.split(' ')
                
                
            result = re.search(r'Description&nbsp;</h3><div><!--MPTEXT-->.*', stri, flags=0)
            if result:
                description = result.group()
                description = re.sub(r'<.*?>', '', description)
                description = description.replace("Description&nbsp;", "")
                description = description.replace("Getting There&nbsp;", " GETTING THERE: ")
                description = description.replace("&", "and")
                #print description
                #output.write('"'+description+'"'+'\n')

            if name != '' and location != '' and description !='':
                filename = outputDir+str(num)+".gpx"
                output = open(filename, 'w')
                #output.write('"'+name +'"'+','+location[0]+','+'"'+description+'"' +'\n')
                output.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'+"\n"+'<gpx version="1.1" creator="Ben Gotthold"'+"\n"+'xmlns="http://www.topografix.com/GPX/1/1"'+"\n"+'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'+"\n"+'xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">'+"\n"+'<wpt lat="'+location[0]+'" lon="'+location[1]+'"><name>'+name+'</name><desc>'+description+'</desc><sym>Waypoint</sym></wpt>'+"\n"+'</gpx>')
                output.close()
                num +=1
            else:
                if fname != '.DS_Store':
                    os.remove(fname)
                            

            name =''
            location=''
            description=''
            f.close()
            
        except IOError as e:
            print (e)
   
print ("created " , num , " files")
    
    
