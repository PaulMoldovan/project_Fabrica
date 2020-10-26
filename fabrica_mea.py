import menu
import angajati


main_menu = menu.Menu()



while True:

    user = main_menu.login()

    if user[3] == 'manager':
        logged_user = angajati.Manager(user)
        logged_user.manager_menu()
        continue
    elif user[3] == 'operator':
        logged_user = angajati.Operator(user)
        logged_user.operator_menu()
        continue
    elif user[3] == 'administrator':
        logged_user = angajati.Administrator(user)
        logged_user.administrator_menu()
        continue


