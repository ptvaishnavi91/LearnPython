import json
import os
import sys

from Classes.Classes_HW import Advertisement, User_Choice, News
from ModuleFiles.ModuleFilesHW import File_Input


class News_Json(File_Input,Advertisement, User_Choice,News):
    def __init__(self):
        self.input_choice = input('How do you want to enter the news feed? 1. Through console, 2. Using input text file, 3. Using input json file \n')

    def input_func(self):
        if self.input_choice == '1':
            from Classes.Classes_HW import Newsfeed
            n = Newsfeed()
            n.select_category()
        elif self.input_choice == '2':
            self.file_input_func()
        elif self.input_choice == '3':
            self.json_input_func()
        else:
            print('Incorrect input method selection, exiting')

    def json_input_func(self):
        # Task 2: Default folder or user provided file path
        ip_file_path = input('Enter the path of the input file:\n')
        sys_path = sys.path
        op_file_path = f'{sys_path[0]}\\News_output.json'

        news_dict = json.load(open(ip_file_path))
        print(type(news_dict))
        # use C:\Users\Vaishnavi_Peranamall\PycharmProjects\LearnPython\JSON_Module\User_category_input.json
        # use National_news_input.json
        # use Advertisement_input.json
        # use International_news_input.json

        category_name = news_dict['Category']
        print(category_name)

        if category_name == 'National News':
            text = news_dict['Text']
            location = news_dict['Location']
            date = news_dict['Date']
            nat_news = News()
            nat_news.news_function(category_name, text, location, date)
        elif category_name == 'International News':
            text = news_dict['Text']
            location = news_dict['Location']
            date = news_dict['Date']
            internat_news = News()
            internat_news.news_function(category_name, text, location, date)
        elif category_name == 'Advertisement':
            text = news_dict['Text']
            exp_date = news_dict['Expiration_Date']
            ad = Advertisement()
            ad.private_ad(text, exp_date)
        elif category_name == 'User Category':
            user_category = news_dict['User_Category']
            text = news_dict['Text']
            user_footer = news_dict['Author_Name']
            user_city = news_dict['Author_City']
            user = User_Choice()
            user.user_function(user_category, text, user_footer, user_city)
        else:
            print('Entered category is incorrect, please check the options and enter the correct serial number.')
            exit()

        json.dump(news_dict, open(op_file_path, 'w'))
        op_file_dict = json.load(open(op_file_path))

        if news_dict == op_file_dict:
            print("Both input and output JSONs are equal")
            os.remove(ip_file_path)
        else:
            print("Input and Output JSONs are not equal")

if __name__ == '__main__':
    news_obj = News_Json()
    news_obj.input_func()