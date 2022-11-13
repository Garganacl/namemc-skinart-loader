import time
import webbrowser
import os
import keyboard




while True:
    print(f'''
    PLEASE ENTER THE NUMBER OF THE OPTION YOU WOULD LIKE TO SELECT

    (1) SET SKIN VARIANT (NOT REQUIRED) (DEFAULTED TO classic)
    (2) SET BEARER TOKEN (REQUIRED)
    (3) SET THE MINECRAFT NAME YOU ARE LOADING SKINS FOR NAMEMC (REQUIRED)
    (4) LINK FOR HOW TO GET YOUR BEARER TOKEN (ONLY LAST FOR 24 HOURS) (NOT REQUIRED)
    (5) HOW TO SET UP SKINS (NOT REQUIRED)
    (7) START THE LOADING PROCESS 
    (8) SET THE DEFAULT LOADING WEBPAGE (VARYS ON WIFI) (IN SECONDS) (DEFAULTS TO 5)


    | IF THE SCRIPT ISNT WORKING TRY SETTING A NEW BEAERER TOKEN
    | THIS SCRIPT LOADS 26 SKINS SO YOU CAN MANUALLY IMPORT THE LAST SKIN AS YOUR OWN IF YOU WOULD LIKE TO CHANGE THIS PRESS NUMBER 6
    | SCRIPT ONLY WORKS WITH Https://thomas.gg/ GENERATED SKINART FILE
    | MAKE SURE TO RUN pip install -r requirements.txt TO RUN ALL THE NEEDED MODULES

    ''')
    try:
        number = int(input('Enter your number: '))
    except:
        os.system('cls')
        print("Please enter a correct number! ")

    if number == 1:

        variant = str(input("Please input the type of skin you want 'classic' or 'slim': "))

        if 'classic' in variant:
             with open('../namemc-skinart-loader/assets/variant.txt','w') as v:
                v.write(f"{variant}")
                os.system('cls')
                print('Variant has been set.') 
                time.sleep(1) 
        if 'slim' in variant:
             with open('../namemc-skinart-loader/assets/variant.txt','w') as v:
                v.write(f"{variant}")
                os.system('cls')
                print('Variant has been set.') 
                time.sleep(1)   
        else:   
            os.system('cls')
            print('Please enter a correct variation')     

    if number == 2:

        token = input("Please input your bearer token: ")
        
        with open('../namemc-skinart-loader/assets/token.txt','w') as t:
            t.write(f"{token}")  

        os.system('cls')
        
        print('Token has been set.')

    if number == 3:

        mcname = input("Please input your minecraft name: ")

        with open('../namemc-skinart-loader/assets/mcname.txt','w') as m:
            m.write(f"{mcname}")  

        os.system('cls')

        print('Minecraft name has been set.')    

    if number == 4:
            os.system('cls')
            webbrowser.open('https://kqzz.github.io/mc-bearer-token/') 
            print('''
            LINK HAS OPENED IN YOUR BROWSER IF ANY ERROR HERE IS THE LINK     https://kqzz.github.io/mc-bearer-token/
            ''')
            time.sleep(1)
    if number == 5:
        print('''
        
        Step (1) PUT YOUR IMAGE INTO https://Thomas.gg/
        Step (2) TAKE THE Skinart.zip AND EXCTRACK IT 
        Step (3) PUT ALL THE NUMBERED SKIN FILES IN THE namemc-skinart-loader\assets\skins FOLDER
        Step (6) AFTER YOU DO ALL THAT MAKE SURE U SET UP ALL THE REQUIRED STUFF THEN RUN NUMBER 6 TO START THE LOADING PROCESS 

        
        ''')

    if number == 7:
        abspath = os.path.abspath("../namemc-skinart-loader/assets/skins")
        
        substr = "\\"
        inserttxt = "\\"    
        abspath = abspath.replace(substr, substr + inserttxt)
        with open('../namemc-skinart-loader/assets/number.txt') as numba:
                numba = numba.readline()
                numba = int(numba)
        num = numba
        while num > 0:
            with open('../namemc-skinart-loader/assets/mcname.txt') as minecraftname:
                minecraftname = minecraftname.readline()
                minecraftname = str(minecraftname)
            with open('../namemc-skinart-loader/assets/token.txt') as ttoken:
                ttoken = ttoken.readline()
            with open('../namemc-skinart-loader/assets/variant.txt') as vvariant:
                vvariant = vvariant.readline()
            with open('../namemc-skinart-loader/assets/time.txt') as time_check:
                time_check = time_check.readline()
                time_check = int(time_check)
            if minecraftname == '':
                print("Please enter a minecraft name.")
                time.sleep(2)
                break
            if ttoken == '':
                print("Please enter a bearer token.")
                time.sleep(2)
                break
            os.system(f'curl -X POST -H "Authorization: Bearer {ttoken}" -F variant={vvariant} -F file="@{abspath}\Skin-{num}.png;type=image/png" https://api.minecraftservices.com/minecraft/profile/skins')
            webbrowser.open(f'https://namemc.com/{minecraftname}')
            time.sleep(time_check)
            keyboard.press_and_release('ctrl+w')
            os.system('cls')
            print(f'Done with skin {num} onto skin number {num - 1}.')
            num -= 1

    if number == 8:
        timee = input("Please enter a time (in seconds): ")
        with open('../namemc-skinart-loader/assets/time.txt','w') as t:
                t.write(f"{timee}")
                os.system('cls')
                print('Time has been set.') 
                time.sleep(1) 