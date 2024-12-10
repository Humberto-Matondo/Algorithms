
from dataclasses import dataclass

''' ESTRUTURA IF and ELSE: '''

def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')

    print('...rest of the code')

# execute_command('ls')


''' ESTRUTURA CASE: '''

# BASIC
# case 'batata': = if case == 'batata':
# case _: == else (default case)

def execute_command(command):
    match command: #como se fosse um if command 

        case 'ls': #caso foi igual a 'ls'
            print('$ listing files')
        
        case 'cd': #caso foi igual a 'cd'
            print('$ changing directory')
        
        case _:  # Não obrigatório usa-lo, funciona como o ELSE, so executa quando o comando n for igual a nada.
            print('$ command not implemented')

    print('...rest of the code')

# execute_command('pwd')

''' .............ESTRUTURA CASE ACTUALIZADO PARA O PYTHON:'''

'''1. EXEMPLO: '''

# Commands in match
# match command_food.split(' '): # split two values
#     case ['like', food, ]: # get a literal and a variable

def execute_command(command):

    match command.split(): # antes de pasar para os cases, podes fazer uma operacao com o command que u usuario informar.
                            #nesse exemplo gracas ao split() vai dividir a string. 
        case ['ls', path, *_]:
            print('$ listing files from', path)
    
        case ['cd', path]:
            print('$ changing directory to', path)
    
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')

# execute_command('ls /home/ /Users /mais')
# execute_command('cd /Users/')

'''2. EXEMPLO: '''

# Case with or inside a list
# case ['enjoy' | 'love', food]:


def execute_command(command):
    match command.split():
        case ['ls' | 'list', path, *_]:
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('list /home/ /Users /mais')

# With rest
# case ['like', *foods]


def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories]:
            for directory in directories:
                print('$ listing directory from', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')

# With case guard
# case ['like', *foods] if len(foods) <= 1:


def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('ls /one/')

# With as
# case data as variable if 'CRACKED' in variable:


def execute_command(command):
    match command.split():
        case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
            print(f'{the_command=}, {the_list=}')
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('ls /one/')

# With generic placeholders
# case ['A', 'B', _, _]:
# case ['A', 'B', _, _, *_, 'Z']:


def execute_command(command):
    match command.split():
        case ['ls' | 'list', _, *directories, _]:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('ls /one/')

# With dicts
# case {'name': _, 'last': 'Doe'}:
# case {'name': 'Otávio' as name, 'last': 'Doe'} as data:


def execute_command(command):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command({'command': 'ls', 'directories': []})
# execute_command('ls /one/')

# With objects
# case Food(name='rice') | Food(name='banana'):


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command(Command('ls', ['/users']))
execute_command(Command('cd', ['/users']))