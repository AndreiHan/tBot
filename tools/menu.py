from tools import bot_commands
from tools.key_mgmt import create_json


def ask_yesno(question):
    """
    Helper to get yes / no answer from user.
    """
    yes = {'yes', 'y', 'Y', ''}

    no = {'no', 'n', 'N'}

    done = False
    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond by yes(y/Y) or no(n/Y)")


def print_menu():
    menu_options = {
        1: 'Enter the keys manually (will delete previous config)',
        2: 'Already created KEY.json',
        3: 'Exit'
    }
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


'''
def clear():
    param = 'cls' if platform.system().lower() == 'windows' else 'clear'
    command = [param]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0
'''


def main_menu():
    while True:
        print_menu()

        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        else:
            if option == 1:
                create_json()
                bot_commands.init_check()
                bot_commands.main_loop()
            elif option == 2:
                try:
                    bot_commands.init_check()
                    bot_commands.main_loop()
                except FileNotFoundError:
                    print("\nFile not found... \n")
            elif option == 3:
                print('Bye now!')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
