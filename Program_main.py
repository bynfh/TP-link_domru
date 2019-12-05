from Class_Tp_link_2600 import Tp_link_2600
import transliterate
from tkinter import *
def main():

    root = Tk()
    root.title('Прошиватор TP-Link-2600')
    root.geometry('500x155+300+200')
    root.resizable(False, False)
    root.grab_set()

    def edit_input_data():


        Addres = transliterate.translit(field_1.get(), reversed=True)
        Addres = Addres.strip()
        Addres = re.sub(r"\.+|,+|\s+", '-', Addres)
        Addres = re.sub(r"-+DSh",'_DSH', Addres)
        Addres = re.sub(r"-+PSh", '_PSH', Addres)

        Ip_addres = field_2.get()
        Ip_addres = Ip_addres.strip()

        Gateway = field_3.get()
        Gateway = Gateway.strip()

        Mask = field_4.get()
        Mask = Mask.strip()

        Vlan_manege = field_5.get()
        Vlan_manege = Vlan_manege.strip()

        Other_vlan = field_6.get()
        Other_vlan = Other_vlan.strip()

        Number_switch = field_7.get()
        Number_switch = Number_switch.strip()

        run_main_block(Addres, Ip_addres, Gateway,
                       Mask, Vlan_manege, Other_vlan,
                       Number_switch)

    def run_main_block(Addres, Ip_addres, Gateway,
                       Mask, Vlan_manege, Other_vlan,
                       Number_switch):


        Tp_link = Tp_link_2600(Addres=Addres, Ip_addres=Ip_addres,
                               Gateway=Gateway, Mask=Mask,
                               Vlan_manege=Vlan_manege, Other_vlan=Other_vlan,
                               Number_switch=Number_switch)


        Tp_link.run_proshivka()

    Hostname = Label(root, text="Имя коммутатора")
    Hostname.grid(column=0, row=0)
    field_1 = Entry(root, width=50)
    field_1.grid(column=1, row=0)
    btn_proshivka = Button(root, text="Прошить!!!", command= edit_input_data)
    btn_proshivka.grid(column=2, row=0)

    Ip_adres = Label(root, text="Ip адрес")
    Ip_adres.grid(column=0, row=1)
    field_2 = Entry(root, width=50)
    field_2.grid(column=1, row=1)

    Gateway = Label(root, text="Шлюз")
    Gateway.grid(column=0, row=2)
    field_3 = Entry(root, width=50)
    field_3.grid(column=1, row=2)

    Mask = Label(root, text="Маска сети")
    Mask.grid(column=0, row=3)
    field_4 = Entry(root, width=50)
    field_4.grid(column=1, row=3)

    Vlan_manage = Label(root, text="Vlan управления")
    Vlan_manage.grid(column=0, row=4)
    field_5 = Entry(root, width=50)
    field_5.grid(column=1, row=4)

    Other_vlan = Label(root, text="Все vlan")
    Other_vlan.grid(column=0, row=5)
    field_6 = Entry(root, width=50)
    field_6.grid(column=1, row=5)

    Number = Label(root, text="Номер коммутатора")
    Number.grid(column=0, row=6)
    field_7 = Entry(root, width=50)
    field_7.grid(column=1, row=6)


    root.mainloop()
if __name__ == '__main__':
    main()
