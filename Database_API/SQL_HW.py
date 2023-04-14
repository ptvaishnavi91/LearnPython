import sqlite3
from XML.xmlHW import News_xml
import xml.etree.ElementTree as ET
class newsSQL(News_xml):
    def __init__(self):
        self.input_choice = input('How do you want to enter the news feed? 1. Console to text, 2. Using input text file, 3. Using input json file, 4. XML to file, 5. XML to table \n')

    def input_func(self):
        if self.input_choice == '1':
            from Classes.Classes_HW import Newsfeed
            n = Newsfeed()
            n.select_category()
        elif self.input_choice == '2':
            self.file_input_func()
        elif self.input_choice == '3':
            self.json_input_func()
        elif self.input_choice == '4':
            self.xml_input_func()
        elif self.input_choice == '5':
            self.sql_output_func()
        else:
            print('Incorrect selection, exiting')


    def sql_output_func(self):
        ip_file_path = input('Enter the path of the input file:\n')
        #C:\Users\Vaishnavi_Peranamall\PycharmProjects\LearnPython\Database_API\news_input_file.xml
        xml_file = ET.parse(open(ip_file_path))
        #print(xml_file)
        root = xml_file.getroot()

        connection = sqlite3.connect('10test.db')
        cursor = connection.cursor()

        for news in root.findall('category'):
            if news.get('name') == 'National News':
                text = news[0].text
                category_name = news.get('name')
                location = news[1].text
                date = news[2].text
                #cursor.execute("DROP TABLE news_table")
                #cursor.execute("DELETE FROM news_table")
                #connection.commit()
                cursor.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'news_table'")
                if cursor.fetchone()[0] == 0:
                    cursor.execute("CREATE TABLE news_table (Category text, News text, Location text, Date date)")
                cursor.execute(f'''SELECT count(News) FROM news_table WHERE  News = '{text}' AND location = '{location}' ''')
                if cursor.fetchall()[0][0] == 0:
                   cursor.execute(f"INSERT INTO news_table values('{category_name}','{text}', '{location}','{date}')")
                connection.commit()
                cursor.execute('SELECT * FROM news_table')
                print(cursor.fetchall())
            elif news.get('name') == 'International News':
                text = news[0].text
                category_name = news.get('name')
                location = news[1].text
                date = news[2].text
                cursor.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'news_table'")
                if cursor.fetchone()[0] == 0:
                    cursor.execute("CREATE TABLE news_table (Category text, News text, Location text, Date date)")
                cursor.execute(
                    f'''SELECT count(News) FROM news_table WHERE  News = '{text}' AND location = '{location}' ''')
                if cursor.fetchall()[0][0] == 0:
                    cursor.execute(f"INSERT INTO news_table values('{category_name}','{text}', '{location}','{date}')")
                connection.commit()
                cursor.execute('SELECT * FROM news_table')
                print(cursor.fetchall())

            elif news.get('name') == 'Advertisement':
                text = news[0].text
                exp_date = news[1].text
                cursor.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'ad_table'")
                if cursor.fetchone()[0] == 0:
                    cursor.execute("CREATE TABLE ad_table (Ad text, Exp_date date)")
                cursor.execute(
                    f'''SELECT count(*) FROM ad_table WHERE  Ad = '{text}' ''')
                if cursor.fetchall()[0][0] == 0:
                    cursor.execute(f"INSERT INTO ad_table values('{text}', '{exp_date}')")
                connection.commit()
                cursor.execute('SELECT * FROM ad_table')
                print(cursor.fetchall())
            elif news.get('name') == 'User Category':
                user_category = news[0].text
                text = news[1].text
                user_footer = news[2].text
                user_city = news[3].text
                cursor.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'user_table'")
                if cursor.fetchone()[0] == 0:
                    cursor.execute("CREATE TABLE user_table (Category text, Content text, Footer text, City date)")
                cursor.execute(
                    f'''SELECT count(*) FROM user_table WHERE  Content = '{text}' AND Category = '{user_category}' ''')
                if cursor.fetchall()[0][0] == 0:
                    cursor.execute(f"INSERT INTO user_table values('{user_category}','{text}', '{user_footer}','{user_city}')")
                connection.commit()
                cursor.execute('SELECT * FROM user_table')
                print(cursor.fetchall())
            else:
                print('Entered category is incorrect, please check the options and enter the correct serial number.')
                exit()


sql_ob = newsSQL()
sql_ob.input_func()