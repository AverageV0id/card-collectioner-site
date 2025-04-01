from models import User
from models import Card
from datetime import date


def add_card(message):
    text = message.text[7::]
    user = User.select().where((User.username == message.chat.username)).get()
    #  сделать проверку по логину на сайте ^^^
    new_card = Card(user=user, name=text)
    new_card.save()
    print(f'Карта получена: *{new_card.name}*')


def new_user(username):
    new_user = User(username=str(username),
                    date_register=date.today(), is_Admin=False)
    new_user.save()
    print(f'Новый пользователь, {new_user.username}, зарегестрирован')

