import telebot
import buttons

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, 'Привет' + message.from_user.first_name + message.from_user.last_name, reply_markup=buttons.main_buttons())


@bot.callback_query_handler(func=lambda call: True)
def callback_checker(call):
    if call.data == 'chat_4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 GPT-4:\n'

                                    '📋 Используется самая последняя языковая модель GPT-4 Turbo. Умеет описывать ваши фотографии.\n'
                                    
                                    '🔘 Принимает текст, голос или фото.\n'
                                    
                                    '🗯 Чат без контекста — не учитывает контекст, каждый ваш запрос как новый диалог.\n'
                                    '⚡️ 1 запрос = 3 GT\n'
                                    
                                    '💬 Чат с контекстом — каждый ответ с учетом контекста вашего диалога.\n'
                                    '⚡️ 1 запрос = 4 GT\n'
                                    
                                    '└ Выберите чат:', reply_markup=buttons.choice_1())

    elif call.data == 'chat_3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 GPT-3.5:\n'

                                    '📋 Используется самая экономически эффективная модель GPT-3.5 Turbo.\n'

                                    '🔘 Принимает текстовое или голосовое сообщение.\n'

                                    '🗯 Чат без контекста — не учитывает контекст, каждый ваш запрос как новый диалог.\n'
                                    '⚡️ 1 запрос = 1 GT\n'
                                    
                                    '💬 Чат с контекстом — каждый ответ с учетом контекста вашего диалога.\n'
                                    '⚡️ 1 запрос = 2 GT', reply_markup=buttons.choice_1())

    elif call.data == 'photo':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 DALL·E:\n' 
                                   
                                    '📋 DALL·E 3 — это нейросеть, которая может создавать реалистичные изображения и произведения искусства на основе вашего описания.\n'
                                    
                                    '🔘 Принимает описание: текстовое или голосовое сообщение, либо фото.\n'
                                    
                                    '⚡️ 1 запрос = 12 GT\n'
                                    
                                    '└ Сгенерировать изображение:', reply_markup=buttons.choice_2())
    elif call.data == 'voice':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 Голосовой ассистент:\n'

                                    '📋 Первый голосовой ассистент в Telegram на базе ChatGPT.\n'
                                    
                                    '🔘 Принимает голосовое сообщение.\n'
                                    
                                    '⚡️ 1 запрос = 3 GT', reply_markup=buttons.choice_3())

    elif call.data == 'text_to_voice':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 Text-To-Speech:\n'
                                        
                                        '📋 Модель искусственного интеллекта, которая преобразует текст в естественно звучащий устный текст.\n'
                                        
                                        '⚡️ 1 запрос = 3 GT\n'
                                        
                                        '└ Выберите голос:', reply_markup=buttons.choice_4())

    elif call.data == 'audio_to_text':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🤖 Speech-To-Text:\n'
                                    
                                    '📋 Модель ИИ, которая преобразует ваше аудио в текст.\n'
                                    
                                    '⚡️ 1 запрос = 2 GT\n'
                                    
                                    '└ Попробуйте:', reply_markup=buttons.choice_5())

    elif call.data == 'back':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Привет {call.from_user.first_name} {call.from_user.last_name}',
                              reply_markup=buttons.main_buttons())


bot.infinity_polling()
