from Class_Tp_link_2600 import Tp_link_2600
from Class_GUI import main_window
import transliterate
import threading
from threading import Thread
from tkinter import *
'''В планах реализовать:
                        Запуск графической программы
                        Получение вводимых данных
                        Запуск класса Class_Tp_link_2600
                        Сделать так, чтобы в графическом окне отображались проценты выполнения и параллельно
                        Выполнялась прошивка коммутатора.
    На данном этапе, при отображении процентов в графическом окне, поток блокируется и прошивка коммутатора начинается
    только когда когда закрываются все графические окна'''
def main():

    window = main_window()

    Tp_link = Tp_link_2600(Addres=window.data['Addres'], Ip_addres=window.data['Ip_addres'],
                          Gateway=window.data['Gateway'], Mask=window.data['Mask'],
                          Vlan_manege=window.data['Vlan_manage'],
                          Number_switch=window.data['Number_switch'])
    Tp_link.run_proshivka()

if __name__ == '__main__':
    main()