#coding: utf-8 -*- -*- 

import xml.etree.ElementTree as ET

import logging
logging.basicConfig(filename='string.txt', level=logging.INFO, filemode='w',format='%(message)s')

treeCN = ET.parse('values/strings.xml')
treeLANG = ET.parse('values-strings.xml')
treeCN2 = ET.parse('values-zh-rCN/strings.xml')
treeLANG2 = ET.parse('values-zh-rCN-strings.xml')


rootCN = treeCN.getroot()
rootLANG = treeLANG.getroot()
rootCN2 = treeCN2.getroot()
rootLANG2 = treeLANG2.getroot()

count = 0
count2 = 0

print(f'String elements CN: {len(rootCN)}, String elements LANG (rus\en): {len(rootLANG)}\n\n')

logging.info('====================================================================================')
logging.info('VALUE/STRING.XML')
logging.info('====================================================================================\n\n')

print('====================================================================================')
print('VALUE/STRING.XML')
print('====================================================================================\n\n')

for child in rootCN:

    findBD = rootLANG.find("string[@name='{index}']".format(index=child.attrib['name']))
    if findBD is not None:
        child.text = findBD.text
    else:
        count = count + 1
        print(f"Found new strings <{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")
        logging.info(f"<{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")

logging.info('\n====================================================================================')
logging.info('VALUES-ZH-rCN//STRING.XML')
logging.info('====================================================================================\n\n')

print('\n====================================================================================')
print('VALUES-ZH-rCN//STRING.XML')
print('====================================================================================\n\n')


for child in rootCN2:
    
    findBD = rootLANG2.find("string[@name='{index}']".format(index=child.attrib['name']))
    if findBD is not None:
        child.text = findBD.text
    else:
        count2 = count2 + 1
        print(f"Found new strings: <{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")
        logging.info(f"<{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")


treeCN.write("values/strings.xml", 'UTF-8', xml_declaration=1)
treeCN2.write("values-zh-rCN/strings.xml", 'UTF-8', xml_declaration=1)
print (f"\nTotal found new strings (values/strings.xml): {count}\nTotal found new strings (values-zh-rCN/strings.xml): {count2}\n\nSee file STRING.TXT\n\n")

input("Press ENTER to exit...")