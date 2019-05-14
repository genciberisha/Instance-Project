#!/usr/bin/python3

import xml.etree.ElementTree as ET

tree = ET.parse('fme-as17.xml')

root = tree.getroot()
##################################### COurse
for i in root.iter('course'):
    if('id' in i.attrib):
        id_str = i.get('id')
        teach_str = i.get('teacher')
        i.set('id',id_str[0] + "07" + id_str[1:])
        i.set('teacher',teach_str[0] + "07" + teach_str[1:])
        #print(i.tag,i.attrib)


    if('ref' in i.attrib):
        ref_str = i.get('ref')
        i.set('ref',ref_str[0] + "07" + ref_str[1:])
###################################### Course End
##################################### Room
for i in root.iter('room'):
    if('id' in i.attrib):
        rid_str = i.get('id')
        i.set('id',rid_str[0] + "07" +rid_str[1:])
    elif('ref' in i.attrib):
        rref_str = i.get('ref')
        i.set('ref',rref_str[0] + "07" + rref_str[1:])
###################################### Room End

##################################### Curriculum
for i in root.iter('curriculum'):
    cur_str = i.get('id')
    i.set('id',cur_str[0] + "07" + cur_str[1:])
##################################### Curriculum End

for i in root.iter('constraint'):
    con_str = i.get('course')
    i.set('course',con_str[0] + "07" + con_str[1:])
 #   print(i.tag,i.attrib)


#print(ET.tostring(root,encoding='utf8').decode('utf8'))
tree.write('output.xml')
