# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

o = []
logger = logging.getLogger(__name__)
reply_keyboard2 = [['/a', '/b', '/c', '/d']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! я бот тестер, готовы ли Вы начать тестирование? /yes or /no"
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def quest_1(update, context):
    await update.message.reply_text("1.Охарактерезуй себя:\n"
                                    "/a)подвижны и любознательны\n"
                                    "/b)спокойны и не торопливы\n"
                                    "/c)неусидчивы и суетливы\n"
                                    "/d)замкнуты и медлительны\n", reply_markup=markup2)


async def a(update, context):
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
        o.clear()


async def b(update, context):
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
        o.clear()


async def c(update, context):
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
        o.clear()


async def d(update, context):
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
    application.run_polling()


if __name__ == '__main__':
    main()
