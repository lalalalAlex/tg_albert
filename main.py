import telebot
import buttons
import openai

bot = telebot.TeleBot('6984712635:AAEGvEDXBBh1-EnutVWro55bsMnBE7klQHQ', threaded=False, skip_pending=True)
openai.api_key = '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'


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, 'Привет' + message.from_user.first_name + message.from_user.last_name, reply_markup=buttons.main_buttons())


@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет' + message.from_user.first_name + message.from_user.last_name, reply_markup=buttons.main_buttons())


@bot.callback_query_handler(func=lambda call: True)
def callback_checker(call):
    if call.data == 'chat_4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 GPT-4:\n\n'

                                    '📋 Используется самая последняя языковая модель GPT-4 Turbo. Умеет описывать ваши фотографии.\n\n'
                                    
                                    '🔘 Принимает текст, голос или фото.\n\n'
                                    
                                    '🗯 Чат без контекста — не учитывает контекст, каждый ваш запрос как новый диалог.\n\n'
                                    '⚡️ 1 запрос = 3 GT\n\n'
                                    
                                    '💬 Чат с контекстом — каждый ответ с учетом контекста вашего диалога.\n\n'
                                    '⚡️ 1 запрос = 4 GT\n\n'
                                    
                                    '└ Выберите чат:', reply_markup=buttons.choice_0())

    elif call.data == 'chat_3':
        bot.send_message(call.message.chat.id,
                                '🤖 GPT-3.5:\n'

                                    '📋 Используется самая экономически эффективная модель GPT-3.5 Turbo.\n\n'

                                    '🔘 Принимает текстовое или голосовое сообщение.\n\n'

                                    '🗯 Чат без контекста — не учитывает контекст, каждый ваш запрос как новый диалог.\n\n'
                                    '⚡️ 1 запрос = 1 GT\n\n'
                                    
                                    '💬 Чат с контекстом — каждый ответ с учетом контекста вашего диалога.\n\n'
                                    '⚡️ 1 запрос = 2 GT', reply_markup=buttons.choice_1())
    elif call.data == 'not':
        user_text = call.message.text
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Инициация с ChatGPT 3 .')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Инициация с ChatGPT 3 ..')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Инициация с ChatGPT 3 ...')
        print(call.message)
        bot.send_message(call.message.from_user.id, 'Напишите что-нибудь...')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_text,
            max_tokens=150
        )
        bot.send_message(call.message.chat.id, f"Ответ от ChatGPT: {response.choices[0].text.strip()}")
    elif call.data == 'photo':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 DALL·E:\n' 
                                   
                                    '📋 DALL·E 3 — это нейросеть, которая может создавать реалистичные изображения и произведения искусства на основе вашего описания.\n\n'
                                    
                                    '🔘 Принимает описание: текстовое или голосовое сообщение, либо фото.\n\n'
                                    
                                    '⚡️ 1 запрос = 12 GT\n\n'
                                    
                                    '└ Сгенерировать изображение:', reply_markup=buttons.choice_2())
    elif call.data == 'voice':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 Голосовой ассистент:\n\n'

                                    '📋 Первый голосовой ассистент в Telegram на базе ChatGPT.\n\n'
                                    
                                    '🔘 Принимает голосовое сообщение.\n\n'
                                    
                                    '⚡️ 1 запрос = 3 GT', reply_markup=buttons.choice_3())

    elif call.data == 'text_to_voice':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 Text-To-Speech:\n\n'
                                        
                                        '📋 Модель искусственного интеллекта, которая преобразует текст в естественно звучащий устный текст.\n\n'
                                        
                                        '⚡️ 1 запрос = 3 GT\n\n'
                                        
                                        '└ Выберите голос:', reply_markup=buttons.choice_4())

    elif call.data == 'audio_to_text':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 Speech-To-Text:\n\n'
                                    
                                    '📋 Модель ИИ, которая преобразует ваше аудио в текст.\n\n'
                                    
                                    '⚡️ 1 запрос = 2 GT\n\n'
                                    
                                    '└ Попробуйте:', reply_markup=buttons.choice_5())

    elif call.data == 'back':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Привет {call.from_user.first_name} {call.from_user.last_name}',
                              reply_markup=buttons.main_buttons())


bot.infinity_polling()
