import win32file
import time
import os
import asyncio
'''Класс для интерпритирования данных и отправки их через COM port(serial port) на коммутатор для его настройки.
   Открываются два файла и с текстом для прошивки и с конфигом. Они правятся и отправляются на коммутатор.
   Так же создаются два файла для отслеживания вводимой информации.
   НА данном этапе закоменчена отправка на коммутатор, необходимо доделать,
   чтобы данные корректно формировались для отправки'''
class Tp_link_2600():
    input_ = {'Addres': '', 'Ip_addres': '',
              'Gateway': '', 'Mask': '',
              'Vlan_manage': '', 'Number_switch': ''}
    Config = []
    Proshivka = []
    convert_masks = {'1': '128.0.0.0', '2': '192.0.0.0', '3': '224.0.0.0',
                     '4': '240.0.0.0', '5': '248.0.0.0', '6': '252.0.0.0',
                     '7': '254.0.0.0', '8': '255.0.0.0', '9': '255.128.0.0',
                     '10': '255.192.0.0', '11': '255.224.0.0', '12': '255.240.0.0',
                     '13': '255.248.0.0	', '14': '255.252.0.0', '15': '255.254.0.0',
                     '16': '255.255.0.0', '17': '255.255.128.0', '18': '255.255.192.0',
                     '19': '255.255.224.0', '20': '255.255.240.0', '21': '255.255.248.0',
                     '22': '255.255.252.0', '23': '255.255.254.0', '24': '255.255.255.0',
                     '25': '255.255.255.128', '26': '255.255.255.192', '27': '255.255.255.224',
                     '28': '255.255.255.240', '29': '255.255.255.248', '30': '255.255.255.252',
                     '31': '255.255.255.254', '32': '255.255.255.255'}

    def __init__(self, Addres, Ip_addres, Gateway,
                 Mask, Vlan_manege, Number_switch):

        self.input_['Addres'] = Addres
        self.input_['Ip_addres'] = Ip_addres
        self.input_['Gateway'] = Gateway
        if Mask in self.convert_masks:

            self.input_['Mask'] = self.convert_masks[Mask]
        else:
            self.input_['Mask'] = Mask
        self.input_['Vlan_manage'] = Vlan_manege
        self.input_['Number_switch'] = Number_switch

    def open_file(self):
        conf = []
        with open('CONFIG_TP_Link_2600.txt', 'r') as g:
            for line in g:
                conf.append(line)
        self.Config = conf

        proshivka = []
        with open('FOR_PROSHIVKA.txt', 'r') as e:
            for line in e:
                proshivka.append(line)
        self.Proshivka = proshivka

    def create_file(self):

        name_file = self.input_['Addres'] + ' ' + self.input_['Ip_addres'] + '.txt'
        with open(name_file, 'w') as g:
            for key, value in self.input_.items():

                    g.write(key + '====' + value + '\n')


    def ping_in(self):
        proverka = 'not ping'
        k = 0
        while k <= 3:
            check_host = os.system("ping " + '192.168.0.1')
            if check_host == 0:
                proverka = 'ping'
                k += 1
                print(k)
            else:
                proverka = 'not ping'

    def ping_out(self):
        proverka = 'ping'
        while proverka == 'ping':
            check_host = os.system("ping -n 1 " + '192.168.0.1')
            if check_host == 0:
                proverka = 'ping'
            else:
                proverka = 'not ping'

    def edit_config(self):
        i = int(self.input_['Number_switch'])
        znach = 0
        spisok_fiz_vlan = []
        if i == 1:
            znach = 601
        elif i == 2:
            znach = 631
        elif i == 3:
            znach = 661
        elif i == 4:
            znach = 701
        elif i == 5:
            znach = 731
        for j in range(znach, znach + 24):
            spisok_fiz_vlan.append(j)
        Vlan = str(int(self.input_['Vlan_manage']) - 3) + '-' + str(int(self.input_['Vlan_manage']) - 1)
        fiz_vlan_begin = '500-' + str(spisok_fiz_vlan[0] - 1)
        fiz_vlan_end = str(spisok_fiz_vlan[23] + 7) + '-' + '1000'
        config = self.Config
        config[6] = 'hostname ' + self.input_['Addres'] + '\n'
        config[7] = 'vlan ' + Vlan + ',' + self.input_['Vlan_manage']+ ',' + fiz_vlan_begin + ',' + \
                     str(spisok_fiz_vlan[0]) + '-' + str(spisok_fiz_vlan[-1]) +\
                    ',' + fiz_vlan_end + ',3700-3799' + '\n'

        config[10] = 'interface vlan ' + self.input_['Vlan_manage'] + '\n'
        config[12] = 'ip address ' + self.input_['Ip_addres'] + ' ' + self.input_['Mask'] + '\n'
        config[16] = 'ip route 0.0.0.0 0.0.0.0 ' + self.input_['Gateway'] + '\n'
        config[142] = 'lldp management-address ' + self.input_['Ip_addres'] + '\n'

        config[18] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[0]) + ' untagged' + '\n'
        config[19] = 'switchport pvid ' + str(spisok_fiz_vlan[0]) + '\n'

        config[22] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[1]) + ' untagged' + '\n'
        config[23] = 'switchport pvid ' + str(spisok_fiz_vlan[1]) + '\n'

        config[26] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[2]) + ' untagged' + '\n'
        config[27] = 'switchport pvid ' + str(spisok_fiz_vlan[2]) + '\n'

        config[30] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[3]) + ' untagged' + '\n'
        config[31] = 'switchport pvid ' + str(spisok_fiz_vlan[3]) + '\n'

        config[34] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[4]) + ' untagged' + '\n'
        config[35] = 'switchport pvid ' + str(spisok_fiz_vlan[4]) + '\n'

        config[38] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[5]) + ' untagged' + '\n'
        config[39] = 'switchport pvid ' + str(spisok_fiz_vlan[5]) + '\n'

        config[42] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[6]) + ' untagged' + '\n'
        config[43] = 'switchport pvid ' + str(spisok_fiz_vlan[6]) + '\n'

        config[46] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[7]) + ' untagged' + '\n'
        config[47] = 'switchport pvid ' + str(spisok_fiz_vlan[7]) + '\n'

        config[50] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[8]) + ' untagged' + '\n'
        config[51] = 'switchport pvid ' + str(spisok_fiz_vlan[8]) + '\n'

        config[54] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[9]) + ' untagged' + '\n'
        config[55] = 'switchport pvid ' + str(spisok_fiz_vlan[9]) + '\n'

        config[58] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[10]) + ' untagged' + '\n'
        config[59] = 'switchport pvid ' + str(spisok_fiz_vlan[10]) + '\n'

        config[62] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[11]) + ' untagged' + '\n'
        config[63] = 'switchport pvid ' + str(spisok_fiz_vlan[11]) + '\n'

        config[66] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[12]) + ' untagged' + '\n'
        config[67] = 'switchport pvid ' + str(spisok_fiz_vlan[12]) + '\n'

        config[70] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[13]) + ' untagged' + '\n'
        config[71] = 'switchport pvid ' + str(spisok_fiz_vlan[13]) + '\n'

        config[74] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[14]) + ' untagged' + '\n'
        config[75] = 'switchport pvid ' + str(spisok_fiz_vlan[14]) + '\n'

        config[78] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[15]) + ' untagged' + '\n'
        config[79] = 'switchport pvid ' + str(spisok_fiz_vlan[15]) + '\n'

        config[82] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[16]) + ' untagged' + '\n'
        config[83] = 'switchport pvid ' + str(spisok_fiz_vlan[16]) + '\n'

        config[86] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[17]) + ' untagged' + '\n'
        config[87] = 'switchport pvid ' + str(spisok_fiz_vlan[17]) + '\n'

        config[90] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[18]) + ' untagged' + '\n'
        config[91] = 'switchport pvid ' + str(spisok_fiz_vlan[18]) + '\n'

        config[94] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[19]) + ' untagged' + '\n'
        config[95] = 'switchport pvid ' + str(spisok_fiz_vlan[19]) + '\n'

        config[98] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[20]) + ' untagged' + '\n'
        config[99] = 'switchport pvid ' + str(spisok_fiz_vlan[20]) + '\n'

        config[102] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[21]) + ' untagged' + '\n'
        config[103] = 'switchport pvid ' + str(spisok_fiz_vlan[21]) + '\n'

        config[106] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[22]) + ' untagged' + '\n'
        config[107] = 'switchport pvid ' + str(spisok_fiz_vlan[22]) + '\n'

        config[110] = 'switchport general allowed vlan ' + str(spisok_fiz_vlan[23]) + ' untagged' + '\n'
        config[111] = 'switchport pvid ' + str(spisok_fiz_vlan[23]) + '\n'
        config[244] = 'ip dhcp l2relay vlan ' + str(spisok_fiz_vlan[0]) + '-' + str(spisok_fiz_vlan[23]) + '\n'
        self.Config = config

    def run_proshivka(self):
        self.open_file()
        self.create_file()
        self.edit_config()
        Conf = self.Config
        with open('CONFIG-FROM-Proga.txt', 'w') as g:
            for line in Conf:
                g.write(line)




        Prosh = self.Proshivka
        start_time = time.time()
        print('=========')
        time.sleep(10)

        # hFile = win32file.CreateFile('COM2', win32file.GENERIC_READ | win32file.GENERIC_WRITE, 0, None,
        #                              win32file.OPEN_EXISTING, 0, None)
        # print('=========')
        #
        # comDCB = win32file.DCB()
        # print('=========')
        #
        # comDCB.ByteSize = 8
        # comDCB.Parity = win32file.NOPARITY
        # comDCB.BaudRate = 38400
        #
        # win32file.SetCommState(hFile, comDCB)
        # win32file.SetupComm(hFile, 4096, 4096)
        # win32file.SetCommMask(hFile, 1)
        #
        # for comand_proshivka in Prosh:
        #     comand_proshivka = comand_proshivka[:-1] + '\r'
        #     ttt = bytearray(comand_proshivka, encoding='cp1251')
        #     win32file.WriteFile(hFile, ttt, None)
        #     print(comand_proshivka)
        #
        # print('start')
        # self.ping_out()
        # print('out')
        # self.ping_in()
        # print('in')
        # time.sleep(3)
        #
        # for comand_config in Conf:
        #     comand_config = comand_config[:-1] + '\r'
        #     ttt = bytearray(comand_config, encoding='cp1251')
        #     win32file.WriteFile(hFile, ttt, None)
        #     print(comand_config)
        #
        # print('=========')
        #
        # win32file.CloseHandle(hFile)
        print('programm has been finished:{:.2f}'.format(time.time() - start_time))

