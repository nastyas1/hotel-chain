# Hotel Chain

## Введение
Созданный сайт поможет людям забронировать номер в отеле, принадлежащему сети ApartLux. После регистрации/входа в личный кабинет, на главной страннице будет высвечено нахождение 5 отелей. Пользователь может выбрать любой для своего проживания. После того, как отель будет определен, пользователь попадет на страницу для выбора номера и даты проживания в нем, эти данные будут сохранены в базу данных. В личном кабинете можно будет аннулировать бронь.

## Написанные классы(в будущем)
- User
- Hotel
- HotelNumber
- UserResource
- HotelResourse
- HotelNumberResource

## Структура базы данных
В базе данных хранятся три таблицы: `user`,  `hotel_number` и `hotel`

В таблице `user` храниться:
- user_id(primary key)
- name
- email
- about
- password
- created_date
- hotel_number_id(foreign key)

В таблице `hotel` храниться:
- hotel_id(primary key)
- name
- coordinate

В таблице `hotel_number` храниться:
- hotel_number_id(primary key)
- number
- free_time
- hotel_id(foreign key)

