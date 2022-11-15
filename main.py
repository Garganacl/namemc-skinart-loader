import time
import webbrowser
import os
import keyboard
import requests

while True:
    # Sets the absolute paths for the files
    abspath = os.path.abspath("../namemc-skinart-loader-main/assets/skins")
    absp_number = os.path.abspath('../namemc-skinart-loader-main/assets/number.txt')
    absp_mcname = os.path.abspath('../namemc-skinart-loader-main/assets/mcname.txt')
    absp_token = os.path.abspath('../namemc-skinart-loader-main/assets/token.txt')
    absp_variant = os.path.abspath('../namemc-skinart-loader-main/assets/variant.txt')
    absp_time = os.path.abspath('../namemc-skinart-loader-main/assets/time.txt')
    
    substr = "\\"
    inserttxt = "\\"    
    abspath = abspath.replace(substr, substr + inserttxt)
    absp_number = absp_number.replace(substr, substr + inserttxt)
    absp_mcname = absp_mcname.replace(substr, substr + inserttxt)
    absp_token = absp_token.replace(substr, substr + inserttxt)
    absp_variant = absp_variant.replace(substr, substr + inserttxt)
    absp_time = absp_time.replace(substr, substr + inserttxt)

    # Prints the main menu of the script
    print(f'''
    PLEASE ENTER THE NUMBER OF THE OPTION YOU WOULD LIKE TO SELECT

    (1) SET SKIN VARIANT (NOT REQUIRED) (DEFAULTED TO classic)
    (2) SET BEARER TOKEN (REQUIRED)
    (3) SET THE MINECRAFT NAME YOU ARE LOADING SKINS FOR NAMEMC (REQUIRED)
    (4) LINK FOR HOW TO GET YOUR BEARER TOKEN (ONLY LAST FOR 24 HOURS) (NOT REQUIRED)
    (5) HOW TO SET UP SKINS (NOT REQUIRED)
    (7) START THE LOADING PROCESS 
    (8) SET THE DEFAULT LOADING WEBPAGE (VARIES ON WIFI) (IN SECONDS) (DEFAULTS TO 5)


    | IF THE SCRIPT ISNT WORKING TRY SETTING A NEW BEAERER TOKEN
    | SCRIPT ONLY WORKS WITH Https://thomas.gg/ GENERATED SKINART FILE
    | MAKE SURE TO RUN pip install -r requirements.txt TO RUN ALL THE NEEDED MODULES

    ''')
    
    try:
        # Handles when you press a number
        number = int(input('Enter your number: '))
    except:
        # Handles when a incorrect button is entered
        os.system('cls')
        print("Please enter a correct number! ")

    if number == 1:
            # Handles when button 1 is pressed
        variant = str(input("Please input the type of skin you want 'classic' or 'slim': "))

        if 'classic' in variant:
            # Saves classic to the variant.txt file
             with open(f'{absp_variant}','w') as v:
                v.write(f"{variant}")
                # Clears the terminal
                os.system('cls')
                print('Variant has been set.') 
                time.sleep(1) 
        if 'slim' in variant:
            # Saves slim to the variant.txt file
             with open(f'{absp_variant}','w') as v:
                v.write(f"{variant}")
                # Clears the terminal
                os.system('cls')
                print('Variant has been set.') 
                time.sleep(1)   
        else: 
            # Handles when a incorrect variant is entered
            # Clears the terminal  
            os.system('cls')
            print('Please enter a correct variation')     

    if number == 2:
            # Handles when button 2 is pressed
        token = input("Please input your bearer token: ")
        
        # Saves the token to the token.txt file
        with open(f'{absp_token}','w') as t:
            t.write(f"{token}")  

        # Clears the terminal
        os.system('cls')
        
        print('Token has been set.')

    if number == 3:
            # Handles when button 3 is pressed
        mcname = str(input("Please input your minecraft name: "))
        response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{mcname}')

        # Makes sure that the minecraft name is valid

        if response.status_code == 200:
            # If the name is valid it saves it in mcname.txt
            with open(f'{absp_mcname}','w') as m:
                m.write(f"{mcname}")  

                os.system('cls')

                print('Minecraft name has been set.') 
        elif response.status_code == 204:
            # If name is invalid prints name is invalid and clears terminal
            os.system('cls')
            print('Please enter a valid minecraft name.') 
        else:
            # Clears the terminal and prints something is wrong with mojang api
            os.system('cls')
            print('Something is wrong with the Mojang api please try again later.')  

    if number == 4:
        # Handles when button 4 is pressed | Opens the how to get bearer token website
            os.system('cls')
            webbrowser.open('https://kqzz.github.io/mc-bearer-token/') 
            print('''
            LINK HAS OPENED IN YOUR BROWSER IF ANY ERROR HERE IS THE LINK     https://kqzz.github.io/mc-bearer-token/
            ''')
            time.sleep(1)
    if number == 5:
        # Handles when button 5 is pressed | Opens the skinart generator website
        webbrowser.open('https://thomas.gg')
        print('''
        
        Step (1) PUT YOUR IMAGE INTO https://Thomas.gg/
        Step (2) TAKE THE Skinart.zip AND EXCTRACT IT 
        Step (3) PUT ALL THE NUMBERED SKIN FILES IN THE namemc-skinart-loader\assets\skins FOLDER
        Step (6) AFTER YOU DO ALL THAT MAKE SURE U SET UP ALL THE REQUIRED STUFF THEN RUN NUMBER 6 TO START THE LOADING PROCESS 

        
        ''')

    if number == 7:
        # Handles when button 7 is pressed | Opens the skinart generator website
        num = 27

        while num > 0:
            # Loop that runs the uploading and opening namemc

            # Opens the mcname.txt file and grabs the name
            with open(f'{absp_mcname}') as minecraftname:
                minecraftname = minecraftname.readline()
                minecraftname = str(minecraftname)
                
            # Opening the token.txt and grabs the bearer token
            with open(f'{absp_token}') as ttoken:
                ttoken = ttoken.readline()

            # Opens the variant.txt file and grabs the variant name
            with open(f'{absp_variant}') as vvariant:
                vvariant = vvariant.readline()

            # Opens the time.txt file and grabs the time
            with open(f'{absp_time}') as time_check:
                time_check = time_check.readline()
                time_check = int(time_check)

            if minecraftname == '':
                # Checks if the minecraft file is empty prints enter a minecraft name
                print("Please enter a minecraft name.")
                time.sleep(2)
                # Clears the terminal
                os.system('cls')
                break
            if ttoken == '':
                # Checks if the token.txt file is empty and prints enter a bearer token
                print("Please enter a bearer token.")
                time.sleep(2)
                # Clears the terminal
                os.system('cls')
                break
            # Uploads the skin to mojang
            result = os.system(f'curl --silent --output /dev/null -X POST -H "Authorization: Bearer {ttoken}" -F variant={vvariant} -F file="@{abspath}\Skin-{num}.png;type=image/png" https://api.minecraftservices.com/minecraft/profile/skins')
            result = int(result)
            # Checks if the bearer token is invalid
            if result != 23:
                # Opens namemc
                webbrowser.open(f'https://namemc.com/{minecraftname}')
                time.sleep(time_check)
                # Closes namemc
                keyboard.press_and_release('ctrl+w')
                # Clears the terminal
                os.system('cls')
                if num - 1 == 0:
                    # Checking if the number is 0 meaning it is all done and opens namemc for last time
                    print("All done!")
                    webbrowser.open(f'https://namemc.com/{minecraftname}')
                else:
                    # Prints the progress of the uploading process
                    print(f'Done with skin {num} onto skin number {num - 1}.')
                num -= 1
                # Checks If the bearer token is invalid it prints enter a valid bearer token
            elif result == 23:
                os.system('cls')
                print('Please enter a valid Bearer token.')
                # Goes back to the main menu of the script
                break
            
    if number == 8:
        # Handles when button 8 | Saves the time to how many seconds to wait for namemc website to load
        timee = input("Please enter a time (in seconds): ")
        with open(f'{absp_time}','w') as t:
                t.write(f"{timee}")
                # Clears the terminal
                os.system('cls')
                # Prints the time has been set
                print('Time has been set.') 
                time.sleep(1) 