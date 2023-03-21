from datetime import datetime, date

class Category:
    def __init__(self):
        self.category = input("Enter the feed category number: \n1. National news \n2. International news\n3. Private Ad\n4. User's choice\n5. Exit\n")
        if self.category in ('1', '2', '3', '4'):
            self.text = input("Please enter the content:\n")
            self.date = datetime.now()
        else:
            print('Incorrect category')

class News(Category):
    def __init__(self):
        # super().__init__()
        self.news_location = input("Enter the location:\n")
       # self.news_content = input("Enter the news content:\n")

    def news_function(self, category='Category', text='Nothing', news_location='World', date='2099-01-01'):
        with open('Newsfeed_2103.txt', 'a') as f:
            f.write(f"Newsfeed: \n News {category} \n {text} \n {news_location}, {date}\n")
            print(f"Newsfeed: \n News {category} \n {text} \n {news_location}, {date}\n")
class Advertisement(Category):
    def __init__(self):
        # super().__init__(self)
        #self.ad_text = input("Enter the Private Ad:\n")
        try:
            self.exp_date = input("Enter the expiration date for the Ad  in the format dd/mm/YYYY :\n")
        except:
            print('Date format is incorrect.')

    def private_ad(self, text='Nothing', exp_date='01/01/2099'):
        exp_date = datetime.strptime(exp_date, '%d/%m/%Y')
        current_date = datetime.today()
        delta = exp_date - current_date
        delta_days = delta.__str__()
        days_list = delta_days.split('days')
        with open('Newsfeed_2103.txt', 'a') as f:
            f.write(f"Private Ad: \n {text} \n Actual Until: {exp_date}, {days_list[0]} days left\n")
            print(f"Private Ad: \n {text} \n Actual Until: {exp_date}, {days_list[0]} days left\n")

class User_Choice(Category):
    def __init__(self):
        # super().__init__(self)
        self.user_category = input("Enter the category of your choice:\n")
       # self.user_text = input(f"Enter the content for {self.user_category}:\n")
        self.user_footer = input("Enter your name:\n")
        self.user_city = input("Enter your city:\n")

    def user_function(self, user_category='None', text='Nothing', user_footer='Noname', user_city='Nowhere'):
        with open('Newsfeed_2103.txt', 'a') as f:
            f.write(f"{user_category}:\n{text}\nAuthor:{user_footer},{user_city}\n")
            print(f"{user_category}:\n{text}\nAuthor:{user_footer},{user_city}\n")

for i in range(0,5):
    cat = Category()
    category_name = cat.category
    if category_name == '1':
        nat_news = News()
        nat_news.news_function('National news', cat.text, nat_news.news_location, cat.date)
    elif category_name == '2':
        internat_news = News()
        internat_news.news_function('International news', cat.text, internat_news.news_location, cat.date)
    elif category_name == '3':
        ad = Advertisement()
        ad.private_ad(cat.text, ad.exp_date)
    elif category_name == '4':
        user = User_Choice()
        user.user_function(user.user_category, cat.text, user.user_footer, user.user_city)
    elif category_name == '5':
        print('Exiting')
        exit()
    else:
        print('Entered category is incorrect, please check the options and enter the correct serial number.')
