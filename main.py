import telebot
from telebot import types

#setting up
bot = telebot.TeleBot("")
#seting completed

#start_private
@bot.message_handler(commands=['start', 'restart', 'Start', 'Restart'], chat_types='private')
def start(message):
    username = message.from_user.username
    links = types.InlineKeyboardMarkup()
    link1 = types.InlineKeyboardButton(text='MAIN GROUP', url='https://t.me/MetaKombat')
    link2 = types.InlineKeyboardButton(text='SHILL ARMY', url='https://t.me/MetaKombatShillArmy')
    link3 = types.InlineKeyboardButton(text='WEBSITE🌐', url='https://metakombat.net')
    link4 = types.InlineKeyboardButton(text='TWITTER📰', url='https://twitter.com/metakombatbsc')
    link5 = types.InlineKeyboardButton(text='Instagram📸', url='https://www.instagram.com/metakombat.bsc')
    links.add(*[link1,link2, link3,link4,link5])
    bot.send_message(message.chat.id, text='Hi @{} my devgeloper made me to only owrk in group only, so you can only use me in group but below are our official links'.format(username), reply_markup=links, )

#functions
#contract
@bot.message_handler(commands=['contract', 'Contract'], chat_types=['supergroup','group'])
def new_member(message):
    bot.reply_to(message, text='We have not launched yet. Contract address will be added here after launch.')

#marketing
@bot.message_handler(commands=['marketing', 'Marketing'], chat_types=['supergroup','group'])
def new_member(message):
    bot.reply_to(message, text='For any calls channel promotion and marketing enquiries please message @metakombatadmin 😊')

#whitelist
@bot.message_handler(commands=['whitelist', 'Whitelist', 'wl',], chat_types=['supergroup','group'])
def new_member(message):
    key = types.InlineKeyboardMarkup()
    call1 = types.InlineKeyboardButton(text='Sweepwidget Form🪐', url='https://sweepwidget.com/view/42921-qzirvotb')
    call2 = types.InlineKeyboardButton(text='🥷 Shill Armies', url='https://t.me/MetaKombatShillArmy')
    key.add(call1)
    key.add(call2)
    bot.reply_to(message, text='''
    ‼️WAYS YOU CAN GET WHITELISTED‼️

✨1: fill out the form below 

✨2: join our shill group & shill 

✨3: Be active in our community- participate in games and trivia 

✨4: win giveaways on call channels
    ''', reply_markup=key)


#giveaway
@bot.message_handler(commands=['giveaway', 'Giveaway'], chat_types=['group', 'supergroup'])
def giveaway(message):
    give = types.InlineKeyboardMarkup()
    give1 = types.InlineKeyboardButton(text='Giveaway🎰', url='https://sweepwidget.com/view/42921-qzirvotb')
    give.add(give1)
    bot.reply_to(message, text='*Metakombat*', reply_markup=give, parse_mode='markdown')

#shillarmy
@bot.message_handler(commands=['shillarmy', 'Shillarmy'], chat_types=['group', 'supergroup'])
def army(message):
    army = types.InlineKeyboardMarkup()
    armyu = types.InlineKeyboardButton(text='Shill Army🥷', url='https://t.me/MetaKombatShillArmy')
    army.add(armyu)
    bot.reply_to(message, text='*MetaKombat*', reply_markup= army, parse_mode= 'Markdown')

#social
@bot.message_handler(commands=['socials', 'Socials'], chat_types=['supergroup','group'])
def social(message):
    key1 = types.InlineKeyboardMarkup()
    instagram = types.InlineKeyboardButton(text='Instagram📸', url='https://www.instagram.com/metakombatbsc')
    twitter = types.InlineKeyboardButton(text='Twitter🐦', url='https://twitter.com/metakombatbsc')
    key1.add(instagram)
    key1.add(twitter)
    bot.reply_to(message, text='*Below are our social Links*', reply_markup=key1, parse_mode= 'markdown')

#presale
@bot.message_handler(commands=['presale', 'Presale'])
def presale(message):
    bot.reply_to(message, text='''
*🚨 PRESALE INFO 🚨*

❗️❗️PRESALE DATE: SATURDAY 8TH JANUARY❗️❗️

PRESALE WILL BE HELD ON PINKSALE

SC:  80 BNB
HC: 160 BNB
Min: 0.1 BNB
Max: 1 BNB    
    ''', parse_mode='markdown')

#website
@bot.message_handler(commands=['website', 'Website', 'web', 'site'], chat_types=['group', 'supergroup'])
def wbesite(message):
    web = types.InlineKeyboardMarkup()
    instagram = types.InlineKeyboardButton(text='Website🌏', url='https://metakombat.net/')
    web.add(instagram)
    bot.reply_to(message, text='*MetaKombat*', reply_markup=web, parse_mode='markdown')

#price & chart
@bot.message_handler(commands=['price', 'chart', 'Price', 'Chart'], chat_types=['group', 'supergroup'])
def Price(message):
    bot.reply_to(message, text='We are not Live, Beware of scammers.\nAdmins will never  dm you first.\n ')

#whitepaper
@bot.message_handler(commands=['whitepaper'], chat_types=['group', 'supergroup'])
def white(message):
    white = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Whitepaper📄', url='https://metakombat.net/wp-content/uploads/2021/12/Metakombat-whitepaper-2.pdf')
    white.add(button)
    bot.reply_to(message, text='*MetaKombat*', reply_markup= white, parse_mode= 'markdown')



bot.infinity_polling()