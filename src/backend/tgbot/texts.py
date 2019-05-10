############# TEXTS #############
# Start
TEXT_HELLO = 'Привет, как дела? Что делать будем?'

# Check registration status
TEXT_ENTER_EMAIL = 'Напишите свою почту, либо введите /skip, чтобы вернуться назад.'
TEXT_SKIP_EMAIL = 'Хорошо, почту можно ввести в другой раз.'
TEXT_EMAIL_NOT_OK = 'К сожалению, данного адреса не оказалось в списке инвайтов. Загляните в следующий раз. 👀'
TEXT_EMAIL_OK = 'Поздравляю! Вы получили приглашение на Data Fest⁶! Проверьте свою почту, там должно быть письмо с кодом для авторизации.'

# Authorization
TEXT_AUTH_EMAIL_OK = 'Хорошо, теперь введите код, который был Вам выслан на данный email в письме-приглашении.'
TEXT_CODE_NOT_OK = 'Вы ввели не правильный код, попробуйте еще раз.'
TEXT_CODE_OK = 'Вы авторизовались, теперь Вы можете попробовать поучаствовать в розыгрыше мерчендайза или в Random beer.'
TEXT_EMAIL_USED_BY_OTHER_USER = 'Под таким email уже авторизован другой пользователь!!!'
# Get news
TEXT_NEWS = "Тут можно подписаться на последние обновления, а также посмотреть последние новости феста. Подписка гарантирует получение уведомления о коде для авторизации."
TEXT_NEWS_SUBSCRIBED = "Подписка на новости в деле! 🔥"
TEXT_NEWS_UNSUBSCRIBED = "Вы отписались от новостей. 😢"
TEXT_NEWS_STAT = '''Статистика по пользователям:
Всего пользователей: {}
С подпиской на новости: {}
Победителей: {}
Админов: {}
'''



# Random prize
TEXT_CHOOSE_YOUR_SIZE = 'Для участия в розыгрыше мерча выберите свой размер 👕. Для каждой категории будет свой отдельный розыгрыш.'
TEXT_KNOW_SIZE = 'Ваш размер {}, если захотите изменить размер, нажмите соответсвующую кнопку 👇.'
TEXT_CHOSEN_SIZE = 'Выбран размер {}, удачи в розыгрыше!'
TEXT_CHANGE_SIZE = 'Хорошо, давайте выберем новый размер.'
TEXT_START_RANDOM_PRIZE = "Статистика по юзерам:{}\n\nДанные из Prizes:{}\n\nВыберите дальнейшие действия."
TEXT_EMPTY_TABLE_PRIZE = "Таблица Prizes пуста!"
TEXT_RANDOM_PRIZE_BROADCAST_STARTED = "Розыгрыш призов запущен"
TEXT_RANDOM_PRIZE_BROADCAST_DONE = "Розыгрыш призов выполнен. {} отправлено. {} ошибок"
TEXT_RANDOM_PRIZE_NOT_SUCCEED_BROADCAST_DONE = "Броадкаст проигравшим выполнен. {} отправлено. {} ошибок"

TEXT_CONGRATULATION = 'Поздравляю Вы выграли приз 🎉🎉🎉, забрать приз <там-то у того-то>.'
TEXT_RANDOM_PRIZE_NOT_SUCCEED = 'Розыгрыш призов завершен. Спасибо за участие'

# Random beer
TEXT_RULES = 'Random beer это возможность прокачать свой нетворкинг.\n' \
             'Для участия в Random beer, Вы должны согласиться предоставить данные такие как ник телеграмма, ник ODS или ссылку на соц. сеть другому человеку.\n' \
             'За день у вас может быть несколько встреч, но не больше 10. Удачи!'
TEXT_RULES_NOT_ACCEPTED = 'Вы не приняли правила, поэтому мы не можем допустить вас до Random beer.'
TEXT_RULES_ACCEPTED_NEED_TG_NICK = "Отлично, для участия, вам надо заполнить данные, введите свой ник в телеграмме либо введите /skip, чтобы пропустить данный шаг."
TEXT_NEED_ODS_NICK = "Хорошо, теперь введите свой ник в ODS. Введите /skip, чтобы пропустить данный шаг."
TEXT_NEED_SN_LINK = 'Почти готово, вы можете оставить ссылку на себя в соц. сети или пропустить данный шаг отправив /skip.'
TEXT_RANDOM_BEER_MENU = 'Ваши данные:\n - Telegram nick: {};\n - ODS nick: {};\n - Social network link: {}'
TEXT_NOT_ENOUGH_PARTICIPANTS = "К сожалению других участников еще нет, попробуйте найти пару чуть позже."
TEXT_RANDOM_BEER_MATCH = 'Итак, великий рандом подобрал тебе партнера в Random beer!\n' \
                         'Контакты партнера: \n - Telegram nick: {};\n - ODS nick: {};\n - Social network link: {}\n' \
                         'Напишите ему/ей и договоритесь о встрече, хорошей встречи'
TEXT_FAILED_SENT = 'Что-то пошло не так! Ваш партнер заблокировал бота и мы не смогли с ним связаться. Обратитесь к разработчику.'
TEXT_END_MEETING = 'Хорошо, надеюсь встреча Вам понравилась.'
TEXT_NOT_ENOUGH_INFO = 'У Вас заполнено слишком мало полей для участия, заполните хотя бы одно поле.'
TEXT_SHOULD_END_MEETING = 'Прежде чем начать следующую встречу, Вам следует закончить предыдущую.'
TEXT_WRITE_FEEDBACK = "Напишите отзыв о встрече в одном сообщении о том, как это было?"
TEXT_LIMIT_IS_OVER = 'Вы выбрали лимит встреч на сегодня.'
TEXT_GOTO_RANDOM_COFFEE = 'Понравился формат встреч? Чего ждешь? Добавляйся в random coffee! https://m.me/676926106042348'
TEXT_CHANGE_FIELD = 'Вы решили {}. Введите новое значение либо введите /skip, чтобы пропустить данный шаг.'
TEXT_SUCCESSFULLY_CHANGED = 'Хорошо. Ваши данные изменены.'

# On Major
TEXT_MAJOR_CODE = 'Введите код который был озвучен на Major'
TEXT_MAJOR_CODE_OK = 'Отлично! Теперь вы можете поучавствовать в Random beer и розыгрыше мерчендайза.'
TEXT_MAJOR_CODE_NOT_OK = 'Вы ввели не правильный код.'
TEXT_ALREADY_ON_MAJOR = 'Вы уже на Major!'

# NVIDIA
TEXT_JETSON = 'Хочешь Jetson?\nЗаполни форму по ссылке: http://bit.ly/2PUPU2Y и участвуй в розыгрыше 3-х NVIDIA® Jetson Nano Developer Kit для создания автономных устройств. Розыгрыш состоится 11 мая в 14.00.\nВнимание! Получить приз можно только лично, и стоит указать почту, с которой регистрировались на DataFest.\nУдачи!'
TEXT_JETSON_WIN = 'Поздравляем, вы выиграли NVIDIA Jetson Nano Developer Kit!\nНадеемся, с его помощью вы создадите нечто крутое😊 Если вдруг не знаете, с чего начать – к вашим услугам JetBot https://github.com/NVIDIA-AI-IOT/jetbot, open-source DIY проект, который поможет вам создать своего первого робота.\nЧтобы получить свой приз, подойдите пожалуйста в 14.30, сразу после начала обеденного перерыва на инфо-стойку'
TEXT_JETSON_NOT_SUCCEED ='Розыгрыш NVIDIA Jetson Nano Developer Kit уже прошел, и, к сожалению, в этот раз вы не выиграли.\nНо мы верим, что вам обязательно повезет на наших будущих мероприятиях. А пока что предлагаем вам посмотреть каталог вебинаров NVIDIA (https://www.nvidia.com/en-us/about-nvidia/webinar-portal/)\nнаверняка там найдется что-то интересное вам.\nБольшое спасибо за участие, остаемся на связи.'

# ZAGLUSHKA
TEXT_NOT_READY_YET = "В разработке. Мы оповестим о запуске!"
TEXT_WILL_BE_ON_DATAFEST = "Данный функционал будет включен 11 числа"

TEXT_BYE = 'До следующей встречи!'

TEXT_SHOW_SCHEDULE = "Актуальную информацию по программе мероприятия можно найти тут: https://datafest.ru/schedule/"
TEXT_SHOW_PATH_MORE_INFO = 'Больше информации на сайте конференции: https://datafest.ru/map/'
TEXT_SHOW_PATH_MAP_CAPTION = 'Выбирайте интересующие вас секции в программе и проходите к нужному залу'

# ADMIN
TEXT_BROADCAST_CHOOSE_GROUP = 'Выберите группу пользователей, кому предназначается сообщение'
TEXT_ENTER_BROADCAST = 'Введите сообщение или введите /cancel, чтобы вернуться назад.'
TEXT_BROADCAST_STARTED = 'Броадкаст запущен'
TEXT_BROADCAST_DONE = 'Броадкаст выполнен. {} отправлено. {} ошибок'
TEXT_CANCEL_BROADCASTING = 'Ну не надо, так не надо...'


TEXT_START_INVITE_REFRESH = 'Запущено обновление инвайтов.'
TEXT_REPORT_INVITE_COUNT = 'Инвайты обновлены, новых {}.'
TEXT_REPORT_NOTIFICATION_COUNT = 'Нотификации по инвайтам разосланы: {} штук.'
TEXT_REPORT_INVITE_REFRESH_ERROR = 'Ошибка обновления инвайтов.'
TEXT_INVITE_NOTIFICATION = 'Вы приглашены на датафест! Проверьте почту.'

TEXT_NOT_ADMIN = 'Доступно только админам. 👹'
TEXT_NOT_AUTHORIZED = "Доступно только авторизованным пользователям, авторизуйтесь в боте."
TEXT_FULL_BACK = 'Ok, вернемся обратно в меню, что будем делать?'
TEXT_UNKNOWN_COMMAND = "Пожалуйста, воспользуйтесь кнопками. 👇"

############# BUTTONS #############
# Main menu
BUTTON_CHECK_REGISTRATION = 'Проверить статус регистрации'
BUTTON_AUTHORISATION = 'Авторизоваться'
BUTTON_SCHEDULE = 'Программа феста'
BUTTON_NEWS = 'Новости феста'
BUTTON_SHOW_PATH = 'Как добраться / Карта'
BUTTON_JETSON = 'Я хочу Jetson!'

BUTTON_PARTICIPATE_IN_RANDOM_PRIZE = 'Участвовать в розыгрыше призов'
BUTTON_XS_SIZE = 'XS'
BUTTON_S_SIZE = 'S'
BUTTON_M_SIZE = 'M'
BUTTON_L_SIZE = 'L'
BUTTON_XL_SIZE = 'XL'
BUTTON_XXL_SIZE = 'XXL'
BUTTON_CHANGE_SIZE = 'Изменить размер'


BUTTON_RANDOM_BEER = 'Участвовать в Random beer'
BUTTON_ACCEPT_RULES = "Я согласен/согласна"
BUTTON_DECLINE_RULES = 'Нет, я против'
BUTTON_CHANGE_TG_NICK = 'Изменить Telegram nick'
BUTTON_CHANGE_ODS_NICK = 'Изменить ODS nick'
BUTTON_CHANGE_SN_LINK = 'Изменить Social network link'
BUTTON_FIND_MATCH = 'Найти партнера'
BUTTON_END_MEETING = 'Закончить встречу'


BUTTON_REFRESH_SCHEDULE = 'Обновить расписание'
BUTTON_SEND_INVITES = 'Разослать инвайты'
BUTTON_DRAW_PRIZES = 'Розыгрыш мерча'
BUTTON_START_DRAWING = 'Начать розыгрыш мерча'
BUTTON_POST_NEWS = 'Запостить новость'
BUTTON_NEWS_GROUP_WITH_SUBSCRIPTION = 'С подпиской на новости'
BUTTON_NEWS_GROUP_ADMIN = 'Админам'
BUTTON_NEWS_GROUP_WINNERS = 'Победителям'
BUTTON_NEWS_GROUP_ALL = 'Всем'
BUTTON_DRAW_JETSON = 'Разыграть Nvidia Jetson'

BUTTON_NEWS_SUBSCRIPTION = 'Подписаться на новости'
BUTTON_NEWS_UNSUBSCRIPTION = 'Отписаться от новостей'
BUTTON_GET_LAST_5_NEWS = 'Посмотреть новости'

BUTTON_REGISTRATION = 'Регистрация'
BUTTON_ON_MAJOR = 'Я на Major 💪'

BUTTON_FULL_BACK = 'Назад'
BUTTON_10_MAY_SCHEDULE = 'Расписание на 10 мая'
BUTTON_11_MAY_SCHEDULE = 'Расписание на 11 мая'

BUTTON_CHECK_EMAIL = 'Проверить Email'
