# Учебный проект "Foodgram"

##  Приложение «Продуктовый помощник».

На сайте пользователи могут разместить рецепт, подписаться на пользователя и просто просматривать рецепты.
При регистрации пользователь указывает свой email, который будет использоваться при авторизации.
Проект реализован на Django REST Framework.

## Как локально запустить проект:

Клонировать репозиторий и перейти в папку /infra/:

```
git clone git@github.com:Vorontsov39/foodgram-project-react.git
cd infra
```

Создайте файл .env командой touch .env и добавьте в него переменные окружения для работы с базой данных:

```
SECRET_KEY=<ваш_django_секретный_ключ>
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Вы можете сгенерировать DJANGO_SECRET_KEY. Из директории проекта /backend/ выполнить:

```
python manage.py shell
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()

Полученный ключ скопировать в файл .env.
```

Скопируйте файлы docker-compose.yml, nginx.conf и .env из папки /infra/ на Ваш виртуальный сервер:

```
scp <название файла> <username>@<server_ip>:/home/<username>/
```

Далее зайдите на виртуальный сервер и подготовьте его к работе с проектом:

```
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
sudo apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh 
sudo apt install docker-compose
```
Разворачиваем проект с помощью Docker используя контейнеризацию:


```
sudo docker-compose up -d --build
```


Осталось выполнить миграции, подключить статику, создать профиль админастратора:

```
sudo docker exec -it <name или id контейнера backend> python manage.py migrate
sudo docker exec -it <name или id контейнера backend> python manage.py collectstatic
sudo docker exec -it <name или id контейнера backend> python manage.py createsuperuser
```

И финально загрузить спискок ингридиентов:

```
sudo docker exec -it <name или id контейнера backend> python manage.py loadjson --path "recipes/data/ingredients.json"
```
Сайт доступен по адресу:
http://51.250.92.99/
