# kahoot-adil

Admin user:
Некоторый функции не доступны для обычного пользователя, поэтмоу ниже данные от суперюзера для админки

login: root
password: 123


Модели: 
Есть большая таблица quizzes в которая может содержать опроссники, в свою очередь каждый опроссник содержит некоторое количество вопросов.
Получается можно разные тесты делить по разным темам, например, создовать опроссник про Медицину, со своими характерными вопросами
или же составить опроссник про Авиацию, тоже со своими вопросами. 



Регистрация обычного игрока через пост:

	по следующему url - "https://kahootadil.herokuapp.com/api/v1/player/registration/"
	Пост запрос на регистрацию следует отправлять в следующей форме

{
    	"username": "aurora",
    	"first_name": "Aurora",
    	"last_name": "Snow",
    	"phone_number": 123,
    	"password": "123",
	"email": "abs@mail.ru"
}

Но так же можно просто перейти и заполнить форму от django rest_framework по тому же адресу 


Логин обычных пользователей по след. адресу:
"https://kahootadil.herokuapp.com/api/v1/login/"


Распределение баллов: 
	Адресс "https://kahootadil.herokuapp.com/getting/" обрабатывает post-запрос следующего вида:
	
	{
          "player_id": 14,
          "question_id": 1,
          "answer_id": 4,
          "players_answer": "Two",
          "time": 1
       }

	id учстника, который отвечает на вопрос, 
	id вопроса, на который отвечает участник,
	id ответа на вопрос, который отвечает,
	выбранный ответ участника на вопрос,
	время за которое участник ответил на вопрос
	
	В случае если было отвечено правильно, начисляются баллы в поле "final_score" и 
добавляется +1 к отвеченным вопросам



Расчет Ранга:
	При каждой отправке ответа алгоритмы написанные в файле "services.py" автоматически 
распределят места в рейтинге по отношению других участников так же будет расчитано 
какое количество опроссников было пройдено этим игроком и если найдется соответсвенно обновиться
поле "passed_tests" в базе игроков.

	Если данные не обновились можно пройти по следующему адресу: 
"https://kahootadil.herokuapp.com/refresh-data/"

Swagger: 
https://kahootadil.herokuapp.com/swagger/

