import os
import time
import shutil
from termcolor import colored
from colorama import init

init()

def cls():
    os.system("clear")

def pause():
    input(colored("\nAppuie sur Entrée pour continuer...", "yellow"))

class InitiateBot:
    def __init__(self, token, prefix, userid, guildid):
        self.token = token
        self.prefix = prefix
        self.userid = userid
        self.guildid = guildid

    def setup(self):
        if os.path.exists("modules/start.py"):
            os.remove("modules/start.py")
        shutil.copyfile("modules/sample.py", "modules/start.py")

        with open("modules/whitelists.txt", "w") as file:
            for id in self.userid:
                file.write(f"{id}\n")

        with open("modules/start.py", "r") as file:
            content = file.read()

        content = content.replace("{bottoken}", self.token)
        content = content.replace("{cmdprefix}", self.prefix)
        content = content.replace("{gid}", self.guildid)

        with open("modules/start.py", "w") as file:
            file.write(content)

        os.system("clear")
        print(colored("Bot prêt à démarrer...", "green"))
        os.system("python modules/start.py")

def main():
    cls()
    print(colored("   __        __        ___           ", "green"))
    print(colored("  /__\__  __/__\__ _  / _ \ _ __ ___ ", "green"))
    print(colored(" /_\ \ \/ /_\ \ \ / / /_)/ '__/ _ \", "green"))
    print(colored("//__  >  < //__  >  < / ___/\__ \  __/", "green"))
    print(colored("\__/ /_/\_\__/ /_/\_\/\/    |___/\___|", "green"))
    print(colored("             WewZ Spammer Termux", "blue"))
    print("")

    prefix = input(colored("Préfixe du bot => ", "blue"))
    token = input(colored("Token du bot => ", "blue"))
    userid = input(colored("IDs whitelist (séparés par virgule) => ", "blue")).split(",")
    guildid = input(colored("ID du serveur cible => ", "blue"))

    bot = InitiateBot(token, prefix, [u.strip() for u in userid], guildid)
    bot.setup()

if __name__ == "__main__":
    main()
