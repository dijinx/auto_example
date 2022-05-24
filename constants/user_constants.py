# PROD страницы пользователя
USER_PROD_MAIN_PAGE = "https://estate.mts.ru/"
USER_PROD_AUTHORIZATION_PAGE = "https://login.mts.ru/amserver/UI/Login?client_id=MTS_Estate&goto=https%3A%2F%2Flogin.mts.ru%2Famserver%2Foauth2%2Frealms%2Froot%2Frealms%2Fusers%2Fauthorize%3Fclient_id%3DMTS_Estate%26redirect_uri%3Dhttps%253A%252F%252Festate.mts.ru%252Fapi%252Fv1%252Fcallback%26response_type%3Dcode%26scope%3Dprofile%2520email%2520sso%26state%3D94594343-aabf-4b69-a1bc-d0cc840f0d5b&realm=%2Fusers"
USER_PROD_MY_PROFILE_PAGE = "https://estate.mts.ru/profile/user"
USER_PROD_FAVORITES_PAGE = "https://estate.mts.ru/favorites"
USER_PROD_ORGANIZATION_PAGE = "https://estate.mts.ru/profile/organization"
USER_PROD_REQUEST_ORDERS = 'https://estate.mts.ru/requests/orders'
USER_PROD_REQUISITES = 'https://estate.mts.ru/profile/requisites'
# STAGE страницы модератора

# данные пользователя для авторизации(Пользователь_1)
# у пользователя должны быть заполнены все поля, загружены все доки
USER_AUTHORIZATION_PHONE_NUMBER = "9137802848"
USER_AUTHORIZATION_PASSWORD = "nhHhyPS6"

# данные пользователя для заполнения данных профиля
USER_DOCUMENT_NAME = "записки"
USER_FIO_FULL = "Горбунова Дмитрия Владимировича"
USER_POSITION = "председателя"
USER_LAST_NAME = "Горбунов"  # вносимое
USER_LAST_NAME_FOR_CHECK = "Горбунов"  # эталон для сравнения
USER_FIRST_NAME = "Дмитрий"  # вносимое
USER_FIRST_NAME_FOR_CHECK = "Дмитрий"  # эталон для сравнения
USER_SECOND_NAME = "Владимирович"  # вносимое
USER_SECOND_NAME_FOR_CHECK = "Владимирович"  # эталон для сравнения
USER_BIRTH_DATE = "27.10.2004"  # вносимое
USER_BIRTH_DATE_FOR_CHECK = "27.10.2004"  # эталон для сравнения
USER_MAIL = "01.01.test@mail.ru"  # вносимое
USER_MAIL_FOR_CHECK = "01.01.test@mail.ru"  # эталон для сравнения
USER_ADDRESS = "г. Москва, ул. Хуторская 2-я, д. 38А, стр. 26"  # вносимое
USER_ADDRESS_FOR_CHECK = "г. Москва, ул. Хуторская 2-я, д. 38А, стр. 26"  # эталон для сравнения

# данные пользователя для регистрации пользователя(Пользователь_2)
USER_REGISTRATION_PHONE_NUMBER = "9965445373"
USER_REGISTRATION_PASSWORD = "nhHhyPS6"
USER_REGISTRATION_MAIL = "01.01.test@mail.ru"

# данные пользователя для регистрации организации пользователя(Пользователь_3)
USER_PROFILE_AND_REQUISITES_REGISTRATION_PHONE_NUMBER = "9965455014"
USER_PROFILE_AND_REQUISITES_REGISTRATION_PASSWORD = "nhHhyPS6"
USER_PROFILE_AND_REQUISITES_REGISTRATION_MAIL = "01.01.test@mail.ru"

# кадастровые номера пользователя
USER_CADASTRAL_NUMBER_0 = "77:01:0004015:1020"
USER_CADASTRAL_NUMBER_0_ADDRESS = "Россия, Москва, Лесная улица, 10-16"
USER_CADASTRAL_NUMBER_0_PRICE = "175 855 322,24"
# ----------------------------------------------------------------------------------------------------
USER_CADASTRAL_NUMBER_1 = "1"

# ----------------------------------------------------------------------------------------------------
USER_CADASTRAL_NUMBER_2 = ""

# ----------------------------------------------------------------------------------------------------
# данные пользователя для заполнения платёжных реквизитов
USER_REQUISITES_NAME = "Акционерное общество «Тинькофф Банк»"
USER_REQUISITES_BIK = "044525974"
USER_REQUISITES_BANK_NAME = "АО «Тинькофф Банк»"
USER_REQUISITES_ADDRESS = "Москва, 127287, ул. Хуторская 2-я, д. 38А, стр. 26;а/я 23, г. Москва, 102001"
USER_REQUISITES_KS = "30101810145250000974"
USER_REQUISITES_RS = "30232810100000000004"
USER_REQUISITES_IS_SAVE_PUSH_TEXT = "Реквизиты были добавлены."
USER_REQUISITES_IS_DELETE_PUSH_TEXT = "1"

# тексты пушей и сообщений для пользователя
USER_REQUEST_IS_SEND = "Мы отправим счет в течение 1-го рабочего дня"
USER_REQUEST_SUCCESSFULLY_ACCEPTED = "Ваше заявление успешно принято!"
# даты и номера доверенностей
USER_JUDICIAL_PRESENTATION_NUMBER = '1'
USER_JUDICIAL_PRESENTATION_DATE = '01.06.2021'
USER_REPRESENTATION_OR_STATUTE_NUMBER = '2'
USER_REPRESENTATION_OR_STATUTE_DATE = '02.06.2021'
USER_INNING_DOCUMENTATION_IN_INSTANCE_NUMBER = '3'
USER_INNING_DOCUMENTATION_IN_INSTANCE_DATE = '03.06.2021'

# файлы для загрузки пользователем
USER_INNING_DOCUMENTATION_IN_INSTANCE_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\доверенность на подачу документов в инстанции.pdf'
USER_REPRESENTATION_OR_STATUTE_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\доверенность на вашего представителя или устав.pdf'
USER_JUDICIAL_PRESENTATION_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\доверенность на судебное представительство.pdf'
USER_DECISION_OF_THE_COMMISSION_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\Решение комиссии (при наличии).pdf'
USER_ECP_FOR_STATEMENT_TO_THE_COMMISSION_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\ЭЦП к заявлению в комиссию (при наличии).sig'
USER_STATEMENT_TO_THE_COMMISSION_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\Заявление в комиссию (при наличии).pdf'
USER_ESTABLISHING_DOCUMENT_ON_OBJECT_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\Правоустанавливающий документ на объект.pdf'
USER_MARKET_PRICE_REPORT_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\Отчёт_о_рыночной_оценке(тестовый).pdf'
USER_SIGN_1_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\ЭЦП №1 к отчету о рыночной оценке (при наличии).sig'
USER_SIGN_2_FILE = r'C:\ru.estate.prod.autotests\resources\user_docs\ЭЦП №2 к отчету о рыночной оценке (при наличии).sig'
USER_ORG_DOCUMENT_ARCHIVE = r'C:\ru.estate.prod.autotests\resources\user_docs\Документы подтверждающие представительство организации.rar'

# файлы для загрузки модератором
MODER_EXTRACT_FROM_EGRN_CADASTRAL_VALUE = r'C:\ru.estate.prod.autotests\resources\user_docs\Выписка_из_ЕГРН_о_кадастровой_стоимости.pdf'
MODER_ECP_FOR_EXTRACT_FROM_EGRN_CADASTRAL_VALUE = r'C:\ru.estate.prod.autotests\resources\user_docs\ЭЦП_к_выписке_из_ЕГРН_о_кадастровой_стоимости_(при наличии).sig'

# данные реквизитов компании пользователя 9137802848 отображаемые в заказе у модератора
USER_ORG_TYPE_OF_OWNERSHIP = "Тип владения: НАО"
USER_ORG_LEGAL_NAME = "Юридическое наименование: ТИНЬКОФФ БАНК"
USER_ORG_INN = "ИНН: 7710140679"
USER_ORG_KPP = "КПП: 773401001"
USER_ORG_OKTMO = "ОКТМО: 45344000"
USER_ORG_OKATO = "ОКАТО: 45277586000"
USER_ORG_OGRN = "ОГРН: 1027739642281"
USER_ORG_PHONE = "Телефон: +7 (913) 780-28-48"
USER_ORG_MAIL = "Email: 01.01.test@mail.ru"

# данные юридического адреса компании пользователя 9137802848 отображаемые в заказе у модератора
USER_ORG_JUDICIAL_INDEX = "Индекс: 123060"
USER_ORG_JUDICIAL_AREA = "Область: Москва"
USER_ORG_JUDICIAL_CITY = "Город: Москва"
USER_ORG_JUDICIAL_STREET = "Улица: 1-й Волоколамский проезд"
USER_ORG_JUDICIAL_HOUSE = "Дом: д. 10, стр. 1"
USER_ORG_JUDICIAL_OFFICE = "Офис: 1"

# данные фактического адреса компании пользователя 9137802848 отображаемые в заказе у модератора
USER_ORG_ACTUAL_INDEX = "Индекс: 123060"
USER_ORG_ACTUAL_AREA = "Область: Москва"
USER_ORG_ACTUAL_CITY = "Город: Москва"
USER_ORG_ACTUAL_STREET = "Улица: 1-й Волоколамский проезд"
USER_ORG_ACTUAL_HOUSE = "Дом: д. 10, стр. 1"
USER_ORG_ACTUAL_OFFICE = "Офис: 1"

# данные текущей компании пользователя 9137802848 отображаемые в заказе у модератора
USER_DATA_IN_REQUEST_FIO = "Горбунов Дмитрий Владимирович"
USER_DATA_IN_REQUEST_EMAIL = "01.01.test@mail.ru"
USER_DATA_IN_REQUEST_PHONE = "9137802848"
USER_DATA_IN_REQUEST_BIRTHDAY = "01.09.1981"
USER_DATA_IN_REQUEST_ADDRESS = "1"
USER_DATA_IN_REQUEST_ORG_ACTUAL_NAME = "НАО \"ТИНЬКОФФ БАНК\""

# данные для редактирования организации
USER_ORG_TYPE_OWNERSHIP = 'НАО'
USER_CHECK_ORG_LEGAL_NAME = "ТИНЬКОФФ БАНК"
USER_CHECK_ORG_INN = '7710140679'
USER_CHECK_ORG_KPP = '773401001'
USER_CHECK_ORG_OGRN = '1027739642281'
USER_CHECK_ORG_OKTMO = '45344000'
USER_CHECK_ORG_OKATO = '45277586000'
USER_CHECK_ORG_PHONE = '+7 (913) 780-28-48'
USER_CHECK_ORG_MAIL = '01.01.test@mail.ru'
USER_ORG_CITY = 'Москва'
USER_ORG_INDEX = '127287'
USER_ORG_STREET = 'Хуторская 2-я'
USER_ORG_HOUSE = '38А'
USER_ORG_OFFICE = '1'
USER_ORG_REG_MAIL = '01.01.test@mail.ru'

