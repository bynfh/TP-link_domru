import transliterate
from tkinter import *
import time
'''Класс для создания окна, в котором будут вводиться данные.
   Далее, при нажатии кнопки "Прошить!!!" введенные данные правятся и импортируются в data.
   Убивается главное окно, создается новое, вызовом функции mainWindow2.
   В функции mainWindow2 в окне которого планируется реализовать вывод Для ИНФОРМИРОВАНИЯ пользователя'''
class main_window():
    root = Tk()

    data = {'Addres': '', 'Ip_addres': '',
              'Gateway': '', 'Mask': '',
              'Vlan_manage': '', 'Number_switch': ''}

    def __init__(self):


        def butCallback():

            self.data['Addres'] = field_1.get()
            self.data['Ip_addres'] = field_2.get()
            self.data['Gateway'] = field_3.get()
            self.data['Mask'] = field_4.get()
            self.data['Vlan_manage'] = field_5.get()
            self.data['Number_switch'] = field_7.get()

            self.edit_input_data()
            self.root.destroy()
            self.root = Tk()
            self.mainWindow2()


        self.root.title('Прошиватор TP-Link-2600')
        self.root.geometry('655x180+300+200')
        self.root.resizable(False, False)
        self.root.grab_set()

        Hostname = Label(self.root, text="Имя коммутатора")
        Hostname.grid(column=0, row=0)

        field_1 = Entry(self.root, width=50)
        field_1.grid(column=1, row=0)
        btn_proshivka = Button(self.root, text="Прошить!!!", command=butCallback)
        btn_proshivka.grid(column=2, row=0)

        Ip_adres = Label(self.root, text="Ip адрес")
        Ip_adres.grid(column=0, row=1)
        field_2 = Entry(self.root, width=50)
        field_2.grid(column=1, row=1)

        Gateway = Label(self.root, text="Шлюз")
        Gateway.grid(column=0, row=2)
        field_3 = Entry(self.root, width=50)
        field_3.grid(column=1, row=2)

        Mask = Label(self.root, text="Маска сети")
        Mask.grid(column=0, row=3)
        field_4 = Entry(self.root, width=50)
        field_4.grid(column=1, row=3)

        Vlan_manage = Label(self.root, text="Vlan управления")
        Vlan_manage.grid(column=0, row=4)
        field_5 = Entry(self.root, width=50)
        field_5.grid(column=1, row=4)

        Number = Label(self.root, text="Номер коммутатора")
        Number.grid(column=0, row=6)
        field_7 = Entry(self.root, width=50)
        field_7.grid(column=1, row=6)

        info = Label(self.root, text="ИНФО \n при нажатии (прошить) \n ждите 3 минуты.")
        info.grid(column=2, row=2)
        self.root.mainloop()


    def mainWindow2(self, *w, **kw):
        def butCallback():
            self.root.destroy()
            self.root = Tk()
            self.__init__()


        self.root.title('ИНФО о выполнении программы')
        self.root.geometry('655x180+300+200')
        self.root.resizable(False, False)
        self.root.grab_set()

        but1 = Button(self.root, text="Выполнение завершено \n вернуться к главному окну", command=butCallback)
        but1.grid(column=1, row=1)
        for i in range(201):

            vuvod = str((i * 100) / 200)
            INFO = Label(self.root, text=vuvod + ' %')
            INFO.grid(column=0, row=0)
            INFO.update()
            # time.sleep(1)




    def edit_input_data(self):

        Addres = transliterate.translit(self.data['Addres'], reversed=True)
        Addres = Addres.strip()
        Addres = re.sub(r"\.+|,+|\s+", '-', Addres)
        Addres = re.sub(r"-+DSh",'_DSH', Addres)
        Addres = re.sub(r"-+PSh", '_PSH', Addres)
        Addres = re.sub(r"-+", '-', Addres)

        Ip_addres = self.data['Ip_addres']
        Ip_addres = Ip_addres.strip()

        Gateway = self.data['Gateway']
        Gateway = Gateway.strip()

        Mask = self.data['Mask']
        Mask = Mask.strip()

        Vlan_manege = self.data['Vlan_manage']
        Vlan_manege = Vlan_manege.strip()

        Number_switch = self.data['Number_switch']
        Number_switch = Number_switch.strip()

        self.data['Addres'] = Addres
        self.data['Ip_addres'] = Ip_addres
        self.data['Gateway'] = Gateway
        self.data['Vlan_manage'] = Vlan_manege
        self.data['Number_switch'] = Number_switch
