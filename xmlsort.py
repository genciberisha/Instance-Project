#!/usr/bin/python3


import xml.etree.ElementTree as ET

fname_key = {
        'instancat/UP-FCEA-DA-AS2017.xml':'05',
        'instancat/UP-FME-AS2017.xml':'06',
        'instancat/UP-FECE-AS2018.xml':'07'}   # instancat\\UP-FCEA... për përdoruesit e Windows-it.


count = 0




## Funksioni që bën ndryshimin e atributeve të etiketave.
def sort_tag(tag,attr,code):
    for i in root.iter(tag):
        if(attr in i.attrib):
            temp = i.get(attr)
            i.set(attr,temp[0] + code + temp[1:])
###########################################################

## Funksioni që kopjon etiketat e ndryshuara dhe i vendos në objektin(element tree) e fajllit final(output.xml).

def write_tag(tag):                                 # Ka vetëm një atribut për arsye se burimi dhe destinacioni është i njejtë.
    for i in root.findall('./'+tag+'/'):            # 'root' është rrënja e fajllit perkatës që në rastin tonë është etiketa 'instance'.
        root1.find(tag).append(i)                   # 'root1' është rrënja e fajllit final.
###########################################################


for fname in fname_key:
    tree = ET.parse(fname)
    root = tree.getroot()
    sort_tag('course','id',fname_key[fname])
    sort_tag('course','ref',fname_key[fname])
    sort_tag('course','teacher',fname_key[fname])
    sort_tag('room','id',fname_key[fname])
    sort_tag('room','ref',fname_key[fname])
    sort_tag('curriculum','id',fname_key[fname])
    sort_tag('constraint','course',fname_key[fname])
    if(count == 0):                         # Objekti i fajllit të parë kopjohet në objektin 'tree1' të fajllit final(output.xml) në mënyrë që ta kemi strukturen e fajllit
        tree1 = tree                        # final te gatshme.
        root1 = tree1.getroot()             # 'count == 0' është përdorur variabla count për të numëruar në 'dictionary(map,hash)'
        count = 1                           #  për arsye se në 'dictionary' nuk kemi mundësi të indeksojmë.
    else:
        write_tag('courses')
        write_tag('rooms')
        write_tag('curricula')
        write_tag('constraints')




tree1.write('output.xml') # Bën "uparse" objektin 'tree1' dhe "write" në fajllin 'output.xml'

