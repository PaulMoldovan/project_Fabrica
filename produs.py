import json

class Aparate_electrocasnice:
    """Aaceasta clasa contine date despre aparatele care se produc in fobrica"""
    creaza_aparate = 'Alege produsul dorit:'

    def __init__(self, numele, utilitate):
        self.numele = numele
        self.utilitate = utilitate

    def menu_aparate(self):
        print(self.creaza_aparate)
        menu = ['1. Construieste masina de spalat.', '2. Construeste cuptor-microunde', '3. Construieste frigider']
        for i in menu:
            print(i)
        optiune = input('Selecteaza produsul:\n> ')

        while True:
            if optiune == 1:
                pass
            if optiune == 2:
                pass
            if optiune == 3:
                pass
            else:
                continue




class Masina_de_spalat(Aparate_electrocasnice):
    """Constructie masina de spalat"""
    def __init__(self, data):
        super().__init__(data[0], data[1])
        self.capacitate = data[2]

    def constructie_masina_spalat(self):

        read_json = open('materiale.json', 'r')
        converted_json = json.load(read_json)
        read_json.close()
        materiale = converted_json.copy()
        masina =[]










