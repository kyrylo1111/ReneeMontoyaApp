from control.controller import Controller


if __name__ == '__main__':
    while True:
        print(
        "Choose a menu item by number: \n" +
        "1. Add new Plant \n" +
        "2. Add new Employee \n" +
        "3. Get plant by id \n" +
        "4. Get employee by id \n" +
        "5. Add new salon \n" +
        "6. Get salon by id \n"
        )

        menu_flag = int(input("Your choose: "))
        getd = Controller

        if menu_flag == 1:
            getd.addplant()
        elif menu_flag == 2:
            getd.addemployee()
        elif menu_flag == 3:
            getd.getplant()
        elif menu_flag == 4:
            getd.getemployee()
        elif menu_flag == 5:
            getd.addsalon()
        elif menu_flag == 6:
            getd.getsalon()
