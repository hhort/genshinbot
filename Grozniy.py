import telebot as tb
import requests as rq
from bs4 import BeautifulSoup as BS


token = '6057873926:AAEfD_3Wr0o8TORURrrmahIwosSCykvr5yE'
bot = tb.TeleBot(token)

#персонажи
characters = {'Кли' : 'klee',
              'Странник' : 'strannik',
              'Барбара' : 'barbara',
              'Беннет' : 'bennet',
              'Бэй Доу' : 'beidou',
              'Кэйа' : 'kaeya',
              'Лиза' : 'lisa',
              'Нин Гуан' : 'ningguang',
              'Ноэль' : 'noelle',
              'Рэйзор' : 'razor',
              'Сахароза' : 'sucrose',
              'Син Цю' : 'xingqiu',
              'Сян Лин' : 'xiangling',
              'Фишль' : 'fischl',
              'Чунь Юнь' : 'chongyun',
              'Эмбер' : 'amber',
              'Джинн' : 'jean',
              'Дилюк' : 'diluc',
              'Кэ Цин' : 'keqing',
              'Мона' : 'mona',
              'Ци Ци' : 'qiqi',
              'Венти' : 'venti',
              'Диона' : 'diona',
              'Тарталья' : 'tartaglia',
              'Синь Янь' : 'xinyan',
              'Чжун Ли' : 'zhongli',
              'Альбедо' : 'albedo',
              'Гань Юй' : 'ganyu',
              'Сяо' : 'xiao',
              'Ху Тао' : 'hu-tao',
              'Розария' : 'rosaria',
              'Янь Фэй' : 'yan-fey',
              'Эола' : 'eola',
              'Кадзуха' : 'kadzukha',
              'Аяка' : 'ayaka',
              'Кокоми' : 'kokomi',
              'Райден' : 'rayden',
              'Элой' : 'eloy',
              'Сара' : 'sara',
              'Ёимия' : 'yeimiya',
              'Саю' : 'sayu',
              'Дэхья' : 'dekhya',
              'Аль-Хайтам' : 'al-khaytam',
              'Яо Яо' : 'yao-yao',
              'Фарузан' : 'faruzan',
              'Лайла' : 'layla',
              'Нахида' : 'nakhida',
              'Нилу' : 'nilu',
              'Сайно' : 'sayno',
              'Кандакия' : 'kandakiya',
              'Дори' : 'Dori',
              'Тигнари' : 'tignari',
              'Коллеи' : 'kollei',
              'Хэйдзо' : 'kheydzo',
              'Синобу' : 'kuki',
              'Е лань' : 'e-lan',
              'Аято' : 'ayato',
              'Яэ Мико' : 'yae-miko',
              'Шень хэ' : 'shen-khe',
              'Юнь дзинь' : 'yun-tzin',
              'Итто' : 'itto',
              'Горо' : 'goro',
              'Тома' : 'toma',
              'Кокоми' : 'kokomi'}



@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Приветствую, {name}')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Напишите имя персонажа')
    bot.register_next_step_handler(message, search)

@bot.message_handler(content_type=['text'])
def search(message):
    char = characters[message.text]
    url = f'https://genshin-info.ru/wiki/personazhi/{char}/'
    response = rq.get(url)
    soup = BS(response.text, 'html.parser')
    a = soup.find_all('div', class_='builds__section _bonuses')
    for i in a:
        b = i.find('li')
        bot.send_message(message.chat.id, b.text)


bot.polling(none_stop=True)
