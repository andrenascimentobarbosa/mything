#!/usr/bin/python3 

# modules
import sys


# defs
def start():
    start = input('Quit (q)\nPress Enter: ').strip().lower()
    if start == 'q':
        sys.exit(1)
    else:
        pass


def header(txt, num=25):
    print('-'*num)
    print(txt.center(num))
    print('-'*num)


def agenda():
    days = ['mon', 'tue', 'wed', 'thu', 'fry', 'sat', 'sun']
    with open('your_agenda.txt', 'w+') as f:
        f.write('DAY  -    Task')
        for day in days:
            tasks_input = str(input(f'Tasks for {day}: '))
            tasks = f'\n{"_"*20}\n\033[1m{day}\033[m:  -  {tasks_input}\n\n'
            f.write(tasks)




# main
start()

msg = """
    
   _____             _____                             .___        
  /     \ ___.__.   /  _  \    ____   ____   ____    __| _/____    
 /  \ /  <   |  |  /  /_\  \  / ___\_/ __ \ /    \  / __ |\__  \   
/    Y    \___  | /    |    \/ /_/  >  ___/|   |  \/ /_/ | / __ \_ 
\____|__  / ____| \____|__  /\___  / \___  >___|  /\____ |(____  / 
        \/\/              \//_____/      \/     \/      \/     \/  

    """

header(msg, 100)

agenda()    


