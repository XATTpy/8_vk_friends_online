import vk
from getpass import getpass


APP_ID = 7034982
API_VERSION =  5.95


def get_user_login():
    return input("Введите телефон или email для vk.com: ")


def get_user_password():
    return getpass(prompt="Введите пароль для vk.com: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session, v=API_VERSION)
    frineds_online_id = api.friends.getOnline()
    frineds_online = api.users.get(user_ids=frineds_online_id)
    return frineds_online


def output_friends_to_console(friends_online):
    friends_count = len(friends_online)
    if friends_count > 0:
        print("{} друзей онлайн:".format(friends_count))
        for friend in friends_online:
            first_name = friend.get("first_name")
            last_name = friend.get("last_name")
            print(first_name+" "+last_name)
    else:
        print("Нет друзей онлайн :(")


if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()

    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        quit("Данные введены неверно.")

    output_friends_to_console(friends_online)
