all foreign keys:  
table Автомобиль table Владелец - PK
table Владелец table Стоимость - Владелец
table Стоимость table Класс - Владелец
table Класс table Налог - Владелец
table Налог table Дистрибьютор - Модель/авто
table Дистрибьютор table Двигатель - Марка/модель
table Двигатель table Производитель - Модель
table Производитель table Цвет - Модель
table Цвет table Тип кузова - Модель

Аномалию заметил в таблицне дистрибьютор, можно обьединить три автомобиля БМВ в одну строчку по адресу ул. Зорге, 17, Москва, Россия