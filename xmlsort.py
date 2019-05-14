#!/usr/bin/python3


from lxml import etree


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
def write_tag(tag,method = None):                       # Atributi 'method = None' eshte per ta mbingarkuar funksionin/   
        for i in root.findall('./'+tag+'/'):            
            if method is None:
                root1.find(tag).append(i)
            else:       
                if(i.get('type') == "period"):
                    last = root1.findall('./constraints/constraint[@type = "period"]')[-1]      #Gjej elementin e fundit të listës së etiketave 'timeslot'.
                    parent = last.getparent()
                    parent.insert(parent.index(last)+1,i)                                       #Shkruaj etiketen 'timeslot' të instancë aktuale pas 
                elif(i.get('type') == 'room'):                                                  # asaj të instances finale(tree1,output.txt).
                    lastR = root1.findall('./constraints/constraint[last()]')[-1]
                    parentR = lastR.getparent()
                    parentR.insert(parent.index(lastR)+1,i)
           
###########################################################

for fname in fname_key:
    tree = etree.parse(fname)
    root = tree.getroot()
    sort_tag('course','id',fname_key[fname])
    sort_tag('course','ref',fname_key[fname])
    sort_tag('course','teacher',fname_key[fname])
    sort_tag('room','id',fname_key[fname])
    sort_tag('room','ref',fname_key[fname])
    sort_tag('curriculum','id',fname_key[fname])
    sort_tag('constraint','course',fname_key[fname])
    if(count == 0):                 # Objekti i fajllit të parë kopjohet në objektin 'tree1' të fajllit final(output.xml) në mënyrë                 
        tree1 = tree                # që ta kemi strukturen e fajllit final te gatshme.
        root1 = tree1.getroot()     # 'count == 0' është përdorur variabla count për të numëruar në 'dictionary(map,hash)'
        count = 1                   # për arsye se në 'dictionary' nuk kemi mundësi të indeksojmë.     
    else:
        write_tag('courses')
        write_tag('rooms')
        write_tag('curricula')
        write_tag('constraints',True)

root1.set('name','TechnicalFacultiesAutumnInstance')
tree1.write('output.xml',xml_declaration=True,encoding='utf-8',standalone=False)    # Bën "uparse" objektin 'tree1' dhe "write" në fajllin 'output.xml'
