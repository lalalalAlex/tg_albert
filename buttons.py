from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_buttons():

    buttons = InlineKeyboardMarkup(row_width=2)

    chat_4 = InlineKeyboardButton(text='☁ Чат с GPT-4', callback_data='chat_4')
    chat_3 = InlineKeyboardButton(text='☁ Чат с GPT-3.5', callback_data='chat_3')
    generator_photo = InlineKeyboardButton(text='🎨 Генератор фото [DALL-E]', callback_data='photo')
    voice_helper = InlineKeyboardButton(text='Голосовой помощник', callback_data='voice')
    text_to_audio = InlineKeyboardButton(text='🗨️ Текст в аудио', callback_data='text_to_voice')
    audio_to_text = InlineKeyboardButton(text='🔉 Аудио в текст', callback_data='audio_to_text')
    helper = InlineKeyboardButton(text='🆘 Помощь', callback_data='helper')
    settings = InlineKeyboardButton(text=' Настройки', callback_data='settings')

    buttons.add(chat_4, chat_3)
    buttons.row(generator_photo)
    buttons.row(voice_helper)
    buttons.row(text_to_audio)
    buttons.row(audio_to_text)
    buttons.add(helper, settings)

    return buttons


def choice_1():
    buttons = InlineKeyboardMarkup(row_width=2)
    bez = InlineKeyboardButton(text='Без контекста', callback_data='not')
    c = InlineKeyboardButton(text='С контекстом', callback_data='with')
    back = InlineKeyboardButton(text='Назад', callback_data='back')

    buttons.add(bez, c)
    buttons.row(back)

    return buttons


def choice_2():
    buttons = InlineKeyboardMarkup(row_width=1)
    try_ = InlineKeyboardButton(text='Попробовать', callback_data='try')
    back = InlineKeyboardButton(text='Назад', callback_data='back')

    buttons.add(try_, back)

    return buttons


def choice_3():
    buttons = InlineKeyboardMarkup(row_width=1)
    start_dialogue = InlineKeyboardButton(text='Начать диалог', callback_data='start_dialogue')
    back = InlineKeyboardButton(text='Назад', callback_data='back')

    buttons.add(start_dialogue, back)

    return buttons


def choice_4():
    buttons = InlineKeyboardMarkup(row_width=2)
    alloy = InlineKeyboardButton(text='alloy', callback_data='alloy')
    echo = InlineKeyboardButton(text='echo', callback_data='echo')
    nova = InlineKeyboardButton(text='nova', callback_data='nova')
    fable = InlineKeyboardButton(text='fable', callback_data='fable')
    shimmer = InlineKeyboardButton(text='shimmer', callback_data='shimmer')
    back = InlineKeyboardButton(text='Назад', callback_data='back')

    buttons.add(alloy, echo, fable, nova)
    buttons.row(shimmer)
    buttons.row(back)

    return buttons


def choice_5():
    buttons = InlineKeyboardMarkup(row_width=1)
    try_ = InlineKeyboardButton(text='Попробовать', callback_data='try')
    back = InlineKeyboardButton(text='Назад', callback_data='back')

    buttons.add(try_, back)

    return buttons


def choice_0():
    buttons = InlineKeyboardMarkup(row_width=2)
    bez = InlineKeyboardButton(text='Без контекста', callback_data='not_1')
    c = InlineKeyboardButton(text='С контекстом', callback_data='with_1')
    back = InlineKeyboardButton(text='Назад', callback_data='back')

    buttons.add(bez, c)
    buttons.row(back)

    return buttons
