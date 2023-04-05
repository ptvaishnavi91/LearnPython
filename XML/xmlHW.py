import xml.etree.ElementTree as ET
import os
import sys

from PythonForDQE.HomeWork.XML.ClassesHW import Advertisement, User_Choice, News
from PythonForDQE.HomeWork.XML.ModuleFilesHW import File_Input
from PythonForDQE.HomeWork.XML.JSON_HW import News_Json



class News_xml(File_Input,Advertisement, User_Choice,News):
    def __init__(self):
        self.input_choice = input('How do you want to enter the news feed? 1. Through console, 2. Using input text file, 3. Using input json file, 4. Using xml input file  \n')

    def input_func(self):
        if self.input_choice == '1':
            import ClassesHW
        elif self.input_choice == '2':
            self.file_input_func()
        elif self.input_choice == '3':
            News_Json.json_input_func()
        elif self.input_choice == '4':
            self.xml_input_func()
        else:
            print('Incorrect input method selection, exiting')

    def xml_input_func(self):
        # Task 2: Default folder or user provided file path
        ip_file_path = input('Enter the path of the input file:\n')
        # Use news_input_file.xml

        sys_path = sys.path
        op_file_path = f'{sys_path[0]}\\output_xml_file.xml'

        xml_file = ET.parse(open(ip_file_path))
        print(xml_file)

        root = xml_file.getroot()

        for news in root.findall('category'):
            if news.get('name') == 'National News':
                text = news[0].text
                category_name = news.get('name')
                location = news[1].text
                date = news[2].text
                nat_news = News()
                nat_news.news_function(category_name, text, location, date)
            elif news.get('name') == 'International News':
                text = news[0].text
                category_name = news.get('name')
                location = news[1].text
                date = news[2].text
                internat_news = News()
                internat_news.news_function(category_name, text, location, date)
            elif news.get('name') == 'Advertisement':
                text = news[0].text
                exp_date = news[1].text
                ad = Advertisement()
                ad.private_ad(text, exp_date)
            elif news.get('name') == 'User Category':
                user_category = news[0].text
                text = news[1].text
                user_footer = news[2].text
                user_city = news[3].text
                user = User_Choice()
                user.user_function(user_category, text, user_footer, user_city)
            else:
                print('Entered category is incorrect, please check the options and enter the correct serial number.')
                exit()

        ET.dump(root)
        xml_file.write(op_file_path)

        ip_file = open(ip_file_path, 'r')
        op_file = open(op_file_path, 'r')

        ip_data = ip_file.readlines()
        op_data = op_file.readlines()

        i = 0
        print('Comparing input and output files:')
        for line1 in ip_data:
            if ip_data[i] == op_data[i]:
                print(f'Line {i} is Identical\n\t Line: {ip_data[i]}')
                compare = 'Identical'
            else:
                print(
                    f'Line {i} from input file is not matching with output file: \n\tInput:{ip_data[i]}\n\tOutput:{op_data[i]} ')
                compare = 'Non-identical'
            i += 1
        ip_file.close()
        op_file.close()

        if compare == 'Identical':
            os.remove(ip_file_path)




news_obj = News_xml()
news_obj.input_func()
