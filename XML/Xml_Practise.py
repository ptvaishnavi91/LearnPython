import xml.etree.ElementTree as ET

xml_file = ET.parse('news_input_file.xml')

root = xml_file.getroot()

# print(root)
# print(type(root))
# print(root[1].attrib)
#
# xml_str = ET.fromstring('<a>123</a>')
# print(xml_str)
# print(xml_str.tag)
# print(xml_str.text)
# print(xml_str.attrib)
#
# ET.dump(xml_str) #only for debugging , doesnt return any value, hence cannot assign result to a variable
#
# print(root.find('category').attrib)
#
# for news in root.findall('category'):
#     print(news[0].text)
#     print(news.attrib)

# for smth in root.iter('location'): # iter= looks thro all the childs - findall - searches only first level of child
#     print(smth.tag)
#     print(type(smth))
#     print(smth.attrib)
#
# for smth in root.findall('location'):
#     print(smth.tag)

for smth in root.iter():
    if smth.get('name') == 'National News':
        # print(smth.attrib)
        # # print(smth.tag)
        # # print(smth.get('name'))
        # smth.set('country','Poland')
        # print(smth.text)

        for t in smth:
            #print(t.text)
            t.text = 'other values'

for smth in root.iter('text'):
    smth.text = f"${str(smth.text.replace('.','!'))+''}"
    smth.text.replace("a", "@")

root.remove(root.find('category'))

new_elem = ET.Element('test element')
new_elem.text = 'test text'
root.insert(0, new_elem)

new_comment = ET.Comment('test comment')
root[0].append(new_comment)

#xpath
for elem in root.iter():
    if elem.tag == 'location':
        print(elem.text)

for elem in root.findall('.//date'):
    print(elem.text)

for elem in root.findall('.//*[@name]'):
    print(elem.tag)
    print(elem.text)

for elem in root.findall('.//*[@n]'):
    print(elem.tag)

#ET.dump(root)
xml_file.write('output_xml_file.xml')
