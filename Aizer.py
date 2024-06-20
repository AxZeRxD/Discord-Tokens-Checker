import datetime,requests,threading;import os as aizer;from colorama import Fore;from pystyle import Colors, Colorate, Center, Write

ct = datetime.datetime.now().strftime('%D:%H:%M:%S')
R  = Fore.RESET
G  = Fore.LIGHTGREEN_EX
C  = Fore.LIGHTCYAN_EX
Y  = Fore.LIGHTYELLOW_EX
RD = Fore.RED
LB = Fore.LIGHTBLACK_EX

B   = "\x1b[38;5;0m"
O   = "\x1b[38;5;209m"
SB  = "\x1b[38;5;51m"
LBL = "\x1b[38;5;27m"
I = F"{LB}[{LBL}INFO{LB}]{R}"


mohit = """
    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗            
    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║            
       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║            
       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║            
       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║            
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝            
                                                        
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
════════════════════════════════════════════════════════
        TOKEN CHECKER || AIZER || .GG/LUXEOP  
════════════════════════════════════════════════════════\n\n\n\n"""

def createfile():
    if not aizer.path.exists('tokens.txt'):
        with open('tokens.txt', 'w') as file:
            file.write('')

    if not aizer.path.exists('output'):
        aizer.makedirs('output')

    with open('output/working.txt', 'w') as file:
        file.write('')
    
    with open('output/invalid.txt', 'w') as file:
        file.write('')
        print(f"{LB} [\x1b[38;5;5m{ct}{LB}] {I} {G}CREATED FILES AND FOLDER.")

def checktokens(token):

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        ipv4 = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        ipv6 = requests.get('https://discord.com/api/v9/users/@me', headers=headers, allow_redirects=False)

        if ipv4.status_code == 200 or ipv6.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"{LB} [\x1b[38;5;5m{ct}{LB}] {I} {C}ERROR")
        return False

def processtokens():
    with open('tokens.txt', 'r') as file:
        tokens = file.readlines()

    with open('output/working.txt', 'w') as working, open('output/invalid.txt', 'w') as invalid:
        def process_chunk(chunk):
            for token in chunk:
                token = token.strip()
                if checktokens(token):
                    working.write(token + '\n')
                    print(f"{LB} [\x1b[38;5;5m{ct}{LB}] {I} {G}VALID   {LB}[{SB}{token[:27]}*********************{LB}]{R}")
                else:
                    invalid.write(token + '\n')
                    print(f"{LB} [\x1b[38;5;5m{ct}{LB}] {I} {RD}INVALID {LB}[{SB}{token[:27]}*********************{LB}]{R}")

        custom = 2 
        trd = [tokens[i:i + custom] for i in range(0, len(tokens), custom)]

        threads = []
        for chunk in trd:
            thread = threading.Thread(target=process_chunk, args=(chunk,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()



if __name__ == '__main__':
    aizer.system("cls")
    print(Colorate.Vertical(Colors.cyan_to_blue ,Center.XCenter(mohit)))
    createfile()
    global tokens, total
    with open("tokens.txt", "r") as f:
        tokens = f.readlines()
        total = len(tokens)
        print(f"{LB} [\x1b[38;5;5m{ct}{LB}] {I} {C}LOADED {LB}{total}{C} TOKENS{R}")
    processtokens()
