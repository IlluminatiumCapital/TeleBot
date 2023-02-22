from telebot.async_telebot import AsyncTeleBot
import asyncio
import requests

from telebot import types

bot = AsyncTeleBot('5797958121:AAGOLMDCQyuvjw-dpdV6m1pY4JcMpYnjakE')
COIN_NAME_TO_FIND = ""  # Creating the global variable for coinName


@bot.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, "Похоже на то что, кто-то решил подзаработать немного шекелей"
                                            "Ну что ж похвально, с нашим ботом ты достигнешь этого"
                                            "Добро пожаловать в мир длинноносых мамонтов"
                                            "Надевайте кипу, и приступим -> ✡️ ")
    markup_inline = types.InlineKeyboardMarkup()
    choosing_coin = types.InlineKeyboardButton(text='Choose coin', callback_data='choose')
    markup_inline.add(choosing_coin)
    await bot.send_message(message.chat.id, 'Choose a coin name:', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
async def answer(call):
    if call.data == 'choose':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        name_usdt = types.KeyboardButton('USDT')
        name_btc = types.KeyboardButton('BTC')
        name_busd = types.KeyboardButton('BUSD')
        name_bnb = types.KeyboardButton('BNB')
        name_eth = types.KeyboardButton('ETH')
        name_uah = types.KeyboardButton('UAH')
        name_shib = types.KeyboardButton('SHIB')

        markup_reply.add(name_usdt, name_btc, name_busd, name_bnb, name_eth, name_uah, name_shib)
        await bot.send_message(call.message.chat.id, 'Choose ', reply_markup=markup_reply)


@bot.message_handler(content_types=['text'])
async def send_price(message):
    if message.text == 'USDT':
        COIN_NAME_TO_FIND = "USDT"
        binance_buy_rate = get_binance_buy(COIN_NAME_TO_FIND)
        binance_sell_rate = get_binance_sell(COIN_NAME_TO_FIND)
        await bot.send_message(message.chat.id, f"""Курсы валют на 
            - Binance \"BUY\" 
            {binance_buy_rate}
            - Binance \"SELL\" 
            {binance_sell_rate}""")
    elif message.text == 'BTC':
        COIN_NAME_TO_FIND = "BTC"
        binance_buy_rate = get_binance_buy(COIN_NAME_TO_FIND)
        binance_sell_rate = get_binance_sell(COIN_NAME_TO_FIND)
        await bot.send_message(message.chat.id, f"""Курсы валют на 
            - Binance \"BUY\" 
            {binance_buy_rate}
            - Binance \"SELL\" 
            {binance_sell_rate}""")
    elif message.text == 'BUSD':
        COIN_NAME_TO_FIND = "BUSD"
        binance_buy_rate = get_binance_buy(COIN_NAME_TO_FIND)
        binance_sell_rate = get_binance_sell(COIN_NAME_TO_FIND)
        await bot.send_message(message.chat.id, f"""Курсы валют на 
            - Binance \"BUY\" 
            {binance_buy_rate}
            - Binance \"SELL\" 
            {binance_sell_rate}""")
    elif message.text == 'BNB':
        COIN_NAME_TO_FIND = "BNB"
        binance_buy_rate = get_binance_buy(COIN_NAME_TO_FIND)
        binance_sell_rate = get_binance_sell(COIN_NAME_TO_FIND)
        await bot.send_message(message.chat.id, f"""Курсы валют на 
            - Binance \"BUY\" 
            {binance_buy_rate}
            - Binance \"SELL\" 
            {binance_sell_rate}""")
    elif message.text == 'ETH':
        COIN_NAME_TO_FIND = "ETH"
        binance_buy_rate = get_binance_buy(COIN_NAME_TO_FIND)
        binance_sell_rate = get_binance_sell(COIN_NAME_TO_FIND)
        await bot.send_message(message.chat.id, f"""Курсы валют на 
            - Binance \"BUY\" 
            {binance_buy_rate}
            - Binance \"SELL\" 
            {binance_sell_rate}""")
    elif message.text == 'UAH':
        COIN_NAME_TO_FIND = "UAH"
        binance_buy_rate = get_binance_buy(COIN_NAME_TO_FIND)
        binance_sell_rate = get_binance_sell(COIN_NAME_TO_FIND)
        await bot.send_message(message.chat.id, f"""Курсы валют на 
            - Binance \"BUY\" 
            {binance_buy_rate}
            - Binance \"SELL\" 
            {binance_sell_rate}""")
    elif message.text == 'SHIB':
        COIN_NAME_TO_FIND = "SHIB"
        binance_buy_rate = get_binance_buy(COIN_NAME_TO_FIND)
        binance_sell_rate = get_binance_sell(COIN_NAME_TO_FIND)
        await bot.send_message(message.chat.id, f"""Курсы валют на 
            - Binance \"BUY\" 
            {binance_buy_rate}
            - Binance \"SELL\" 
            {binance_sell_rate}""")
    elif message.text == 'sexy':
        await bot.send_message(message.chat.id, f"""Ты тоже сладкий 👨‍❤️‍👨""")
    elif message.text == 'BTS':
        pic = 'https://sun9-75.userapi.com/impg/c857524/v857524361/111459/0xxLNZq9ieU.jpg?size=1280x720&quality=96&sign=200c85a227cf6387c9c6f1f0b145f0eb&c_uniq_tag=rDbKMxvSTPa1Kz8ddtMtaSCLuPWv_bTd1cwzNsDkEyw&type=album'
        await bot.send_photo(message.chat.id, pic)
        # await bot.send_message(message.chat.id, f"""Не братан, мы пидорасню не слушаем""")


@bot.message_handler(commands=['get_rates'])
async def send_rates(message):
    binance_buy_rate = get_binance_buy("BTC")
    binance_sell_rate = get_binance_sell("BTC")
    await bot.send_message(message.chat.id, f"""Курсы валют на
    - Binance \"BUY\" {binance_buy_rate}
    - Binance \"SELL\" {binance_sell_rate}""")


def get_binance_buy(name):  # string params
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    params = {
        "proMerchantAds": False,
        "page": 1,
        "rows": 10,
        "payTypes": [],
        "countries": [],
        "publisherType": None,
        "transAmount": "",
        "asset": name,
        "fiat": "UAH",
        "tradeType": "BUY",
    }
    response = requests.post(url=url, headers=headers, json=params).json()
    response_with_name = 'Name: ' + response['data'][0]['advertiser']['nickName'] + ' Price: ' + \
                         response['data'][0]['adv']['price']
    return response_with_name


def get_binance_sell(name):
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    params = {
        "proMerchantAds": False,
        "page": 1,
        "rows": 10,
        "payTypes": [],
        "countries": [],
        "publisherType": None,
        "tradeType": "SELL",
        "asset": name,
        "fiat": "UAH"
    }
    response = requests.post(url=url, headers=headers, json=params).json()
    response_with_name = 'Name: ' + response['data'][0]['advertiser']['nickName'] + ' Price: ' + \
                         response['data'][0]['adv']['price']
    return response_with_name


if __name__ == '__main__':
    asyncio.run(bot.polling())
