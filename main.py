import random
import telebot

# import webbrowser
# import time

bot_token = '988563200:AAHTscEL3pmsgAnSsQwdVuhpfAqjbmyrMMs'
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(func=lambda message: message.voice is not None)
def aud(message):
    bot.reply_to(message, 'its an audio')


@bot.message_handler(content_types=['sticker'])
def per(message):
    if message.sticker.emoji == "👋":
        rand = ['1.tgs', '2.webp', '3.tgs', '5.tgs', '6.tgs', '7.tgs']
        sti = open('stickers/hi/' + random.choice(rand), 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.sticker.emoji == '😡' or message.sticker.emoji == '😠':
        rand = ['1.tgs', '2.tgs', '3.tgs', '5.tgs', '6.tgs', '7.tgs', '8.webp', '9.webp']
        sti = open('stickers/shock/' + random.choice(rand), 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif message.sticker.emoji == '🤦‍♂️' or message.sticker.emoji == '🙄' or message.sticker.emoji == "😑":
        rand = ['1.tgs', '2.tgs', '3.tgs', '5.tgs', '6.tgs', '7.tgs', '8.webp', '9.webp']
        sti = open('stickers/shock/' + random.choice(rand), 'rb')
        bot.send_sticker(message.chat.id, sti)
    else:
        rand = ['tgs1.tgs', 'tgs2.tgs', 'tgs3.tgs', 'tgs4.tgs', 'tgs5.tgs', 'tgs6.tgs', 'tgs7.tgs', 'tgs8.tgs',
                'tgs9.tgs', 'tgs10.tgs', 'h (1).tgs', 'h (2).tgs', 'h (4).tgs', 'h (3).tgs', 'h (5).tgs', 'h (6).tgs',
                'h (7).tgs', 'h (8).tgs', 'h (9).tgs', 'h (10).tgs', 'h (11).tgs', 'h (12).tgs', 'hw (1).tgs',
                'hw (2).tgs', 'hw (3).tgs', 'hw (4).tgs', 'hw (5).tgs', 'hw (6).tgs', 'hw (7).tgs', 'hw (8).tgs',
                'hw (9).tgs', 'hw (10).tgs', 'hw (11).tgs', 'hw (12).tgs', 'hw (13).tgs', 'hw (14).tgs', 'hw (15).tgs']
        sti = open('stickers/Randstickers/' + random.choice(rand), 'rb')
        bot.send_sticker(message.chat.id, sti)


@bot.message_handler(regexp="(?=.*(are you|name))(?=.*(who|what))")
def name(message):
    bot.reply_to(message, "I am your Medical Assistant")


@bot.message_handler(func=lambda
        message: message.text is not None and 'hi' in message.text.lower() or message.text is not None and 'hello' in message.text.lower())
def wel(message):
    bot.reply_to(message,
                 'Hello ' + message.from_user.first_name + '. Welcome to MedicalBot using pyTelegramBotAPI.How can i help you?🙂')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!I am active as ever.Go ahead and ask me your Queries.')
    file_id = ['1.tgs', '2.webp', '3.tgs', '4.webp', '5.tgs', '6.tgs', '7.tgs']
    sti = open('stickers/hi/' + random.choice(file_id), 'rb')
    bot.send_sticker(message.chat.id, sti)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
                 "Here's the list of features in provide:\n/start-Activate me😋\n/desc-About me😍\n/medinfo-Health Info\npretty cool huh😎")


@bot.message_handler(commands=['medinfo'])
def send_m(message):
    bot.reply_to(message, 'Please send name of the disease to continue✌️:\n/amru-send to know about Maa Amrutam Yojna')


@bot.message_handler(commands=['desc'])
def send_d(message):
    bot.reply_to(message,
                 'This bot was created to fulfill otherwordly http://www.magujarat.com/about-gujarati.html of E divsion.Proceed with caution.')


@bot.message_handler(func=lambda message: message.text is not None and 'how are you' in message.text.lower())
def sendd(message):
    bot.reply_to(message, "i've had an exciting day,looking up some fun things to do,What can i do for you🙂")


@bot.message_handler(func=lambda message: message.text is not None and 'flu' in message.text.lower())
def flu(message):
    bot.reply_to(message,
                 "The flu, also called influenza, is a respiratory infection caused by viruses. Sometimes it causes mild illness. But it can also be serious or even deadly, especially for people over 65, newborn babies, and people with certain chronic illnesses.\nFor more Information visit:<a href='https://en.wikipedia.org/wiki/Influenza'>Wiki</a>",
                 parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text is not None and 'diabetes' in message.text.lower())
def dia(message):
    bot.reply_to(message,
                 "Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.\nFor more information visit:<a href='https://en.wikipedia.org/wiki/Diabetes'>Wiki</a>",
                 parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text is not None and 'fever' in message.text.lower())
def fev(message):
    bot.reply_to(message,
                 "Fever is when a human's body temperature goes above the normal range of 36–37° Centigrade (98–100° Fahrenheit). It is a common medical sign. Other terms for a fever include pyrexia and controlled hyperthermia. As the body temperature goes up, the person may feel cold until it levels off and stops rising.\nFor more information visit:<a href='https://en.wikipedia.org/wiki/Fever'>Wiki</a>",
                 parse_mode='HTML')


@bot.message_handler(func=lambda
        message: message.text is not None and 'measure' in message.text.lower() and 'blood pressure' in message.text.lower())
def sendbp1(message):
    bot.reply_to(message,
                 'Unfortunately, I am physically unable to provide what you ask for🤷‍♂.But visiting a doctor would definitely help you😊.')


@bot.message_handler(func=lambda message: message.text is not None and 'what is blood pressure' in message.text.lower())
def sendbp(message):
    bot.reply_to(message,
                 "Blood pressure (BP) is the pressure of circulating blood on the walls of blood vessels. Most of this pressure is due to work done by the heart by pumping blood through the circulatory system.\nNormal resting blood pressure in an adult is approximately 120 millimetres of mercury (16 kPa) systolic, and 80 millimetres of mercury (11 kPa) diastolic, abbreviated 120/80 mmHg.\nFor more Information visit:<a href='https://en.wikipedia.org/wiki/Blood_pressure'>Wiki</a>",
                 parse_mode='HTML')


@bot.message_handler(regexp="(?=.*appetite)(?=.*(loss|decrease))")
def lapp(message):
    bot.reply_to(message,
                 "Lack of appetite, or decreased hunger, is one of the most troublesome nutrition problems you can experience. Although it is a common problem, its cause is unknown. There are some medicines that might stimulate your appetite. Ask your doctor if such medicines would help you.\n*Solutions:-*\n~Eat smaller meals and snacks more frequently.\n~Eating six or seven or eight times a day might be more easily tolerated than eating the same amount of food in three meals.\n~Talk to your doctor. Sometimes, poor appetite is due to depression, which can be treated. Your appetite is likely to improve after depression is treated.\n~Avoid non-nutritious beverages such as black coffee and tea.\n~Try to eat more protein and fat, and less simple sugars.\n~Walk or participate in light activity to stimulate your appetite.",
                 parse_mode="Markdown")


@bot.message_handler(regexp="(?=.*weight)(?=.*(loss|decrease))")
def lwei(message):
    bot.reply_to(message,
                 'If your doctor tells you that you have lost too much weight, or if you are having difficulty maintaining a healthy weight, here are some tips:\n=>Drink milk or try  "high-calorie recipes"  instead of drinking low-calorie beverages.\n=>Ask your doctor or dietitian about nutritional supplements. Sometimes, supplements in the form of snacks, drinks (such as Ensure® or Boost®), or vitamins might be prescribed to eat between meals. These supplements help you increase your calories and get the right amount of nutrients every day. Note: Do not use supplements in place of your meals.\n=>Avoid low-fat or low-calorie products unless you have been given other dietary guidelines. Use whole milk, whole milk cheese, and yogurt.\n=>Use the "*Calorie Boosters*"  to add calories to your favorite foods.',
                 parse_mode="Markdown")


@bot.message_handler(regexp="(?=.*anemia)(?=.*(what|mean|how))")
def ane(message):
    bot.reply_to(message,
                 "Anemia is a condition in which you lack enough healthy red blood cells to carry adequate oxygen to your body's tissues. Having anemia can make you feel tired and weak. There are many forms of anemia, each with its own cause. Anemia can be temporary or long term, and it can range from mild to severe.\nFor more Information visit:<a href='https://www.medicalnewstoday.com/articles/158800.php'>Click Here</a>",
                 parse_mode='HTML')


@bot.message_handler(regexp="(?=.*arthritis)(?=.*(what|mean|how))")
def art(message):
    bot.reply_to(message,
                 "Arthritis means joint inflammation, but the term is used to describe around 200 conditions that affect joints, the tissues that surround the joint, and other connective tissue. It is a rheumatic condition. The most common form of arthritis is osteoarthritis.\nFor more Information visit:<a href='https://www.medicalnewstoday.com/articles/7621.php'>Click Here</a>",
                 parse_mode='HTML')


@bot.message_handler(regexp="(?=.*cancer)(?=.*(what|mean|how))")
def can(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Visit the page',
                                                    url='https://www.medicalnewstoday.com/articles/323648.php'))
    bot.reply_to(message,
                 "Cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body. These contrast with benign tumors, which do not spread.\nFor more Information visit:<a href='https://www.medicalnewstoday.com/articles/323648.php'>Click Here</a>",
                 parse_mode="HTML", reply_markup=keyboard)
@bot.message_handler(regexp="(?=.*bp)(?=.*(what|mean|how))")
def sendbp1(message):
    bot.reply_to(message,
                 "Blood pressure (BP) is the pressure of circulating blood on the walls of blood vessels. Most of this pressure is due to work done by the heart by pumping blood through the circulatory system.\nNormal resting blood pressure in an adult is approximately 120 millimetres of mercury (16 kPa) systolic, and 80 millimetres of mercury (11 kPa) diastolic, abbreviated 120/80 mmHg.\nFor more Information visit:<a href='https://en.wikipedia.org/wiki/Blood_pressure'>Wiki</a>",
                 parse_mode='HTML')
@bot.message_handler(func=lambda message: message.text is not None and 'what is bmi' in message.text.lower())
def send1(message):
    '''keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
    telebot.types.InlineKeyboardButton('Yes!', callback_data='get-yes'),
    telebot.types.InlineKeyboardButton('No!', callback_data='get-no')
    )'''
    msg = bot.reply_to(message,
                       "Body Mass Index(BMI) is a measurement of a person's leanness or corpulence based on their height and weight, and is intended to quantify tissue mass. It is widely used as a general indicator of whether a person has a healthy body weight for their height. Specifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between.Do you want to calculate your BMI?🧐")
    bot.register_next_step_handler(msg, send2)


'''@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "get-yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "get-no":
        bot.answer_callback_query(call.id, "Answer is No")'''


def send2(message):
    if message.text.lower() == 'yes':
        bot.reply_to(message,
                     '<a href="https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm">BMI Calculator</a>',
                     parse_mode='HTML')
    elif message.text.lower() == 'no':
        bot.reply_to(message, 'Have fun😄')
    else:
        bot.reply_to(message, 'Well, that was unexpected!')


@bot.message_handler(commands=['amru'])
def amru_hand(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Click Here', url='http://www.magujarat.com/about-gujarati.html'))
    bot.send_message(message.chat.id, 'Ma Amrutam Yojna Website', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def unrec(message):
    bot.send_message(message.chat.id, "Sorry! I wasn't able to recognize what you sent.Please try again")


bot.polling(none_stop=True)