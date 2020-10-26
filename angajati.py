import json
import produs


# aparate = produs.Aparate_electrocasnice
# menu_aparate = aparate.menu_aparate()


class Angajat:
    """Clasa aceasta contine informatii despre angajatii unei fabrici"""

    stelute = '*' * 40

    def __init__(self, prenume, nume, id, functie):
        self.prenume = prenume
        self.nume = nume
        self.id = id
        self.functie = functie
        self.welcome_message = f'Bine ai venit {self.nume} {self.prenume} <{self.id}>'

    def fullname(self):
        full_name = f'Nume angajat: {self.nume} {self.prenume}'
        return full_name


class Manager(Angajat):
    """Clasa aceasta contine date despre Manager"""

    mesaj_adaugare = 'Adauga un angajat:'
    mesaj_stergere = 'Sterge un angajat:'
    mesaj_modificare = 'Modifica calificare:'

    def __init__(self, data):
        super().__init__(data[0], data[1], data[2], data[3])

    def manager_menu(self):
        print(self.welcome_message)

        menu = ['1. Vizualizeaza lista angajati', '2. Adauga angajat', '3. Sterge angajat din lista',
                '4. Modifica calificare', '5. Exit']
        while True:
            for i in menu:
                print(i)
            try:
                optiune = int(input('Alege o optiune:\n> '))
            except:
                print('Optiunea introdusa este incorecta')
                continue
            if optiune == 1:
                self.lista_angajati()
            elif optiune == 2:
                self.add_muncitor()
            elif optiune == 3:
                self.sterge_angajat()
            elif optiune == 4:
                self.modifica_calificare()
            else:
                print('Ai ales sa iesi din program')
                break

    def add_muncitor(self):

        print(self.mesaj_adaugare)

        prenume = input('Prenume:\n> ')
        nume = input('Nume:\n> ')
        id = int(input('ID:\n> '))
        functie = input('Functie:\n> ')
        calificare = input('Calificare:\n> ')

        muncitor = [prenume, nume, id, functie, calificare]

        file_angajati = open('lista_angajati.json', 'r')
        angajatii_firmei = json.load(file_angajati)
        file_angajati.close()

        angajatii_firmei[len(angajatii_firmei) + 1] = muncitor
        file_angajati = open('lista_angajati.json', 'w')
        file_angajati.write(json.dumps(angajatii_firmei, indent=4))

        print('Adaugat cu succes!')

    def lista_angajati(self):

        read_json = open('lista_angajati.json', 'r')
        converted_json = json.load(read_json)
        read_json.close()

        for i in converted_json:
            lista = f' {i}. {converted_json[i][0]} {converted_json[i][1]} - {converted_json[i][3]}'
            print(lista)
        print(self.stelute)

    def sterge_angajat(self):

        print(self.mesaj_stergere)
        read_json = open('lista_angajati.json', 'r')
        converted_json = json.load(read_json)
        read_json.close()
        angajati = converted_json.copy()

        for i in converted_json:
            print(f' {i}. {converted_json[i][0]} {converted_json[i][1]} - {converted_json[i][3]}')
        deleted_user = input('> ')
        for angajat in angajati:
            if angajat == deleted_user:
                converted_json.pop(angajat)

        read_json = open('lista_angajati.json', 'w')
        read_json.write(json.dumps(converted_json, indent=4))
        read_json.close()

        print('Angajat sters din lista')

    def modifica_calificare(self):
        print(self.mesaj_modificare)

        read_json = open('lista_angajati.json', 'r')
        converted_json = json.load(read_json)
        read_json.close()
        angajati = converted_json.copy()

        for i in converted_json:
            print(f' {i}. {converted_json[i][0]} {converted_json[i][1]} - {converted_json[i][3]} - {converted_json[i][4]}')
        user_modificat = input('Alege angajatul:\n> ')
        noua_calificare = input('Introdu noua calificare:\n> ')
        for angajat in angajati:
            if angajat == user_modificat:
                angajati[angajat][4] = noua_calificare

        read_json = open('lista_angajati.json', 'w')
        read_json.write(json.dumps(converted_json, indent=4))
        read_json.close()
        print('Calificare modificata.')
        print(self.stelute)


class Operator(Angajat):
    stoc = 'Materiale:'
    #aparate = produs.Aparate_electrocasnice
    # menu_aparate = aparate.menu_aparate()


    def __init__(self, data):
        super().__init__(data[0], data[1], data[2], data[3], )
        self.calificare = data[4]



    def operator_menu(self):
        print(self.welcome_message)

        menu = ['1. Creaza produs', '2. Verifica stoc materiale', '3. Exit']
        for i in menu:
            print(i)
        while True:


            try:
                optiune = int(input('Alege o optiune:\n> '))
            except:
                print('Optiunea introdusa este incorecta')
                continue

            if optiune == 3:
                print('Exit...')
                break
            elif optiune == 2:
                self.verifica_stoc()
            elif optiune not in range(len(menu)):
                print('Optiunea introdusa este incorecta')
            elif optiune == 1:
                pass

            else:
                continue

    def verifica_stoc(self):
        print(self.stoc)
        print(self.stelute)

        read_json = open('materiale.json', 'r')
        materiale = json.load(read_json)
        read_json.close()

        for i in materiale:
            print(f'{i} - {materiale[i]}')
        print(self.stelute)







class Administrator(Angajat):
    adauga_materiale = 'Adauga materiale:'
    adauga_cantitate = 'Cantitate materiale:'
    stoc = 'Materiale:'

    def __init__(self, data):
        super().__init__(data[0], data[1], data[2], data[3])
        self.calificare = data[4]

    def administrator_menu(self):
        print(self.welcome_message)
        menu = ['1. Adauga materiale', '2. Verifica stoc materiale', '3.Exit']
        for i in menu:
            print(i)

        while True:

            try:
                optiune = int(input('Alege o optiune:\n> '))
            except:
                print('Optiunea introdusa este incorecta')
                continue
            if optiune == 3:
                print('Exit...')
                break
            elif optiune not in range(len(menu)):
                print('Optiunea introdusa este incorecta')
            elif optiune == 1:
                self.adauga_material()
            elif optiune == 2:
                self.verifica_stoc()
            else:
                continue


    def adauga_material(self):

        #print(self.adauga_materiale)

        read_json = open('materiale.json', 'r')
        lista_materiale = json.load(read_json)
        read_json.close()
        materiale = lista_materiale.copy()
        for material in materiale:
            print(f'{material} - {materiale[material]}')

        material_adaugat = input(f'{self.adauga_materiale}\n> ')
        cantitate_material = input(f'{self.adauga_cantitate}\n> ')

        materiale[material_adaugat] = cantitate_material

        file = open('materiale.json', 'w')
        file.write(json.dumps(materiale, indent=4))
        file.close()
        print('Materiale si cantitati adaugate')

    def verifica_stoc(self):
        print(self.stoc)
        print(self.stelute)

        read_json = open('materiale.json', 'r')
        materiale = json.load(read_json)
        read_json.close()

        for i in materiale:
            print(f'{i} - {materiale[i]}')
        print(self.stelute)
