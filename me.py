import time
import fade
import webbrowser
import os



asciibaner = """
██╗███╗   ██╗████████╗██████╗  █████╗ ██████╗ ██╗     ███████╗
██║████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║██╔██╗ ██║   ██║   ██████╔╝███████║██████╔╝██║     █████╗  
██║██║╚██╗██║   ██║   ██╔══██╗██╔══██║██╔══██╗██║     ██╔══╝  
██║██║ ╚████║   ██║   ██║  ██║██║  ██║██████╔╝███████╗███████╗
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
[1] Join mon discord (leak)
[2] Voir mes objectif 
[3] m'ajouter sur discord
[!] notez que ce programme est vraiment nul , et c'est juste pour me presenter via un program python
[*]votre choix : """


jspcommentnommercettevariable = "mes objectif sont de progresser en dev (python principalement) et de plus tard , faire de l'informatique mon métier !(j'aimerais aussi que mon serveur discord monte en fleche lol) "
jspcommentnommercettevariable = fade.purpleblue(jspcommentnommercettevariable)
asciibaner = fade.pinkred(asciibaner)

choice = input(asciibaner)
if "1" in choice.lower():
    webbrowser.open('https://discord.gg/freeforreal')
    print(' merci d avoir rejoins mon serveur !' )
    time.sleep(2)
    os.system('cls')
    os.system('python me.py')
    
    
if "2" in choice.lower():
    print(jspcommentnommercettevariable)
    time.sleep(8)
    os.system('cls')
    os.system('python me.py')
    
    
if "3" in choice.lower():
    webbrowser.open('https://discord.com/users/1282716636880830509')
    print('merci de m ajouter (: ' )
    time.sleep(3)
    os.system('cls')
    os.system('python me.py')
    
    
    
    
    
    
    
    
    
    
    
else:
    print(' choix non dispo')
    os.system('cls')
    os.system('python me.py')
    
    


