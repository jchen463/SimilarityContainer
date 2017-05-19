#!/usr/bin/python
import csv, os
import string
import random
string.ascii_lowercase

#point to a relative path
#os.chdir(os.path.relpath('Stims', start='.')+'//')

def searchList( object, myList ):
    for index in range(len(myList)):
        if object == myList[index]['STIMULUS NAME']:
            return index;

    return -1;

'''might need to put a full path before file name'''
files=csv.DictReader(open(os.getcwd()+'/Stims_Similarities.csv','r+'))
files=list(files)

for i in files:
    i['SIMILAR IN COLOR'] = i['SIMILAR IN COLOR'].replace(" ", "")
    i['SIMILAR IN COLOR'] = i['SIMILAR IN COLOR'].split(',')
    i['SIMILAR IN SHAPE'] = i['SIMILAR IN SHAPE'].replace(" ", "")
    i['SIMILAR IN SHAPE'] = i['SIMILAR IN SHAPE'].split(',')
    i['SIMILAR IN COLOR'] = set(i['SIMILAR IN COLOR'])
    i['SIMILAR IN SHAPE'] = set(i['SIMILAR IN SHAPE'])
    
stims = [file['STIMULUS NAME'] for file in files] # format dictionary => all stim names in one list called [stims], shuffle
finalStims = [] # initialize list for finalStims

#keep adding items until you get a list of 4, if you have deleted all items from stim, reset
while(len(finalStims) != 4):
    #shuffle files and add item from the first index
    random.shuffle(stims)
    finalStims.append(stims[0])
    tempIndex = searchList(stims[0],files);


    #removes simlarities between the two and the item
    stims = set(stims).symmetric_difference(set(files[tempIndex]['SIMILAR IN COLOR']))
    stims = set(stims).symmetric_difference(set(files[tempIndex]['SIMILAR IN SHAPE']))
    if files[tempIndex]['STIMULUS NAME'] in stims:
        stims.remove(files[tempIndex]['STIMULUS NAME'])
    stims = list(stims) # turn it back into a list

    if len(stims) == 0:
        finalStims = []
        stims = [file['STIMULUS NAME'] for file in files]

print finalStims

## for number of elements in [finalStims] < 4, do
#for i in xrange(1,4):
##    shuffle [stims]
#     random.shuffle(stims)
##    place stim name in [finalStims]    
#    finalStims.append(files[0]['STIMULUS NAME'])
##remove the simimlaries of that item form stims    
#    stims = set(stims).symmetric_difference(set(files[0]['SIMILAR IN COLOR']))
#    stims = set(stims).symmetric_difference(set(files[0]['SIMILAR IN SHAPE']))
#    stims.remove(files[0]['STIMULUS NAME'])#    compare strings under [SIMILAR IN COLOR] and [SIMILAR IN SHAPE] with [stims]
##       if matches, then
##          remove from [stims]
## remove from dictionary


# return [final stims], which should now be a list of 4 dissimilar fractals
#print finalStims; 


#--------------------------------------------------------------------------------


#letters
#letters=list(string.ascii_lowercase)


#for i in files[0:5]:
#    #update our dicts to have neighbor entry
#    i.update({'MatchingLetter':[]})
    
#    if files.index(i)==0:
#        i['MatchingLetter']=letters[0]
#    else:
        #look through all the files
#        for l in files:
#            if l['STIMULUS NAME'] in i['SIMILAR IN COLOR'] or l['STIMULUS NAME'] in i['SIMILAR IN SHAPE']:
#                i['MatchingLetter'].append(l['STIMULUS NAME'])