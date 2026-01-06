def filter_users_by_age(users, age_limit):
    filtered_users_by_age = []
    for user in users:
        if user['age'] > age_limit:
            filtered_users_by_age.append(user)
    return filtered_users_by_age

def printUsers(users):
    for user in users:
        print(f"Nome: {user['nome']}, Idade: {user['age']}, Email: {user['email']}")

def almendar_idade(users):
    for user in users:
        user['age'] += 5
    return users

def Media_das_idades(users):
    total = 0
    for user in users:
        total += user['age']
    print(total / len(users))
    
users = [
    {'nome': 'Humberto', 'age': 28, 'email': 'humbertomat77@gmail.com'},
    {'nome': 'Sandra', 'age': 30, 'email': 'sandra@gmail.com'},
    {'nome': 'Carlos', 'age': 35, 'email': 'carlos@gmail.com'},
    {'nome': 'Gabriel', 'age': 19, 'email': 'Gabril@gmail.com'},
    {'nome': 'Bruninha', 'age': 24, 'email': 'Bruninha@gmail.com'},
    ]

# Exercício 1:
print("\nNome dos usuários:\n")
for user in users:
    print(f"Nome: {user['nome']}")

print("\nDetalhes dos usuários:\n")
for user in users:
    print(f"Nome: {user['nome']}, Idade: {user['age']}, Email: {user['email']}")

print("\nDetalhes dos usuários maiores de 25 anos:\n")
printUsers(filter_users_by_age(users, 25))

# Exercício 2: Envelhecer usuários em 5 anos
print("\nusuários com 5 anos a mais:\n")
printUsers(almendar_idade(users))

# Exercício 3: Media das Idades
print("\nIdade Media:")
Media_das_idades(users)