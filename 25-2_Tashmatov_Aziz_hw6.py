import re

print('1 - Считать имена и фамилии, 2 - Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход')
while True:
    try:
        user_input = int(input('введите команду: '))
    except:
        print('1 - Считать имена и фамилии, 2 - Считать все емайлы, 3 - Считать названия файлов,'
              ' 4 - Считать цвета, 5 - Выход')
        continue
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        cont = file.read()
        color_list = re.findall(r"#[a-z0-9]{6}", cont)
        # print(f'{len(color_list)}\n{color_list}')
        file_list = re.findall(r"[A-Z][A-Za-z]*\.[a-z0-9]+", cont)
        # print(f'{len(file_list)}\n{file_list}')
        email_list = re.findall(r"[a-z0-9]+@[a-z.0-9-]+", cont)
        # print(f'{len(email_list)}\n{email_list}')
        name_list = re.findall(r"[A-Z][a-z-]+\s+[A-Za-d][A-Za-z- O']+", cont)
        # print(f'{len(name_list)}\n{name_list}')
        if user_input == 4:
            with open('color.txt', 'w') as color_file:
                color_file.write(f'{len(color_list)}\n{color_list}')
        elif user_input == 2:
            with open('email.txt', 'w') as email_file:
                email_file.write(f'{len(email_list)}\n{email_list}')
        elif user_input == 3:
            with open('file.txt', 'w') as file_file:
                file_file.write(f'{len(file_list)}\n{file_list}')
        elif user_input == 1:
            with open('name.txt', 'w') as name_file:
                name_file.write(f'{len(name_list)}\n{name_list}')
        elif user_input == 5:
            break
        else:
            print('1 - Считать имена и фамилии, 2 - Считать все емайлы, 3 - Считать названия файлов,'
                  ' 4 - Считать цвета, 5 - Выход')