#coding: utf-8 -*- -*- 

import xml.etree.ElementTree as ET

import logging
logging.basicConfig(filename='new_string.txt', level=logging.INFO, filemode='w',format='%(message)s')

patch = 'values'
patch2 = 'values-zh-rCN'
print(r'Default folder \values')
print(r'Default folder \values-zh-rCN')

select = int(input('Please select language:\n1 - Russian\n2 - English\n>> '))

if select == 1:
    selectdir = 'DATABASE/RUS/'
elif select == 2:
    selectdir = 'DATABASE/EN/'
else:
    print('Error input number')

# baselang (English, russian ...)
LANGs = ET.parse(f'{selectdir}values/strings.xml').getroot()
LANGp = ET.parse(f'{selectdir}values/plurals.xml').getroot()

LANG2s = ET.parse(f'{selectdir}values-zh-rCN/strings.xml').getroot()
LANG2p = ET.parse(f'{selectdir}values-zh-rCN/plurals.xml').getroot()

# output CN lang
CNs = ET.parse(f'{patch}/strings.xml')
CNp = ET.parse(f'{patch}/plurals.xml')

CN2s = ET.parse(f'{patch2}/strings.xml')
CN2p = ET.parse(f'{patch2}/plurals.xml')

rootCNs = CNs.getroot()
rootCNp = CNp.getroot()

rootCN2s = CN2s.getroot()
rootCN2p = CN2p.getroot()

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

print(f'String elements CN: {len(rootCNs)} (values/strings.xml), String elements LANG (rus\en): {len(LANGs)} (baselang/values/strings.xml)')
print(f'String elements CN: {len(rootCN2s)} (values-zh-rCN/strings.xml), String elements LANG (rus\en): {len(LANG2s)} (baselang/values-zh-rCN/strings.xml)\n\n')

logging.info('====================================================================================')
logging.info('VALUE/STRING.XML')
logging.info(f'Translate this strings and paste in {selectdir}values/strings.xml')
logging.info('====================================================================================\n')

print('====================================================================================')
print('VALUE/STRING.XML')
print(f'Translate this strings and paste in {selectdir}values/strings.xml and re-run app')
print('====================================================================================\n')

for child in rootCNs:

    findBD = LANGs.find("string[@name='{index}']".format(index=child.attrib['name']))
    if findBD is not None:
        child.text = findBD.text
    else:
        count1 += 1
        print(f"Found new strings <{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")
        logging.info(f"<{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")



logging.info('====================================================================================')
logging.info('VALUE/PLURALS.XML')
logging.info(f'Translate this strings and paste in {selectdir}values/plurals.xml and re-run app')
logging.info('====================================================================================\n\n')

print('====================================================================================')
print('VALUE/PLURALS.XML')
print(f'Translate this strings and paste in {selectdir}values/plurals.xml')
print('====================================================================================\n\n')

for child in rootCNp:

    findBD = LANGp.find("plurals[@name='{index}']".format(index=child.attrib['name'])).find('item')
    for mg in child.getchildren():
        print(mg.text)
        if findBD is not None:
            mg.text = findBD.text
        else:
            count3 += 1
            print(f"Found new strings <plurals name=\"{child.attrib['name']}\"><item quantity=\"other\">{mg.text}</item></plurals>")
            logging.info(f"Found new strings <plurals name=\"{child.attrib['name']}\"><item quantity=\"other\">{mg.text}</item></plurals>")




logging.info('\n====================================================================================')
logging.info('VALUES-ZH-rCN/STRING.XML')
logging.info(f'Translate this strings and paste in {selectdir}values-zh-rCN/strings.xml and re-run app')
logging.info('====================================================================================\n')

print('\n====================================================================================')
print('VALUES-ZH-rCN/STRING.XML')
print(f'Translate this strings and paste in {selectdir}values-zh-rCN/strings.xml')
print('====================================================================================\n')


for child in rootCN2s:
    
    findBD = LANG2s.find("string[@name='{index}']".format(index=child.attrib['name']))
    if findBD is not None:
        child.text = findBD.text
    else:
        count4 += 1
        print(f"Found new strings: <{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")
        logging.info(f"<{child.tag} name=\"{child.attrib['name']}\">{child.text}</{child.tag}>")



logging.info('====================================================================================')
logging.info('VALUES-ZH-rCN/PLURALS.XML')
logging.info(f'Translate this strings and paste in {selectdir}values-zh-rCN/plurals.xml and re-run app')
logging.info('====================================================================================\n\n')

print('\n====================================================================================')
print('VALUES-ZH-rCN/PLURALS.XML')
print(f'Translate this strings and paste in {selectdir}values-zh-rCN/plurals.xml')
print('====================================================================================\n\n')


for child in rootCN2p:
    
    findBD = LANGp.find("plurals[@name='{index}']".format(index=child.attrib['name'])).find('item')
    for mg in child.getchildren():
        print(mg.text)
        if findBD is not None:
            mg.text = findBD.text
        else:
            count6 += 1
            print(f"Found new strings <plurals name=\"{child.attrib['name']}\"><item quantity=\"other\">{mg.text}</item></plurals>")
            logging.info(f"Found new strings <plurals name=\"{child.attrib['name']}\"><item quantity=\"other\">{mg.text}</item></plurals>")


CNs.write(f"{patch}/strings.xml", 'UTF-8', xml_declaration=1)
CNp.write(f"{patch}/plurals.xml", 'UTF-8', xml_declaration=1)

CN2s.write(f"{patch2}/strings.xml", 'UTF-8', xml_declaration=1)
CN2p.write(f"{patch2}/plurals.xml", 'UTF-8', xml_declaration=1)

print(f'\nTotal found new strings (values/strings.xml): {count1}')
print(f'Total found new strings (values/plurals.xml): {count3}')
print(f'Total found new strings (values-zh-rCN/strings.xml): {count4}')
print(f'Total found new strings (values-zh-rCN/plurals.xml): {count6}')
print(f'\nSee file NEW_STRING.TXT\n\n')

logging.info(f'Total found new strings (values/strings.xml): {count1}')
logging.info(f'Total found new strings (values/plurals.xml): {count3}')
logging.info(f'Total found new strings (values-zh-rCN/strings.xml): {count4}')
logging.info(f'Total found new strings (values-zh-rCN/plurals.xml): {count6}')

input("Press ENTER to exit...")