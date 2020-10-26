import json


class Menu:

    menu = 'Welcome\nLogin: '
    invalid_login = 'Invalid login'

    def login(self):
        file_angajati = open("lista_angajati.json", "r")
        angajati = json.load(file_angajati)
        file_angajati.close()
        tmp_list = []

        try:
            id = int(input(f'{self.menu}'))
        except:
            print('Incearca din nou')

        for angajat in angajati:
            tmp_list.append(angajati[angajat][2])
        if id not in tmp_list:
            print(f'{self.invalid_login}')
        else:
            for angajat in angajati:
                if id in angajati[angajat]:
                    return angajati[angajat]




