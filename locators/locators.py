from selenium.webdriver.common.by import By

class MainPageLocators:
    FAQ = By.XPATH, "//div[contains(@class, 'Home_FAQ_')]"  # Раздел "Вопросы о важном"
    Questions = By.XPATH, "//div[contains(@class, 'accordion__item')]"  # Вопросы
    Answer = By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]"  # Отображаемый ответ
    Cookie_button = By.XPATH, "//button[contains(@class, 'App_CookieButton_')]"  # Кнопка "Да все привыкли"
    Scooter_logo = By.XPATH, "//*[@alt='Scooter']"  # Логотип "Самокат"
    Yandex_logo = By.XPATH, "//*[@alt='Yandex']"  # Логотип "Яндекс"

class OrderPageLocators:
    Name_field_locator = By.XPATH, "//input[@placeholder='* Имя']"  # Поле ввода имени
    Lastname_field_locator = By.XPATH, "//input[@placeholder='* Фамилия']"  # Поле ввода фамилии
    Order_button = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"  # Кнопка "Заказать"
    Next_button = By.XPATH, "//button[text()='Далее']"  # Кнопка "Далее"
    Address_field = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # Поле ввода адреса
    Station_field = By.XPATH, "//input[@placeholder='* Станция метро']"  # Поле выбора метро
    Station_dropdown = By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li"  # Список метро
    Phone_number_field = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # Поле ввода номера
    Comment_field = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # Поле комментария
    Confirm = By.XPATH, "//div[text()='Хотите оформить заказ?']"  # Диалог подтверждения
    Yes_button = By.XPATH, "//button[text()='Да']"  # Кнопка "Да"
    Date_field = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # Поле ввода даты
    Black_checkbox = By.ID, "black"  # Черный цвет
    Grey_checkbox = By.ID, "grey"  # Серый цвет
    Rental_period = By.XPATH, "//div[@class='Dropdown-root']"  # Поле срока аренды
    Rental_period_dropdown = By.XPATH, "//div[@class='Dropdown-menu']"  # Периоды
    Order_completed = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"  # Информация о заказе
    Order_status_button = By.XPATH, "//button[text()='Посмотреть статус']"  # Кнопка "Посмотреть статус"
    One_day = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='сутки')]"  # День
    Two_day = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='двое суток')]"  # Два дня
    Rent_form = By.XPATH, "//div[text()='Про аренду']"  # Раздел "Про аренду"
    Order_button_in_footer = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"  # Кнопка "Заказать" на странице
    Order_button_in_header = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']"  # Кнопка "Заказать" в шапке