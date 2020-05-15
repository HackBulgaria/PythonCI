from project.bootstrap import bootstrap
from project.services import create_user, get_last_user


def main():
    bootstrap()

    create_user(name='ed')
    user = get_last_user()

    print(user)


if __name__ == '__main__':
    main()
