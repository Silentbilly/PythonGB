def get_user_data(**kwargs):
    print(kwargs, sep=" ")


def main():
    user_data = {'name': 'Akex', 'surname': 'Johnson', 'birth_year': 1988, 'city': 'Wroclaw', 'tel': '+345678910'}
    get_user_data(**user_data)


if __name__ == "__main__":
    main()
