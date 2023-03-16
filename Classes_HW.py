from datetime import datetime, date

class News:
    def __init__(self):
        self.news_category = input("Enter the news category: \n * National \n * International\n")
        self.news_location = input("Enter the location:\n")
        self.news_content = input("Enter the news content:\n")

    def news_function(self, news_category='Category', news_content='Nothing', news_location='World'):
        with open('Newsfeed_doc.txt', 'a') as f:
            f.write(f"Newsfeed: \n News {news_category} \n {news_content} \n {news_location}, {datetime.now()}\n")

class Advertisement():
    def __init__(self):
        self.ad_text = input("Enter the Private Ad:\n")
        self.exp_date = input("Enter the expiration date for the Ad:\n")

    def private_ad(self, ad_text='Nothing', exp_date='01/01/2099'):
        exp_date = datetime.strptime(exp_date, '%d/%m/%Y')
        current_date = datetime.today()
        delta = exp_date - current_date
        delta_days = delta.__str__()
        days_list = delta_days.split('days')
        with open('Newsfeed_doc.txt', 'a') as f:
            f.write(f"Private Ad: \n {ad_text} \n Actual Until: {exp_date}, {days_list[0]} days left\n")

class User_Choice():
    def __init__(self):
        self.user_category = input("Enter the category of your choice:\n")
        self.user_text = input(f"Enter the content for {self.user_category}:\n")
        self.user_footer = input("Enter your name:\n")
        self.user_city = input("Enter your city:\n")

    def user_function(self, user_category='None', user_text='Nothing', user_footer='Noname', user_city='Nowhere'):
        with open('Newsfeed_doc.txt', 'a') as f:
            f.write(f"{user_category}:\n{user_text}\nAuthor:{user_footer},{user_city}\n")

newsfeed1 = News()
newsfeed1.news_function(newsfeed1.news_category, newsfeed1.news_content, newsfeed1.news_location)
newsfeed2 = News()
newsfeed2.news_function(newsfeed2.news_category, newsfeed2.news_content, newsfeed2.news_location)
ad = Advertisement()
ad.private_ad(ad.ad_text, ad.exp_date)
u = User_Choice()
u.user_function(u.user_category, u.user_text, u.user_footer, u.user_city)

