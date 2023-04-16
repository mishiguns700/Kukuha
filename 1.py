# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup
import random

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
# Варианты ответов на отказы
noo = ["Ладно, спрошу ещё раз. Вы ГОТОВЫ начать тестирование? /yes или /no",
       "Вы наверно неправильно поняли меня. Вы готовы пройти тест? /yes или /no",
       "Вы что глухой? Я спрошу членораздельно В-ы г-о-то-в-ы п-р-о-й-т-и т-е-с-т? /yes и-л-и /no",
       "Советую вам нажать на /yes не нужно нажимать на /no",
       "Давайте договоримся: Вы нажимаете на /yes я задаю вам вопросы, вы ответите на них и я покожу результат, иначе ("
       "если вы нажмёте на /no) мы так и не решим эту проблему",
       "Не усугубляйте своё положение! Нажмите на /yes если Вы продолжите нажиать н а /no Вы потеряете время!"
       ]
# Варианты приветствий
privet = ["Вы наверняка хотите пройти тест. Для формальности скажите, готовы ли вы пройти тест? /yes или /no",
          "Я бот тестер, готовы ли Вы начать тестирование? /yes или /no",
          "Я тот, кто поможет Вам понять кто Вы в этом мире. Готовы ли Вы пройти небольшой тест? /yes или /no",
          "Для начала тестирования выберите 2 варианта: /yes или /no",
          "Если Вы хотите пройти тестирование нажмите /yes иначе нажмите /no",
          "Я могу узнать ваш темперамент с помощью теста. Готовы ли Вы пройти его? /yes или /no"]
o = []
logger = logging.getLogger(__name__)
# Клавиатуры
# reply_keyboard1 был удалён, как слабое звено
reply_keyboard2 = [['/a', '/b', '/c', '/d']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)
reply_keyboard3 = [['/help', '/yes', '/no', '/authors']]
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=False)
reply_keyboard4 = [['/yes', '/no', '/authors']]
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=False)
reply_keyboard5 = [['/help', '/yes', '/no']]
markup5 = ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=False)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    # Приветствие
    # Все приветствия рандомизируются
    await update.message.reply_html(
        rf"Приветствую {user.mention_html()}! " + random.choice(privet), reply_markup=markup3
    )
    await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
    await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")


async def no(update, contex):
    # Ответы на отказы
    # Все ответы рандомизируются
    await update.message.reply_text(random.choice(noo))
    await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
    await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    # Поясниение, что из себя представляет бот и как с ним взаимодействовать
    await update.message.reply_text("Данный тест определяет тип вашего темперамента.")
    await update.message.reply_text("Вам будут предложены вопросы, на которые Вы будете отвечать, выбирая один из 4 "
                                    "вариантов ответа.")
    await update.message.reply_text("В конце Вам будет предоставлен результат ваших ответов, т. е. будет указан "
                                    "тип вашего темперамента.")
    await update.message.reply_text("(Всего темпераментов 4 - Сангвитик, Флегматик, Холерик и Меланхолик)")
    await update.message.reply_text("Итак, готовы ли Вы пройти этот тест? /yes или /no", reply_markup=markup4)
    await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")


async def authors(update, context):
    # Информация об авторах
    await update.message.reply_text("Авторами этого чуда являютя Михаил Киршенман (или же бог) и Александр Фомичев "
                                    "(рандомный чел), которые хотят чтобы им поставили побольше баллов.")
    await update.message.reply_text("Готовы ли вы теперь пройти тест? /yes или /no")
    await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help", reply_markup=markup5)


async def quest_1(update, context):
    # 1 вопрос
    await update.message.reply_text("1.Охарактерезуй себя:\n"
                                    "/a)подвижны и любознательны\n"
                                    "/b)спокойны и не торопливы\n"
                                    "/c)неусидчивы и суетливы\n"
                                    "/d)замкнуты и медлительны\n", reply_markup=markup2)


async def a(update, context):
    # Последующие вопросы
    # Каждый вариант ответа отсылает к нужным функциям
    # В даннам случае это ответ a
    # Все ответы запоминаются
    o.append("a")
    if len(o) == 1:
        await update.message.reply_text("2.Что из перечисленного соответствует Вам?\n"
                                        "/a)находчив и придирчив\n"
                                        "/b)спокоен и халоднокровен\n"
                                        "/c)решителен\n"
                                        "/d)раним и чувствителен\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("3.Что Вы думаете о своей самооценке?\n"
                                        "/a)она в порядке\n"
                                        "/b)не могу сказать точно\n"
                                        "/c)она высокая , но не завышенная\n"
                                        "/d)заниженная\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("4.В компании незнокомых людей Вы ...\n"
                                        "/a)чувствуете себя как и обычно\n"
                                        "/b)сначала присматриваетесь к окружающим\n"
                                        "/c)будете замкнутым и мочаливым\n"
                                        "/d)сразу попытаетесь влиться в коллектив\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("5.В экстремальной ситуации Вы ...\n"
                                        "/a)попытаетесь взвесить все за и против и выбрать подходяшее решение\n"
                                        "/b)понаблюдаете за остальными и выберите для себя подходящий вариант\n"
                                        "/c)будете паниковать и вспешке можете ощибиться\n"
                                        "/d)растеряетесь и загрустите(заплачите)\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "6.Представьте, вы пошли по неизвестному городу в поисках магазина, Ваши действия:\n"
            "/a)спросите у прохожих\n"
            "/b)вернётесь домой,когда узнаете тогда и пойдёте\n"
            "/c)попытаетесь самостоятельно выяснить(своми методами)\n"
            "/d)пойдёте,полагаясь на интуицию\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("7. Ваше сильное качество:\n"
                                        "/a)рациональность(рассудительны)\n"
                                        "/b)уравновешенность(спокойны)\n"
                                        "/c)позитивность(всегда хорошее настроение)\n"
                                        "/d)активность(избыток энергии)\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("8.Какая фигура симпотизирует Вам больше остальных?\n"
                                        "/a)Квадрат\n"
                                        "/b)Зигзаг\n"
                                        "/c)Треугольник\n"
                                        "/d)Круг\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "9.Вы случайно роняете предмет, который дорог Вам и от удара предмет ломается. Ваши действия:\n"
            "/a)очень расстроетесь(ничего не будете делать)\n"
            "/b)в сердцах кину предмет ещё раз(разозлитесь)\n"
            "/c)энергично притуплю к починке\n"
            "/d)спокойно подумаю,что можно сделать и выберу лучший вариант\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "10.Представьте ситуацию, Вам надо сдать важный экзамен, но вы не готовы. Ваши действия\n"
            "/a)попытаетесь вспомнить хоть что то и решить своими силами\n"
            "/b)распсихуетесь и не пойдёте на экзамен\n"
            "/c)загрустите(пустите всё на самотёк)\n"
            "/d)не всё потеряно, будете импровизировать\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        g = ''
        for i in o:
            g = g + i + ' '
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Сангвитик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Флегматик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Холерик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Меланхолик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        o.clear()


async def b(update, context):
    # Последующие вопросы
    # Каждый вариант ответа отсылает к нужным функциям
    # В даннам случае это ответ b
    # Все ответы запоминаются
    o.append("b")
    if len(o) == 1:
        await update.message.reply_text("2.Что из перечисленного соответствует Вам?\n"
                                        "/a)находчив и придирчив\n"
                                        "/b)спокоен и халоднокровен\n"
                                        "/c)решителен\n"
                                        "/d)раним и чувствителен\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("3.Что Вы думаете о своей самооценке?\n"
                                        "/a)она в порядке\n"
                                        "/b)не могу сказать точно\n"
                                        "/c)она высокая , но не завышенная\n"
                                        "/d)заниженная\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("4.В компании незнокомых людей Вы ...\n"
                                        "/a)чувствуете себя как и обычно\n"
                                        "/b)сначала присматриваетесь к окружающим\n"
                                        "/c)будете замкнутым и мочаливым\n"
                                        "/d)сразу попытаетесь влиться в коллектив\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("5.В экстремальной ситуации Вы ...\n"
                                        "/a)попытаетесь взвесить все за и против и выбрать подходяшее решение\n"
                                        "/b)понаблюдаете за остальными и выберите для себя подходящий вариант\n"
                                        "/c)будете паниковать и вспешке можете ощибиться\n"
                                        "/d)растеряетесь и загрустите(заплачите)\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "6.Представьте, вы пошли по неизвестному городу в поисках магазина, Ваши действия:\n"
            "/a)спросите у прохожих\n"
            "/b)вернётесь домой,когда узнаете тогда и пойдёте\n"
            "/c)попытаетесь самостоятельно выяснить(своми методами)\n"
            "/d)пойдёте,полагаясь на интуицию\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("7. Ваше сильное качество:\n"
                                        "/a)рациональность(рассудительны)\n"
                                        "/b)уравновешенность(спокойны)\n"
                                        "/c)позитивность(всегда хорошее настроение)\n"
                                        "/d)активность(избыток энергии)\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("8.Какая фигура симпотизирует Вам больше остальных?\n"
                                        "/a)Квадрат\n"
                                        "/b)Зигзаг\n"
                                        "/c)Треугольник\n"
                                        "/d)Круг\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "9.Вы случайно роняете предмет, который дорог Вам и от удара предмет ломается. Ваши действия:\n"
            "/a)очень расстроетесь(ничего не будете делать)\n"
            "/b)в сердцах кину предмет ещё раз(разозлитесь)\n"
            "/c)энергично притуплю к починке\n"
            "/d)спокойно подумаю,что можно сделать и выберу лучший вариант\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "10.Представьте ситуацию, Вам надо сдать важный экзамен, но вы не готовы. Ваши действия\n"
            "/a)попытаетесь вспомнить хоть что то и решить своими силами\n"
            "/b)распсихуетесь и не пойдёте на экзамен\n"
            "/c)загрустите(пустите всё на самотёк)\n"
            "/d)не всё потеряно, будете импровизировать\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        g = ''
        for i in o:
            g = g + i + ' '
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Сангвитик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Флегматик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Холерик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Меланхолик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        o.clear()


async def c(update, context):
    # Последующие вопросы
    # Каждый вариант ответа отсылает к нужным функциям
    # В даннам случае это ответ c
    # Все ответы запоминаются
    o.append("c")
    if len(o) == 1:
        await update.message.reply_text("2.Что из перечисленного соответствует Вам?\n"
                                        "/a)находчив и придирчив\n"
                                        "/b)спокоен и халоднокровен\n"
                                        "/c)решителен\n"
                                        "/d)раним и чувствителен\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("3.Что Вы думаете о своей самооценке?\n"
                                        "/a)она в порядке\n"
                                        "/b)не могу сказать точно\n"
                                        "/c)она высокая , но не завышенная\n"
                                        "/d)заниженная\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("4.В компании незнокомых людей Вы ...\n"
                                        "/a)чувствуете себя как и обычно\n"
                                        "/b)сначала присматриваетесь к окружающим\n"
                                        "/c)будете замкнутым и мочаливым\n"
                                        "/d)сразу попытаетесь влиться в коллектив\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("5.В экстремальной ситуации Вы ...\n"
                                        "/a)попытаетесь взвесить все за и против и выбрать подходяшее решение\n"
                                        "/b)понаблюдаете за остальными и выберите для себя подходящий вариант\n"
                                        "/c)будете паниковать и вспешке можете ощибиться\n"
                                        "/d)растеряетесь и загрустите(заплачите)\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "6.Представьте, вы пошли по неизвестному городу в поисках магазина, Ваши действия:\n"
            "/a)спросите у прохожих\n"
            "/b)вернётесь домой,когда узнаете тогда и пойдёте\n"
            "/c)попытаетесь самостоятельно выяснить(своми методами)\n"
            "/d)пойдёте,полагаясь на интуицию\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("7. Ваше сильное качество:\n"
                                        "/a)рациональность(рассудительны)\n"
                                        "/b)уравновешенность(спокойны)\n"
                                        "/c)позитивность(всегда хорошее настроение)\n"
                                        "/d)активность(избыток энергии)\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("8.Какая фигура симпотизирует Вам больше остальных?\n"
                                        "/a)Квадрат\n"
                                        "/b)Зигзаг\n"
                                        "/c)Треугольник\n"
                                        "/d)Круг\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "9.Вы случайно роняете предмет, который дорог Вам и от удара предмет ломается. Ваши действия:\n"
            "/a)очень расстроетесь(ничего не будете делать)\n"
            "/b)в сердцах кину предмет ещё раз(разозлитесь)\n"
            "/c)энергично притуплю к починке\n"
            "/d)спокойно подумаю,что можно сделать и выберу лучший вариант\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "10.Представьте ситуацию, Вам надо сдать важный экзамен, но вы не готовы. Ваши действия\n"
            "/a)попытаетесь вспомнить хоть что то и решить своими силами\n"
            "/b)распсихуетесь и не пойдёте на экзамен\n"
            "/c)загрустите(пустите всё на самотёк)\n"
            "/d)не всё потеряно, будете импровизировать\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        g = ''
        for i in o:
            g = g + i + ' '
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Сангвитик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Флегматик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Холерик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Меланхолик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        o.clear()


async def d(update, context):
    # Последующие вопросы
    # Каждый вариант ответа отсылает к нужным функциям
    # В даннам случае это ответ d
    # Все ответы запоминаются
    o.append("d")
    if len(o) == 1:
        await update.message.reply_text("2.Что из перечисленного соответствует Вам?\n"
                                        "/a)находчив и придирчив\n"
                                        "/b)спокоен и халоднокровен\n"
                                        "/c)решителен\n"
                                        "/d)раним и чувствителен\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("3.Что Вы думаете о своей самооценке?\n"
                                        "/a)она в порядке\n"
                                        "/b)не могу сказать точно\n"
                                        "/c)она высокая , но не завышенная\n"
                                        "/d)заниженная\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("4.В компании незнокомых людей Вы ...\n"
                                        "/a)чувствуете себя как и обычно\n"
                                        "/b)сначала присматриваетесь к окружающим\n"
                                        "/c)будете замкнутым и мочаливым\n"
                                        "/d)сразу попытаетесь влиться в коллектив\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("5.В экстремальной ситуации Вы ...\n"
                                        "/a)попытаетесь взвесить все за и против и выбрать подходяшее решение\n"
                                        "/b)понаблюдаете за остальными и выберите для себя подходящий вариант\n"
                                        "/c)будете паниковать и вспешке можете ощибиться\n"
                                        "/d)растеряетесь и загрустите(заплачите)\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "6.Представьте, вы пошли по неизвестному городу в поисках магазина, Ваши действия:\n"
            "/a)спросите у прохожих\n"
            "/b)вернётесь домой,когда узнаете тогда и пойдёте\n"
            "/c)попытаетесь самостоятельно выяснить(своми методами)\n"
            "/d)пойдёте,полагаясь на интуицию\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("7. Ваше сильное качество:\n"
                                        "/a)рациональность(рассудительны)\n"
                                        "/b)уравновешенность(спокойны)\n"
                                        "/c)позитивность(всегда хорошее настроение)\n"
                                        "/d)активность(избыток энергии)\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("8.Какая фигура симпотизирует Вам больше остальных?\n"
                                        "/a)Квадрат\n"
                                        "/b)Зигзаг\n"
                                        "/c)Треугольник\n"
                                        "/d)Круг\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "9.Вы случайно роняете предмет, который дорог Вам и от удара предмет ломается. Ваши действия:\n"
            "/a)очень расстроетесь(ничего не будете делать)\n"
            "/b)в сердцах кину предмет ещё раз(разозлитесь)\n"
            "/c)энергично притуплю к починке\n"
            "/d)спокойно подумаю,что можно сделать и выберу лучший вариант\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "10.Представьте ситуацию, Вам надо сдать важный экзамен, но вы не готовы. Ваши действия\n"
            "/a)попытаетесь вспомнить хоть что то и решить своими силами\n"
            "/b)распсихуетесь и не пойдёте на экзамен\n"
            "/c)загрустите(пустите всё на самотёк)\n"
            "/d)не всё потеряно, будете импровизировать\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        g = ''
        for i in o:
            g = g + i + ' '
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Сангвитик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Флегматик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Холерик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Поздравляем, Вы прошли тест! По результатам ваших ответов Вы Меланхолик!")
            await update.message.reply_text("Ваши ответы: " + g)
            await update.message.reply_text("Хотите ли Вы снова пройти тест? /yes или /no",
                                            reply_markup=markup3)
            await update.message.reply_text("Если Вы затрудняетесь в выборе ответа, нажмите /help")
            await update.message.reply_text("Также Вы можете узнать информацию об авторах, нажав /authors")
        o.clear()


def main():
    application = Application.builder().token("6218641307:AAETxF-N_OoITvKa98VUhk568qpmPt3k_RI").build()
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("yes", quest_1))
    application.add_handler(CommandHandler("a", a))
    application.add_handler(CommandHandler("b", b))
    application.add_handler(CommandHandler("c", c))
    application.add_handler(CommandHandler("d", d))
    application.add_handler(CommandHandler("no", no))
    application.add_handler(CommandHandler("authors", authors))
    application.run_polling()


if __name__ == '__main__':
    main()
