from array import array
def filter_users_by_age(users, age_limit):
    filtered_users_by_age = []
    for user in users:
        if user['age'] > age_limit:
            filtered_users_by_age.append(user)
    return filtered_users_by_age

def printUsers(users):
    for user in users:
        print(f"Nome: {user['nome']}, Idade: {user['age']}, Email: {user['email']}")

users = [
    {'nome': 'Humberto', 'age': 28, 'email': 'humbertomat77@gmail.com'},
    {'nome': 'Sandra', 'age': 30, 'email': 'sandra@gmail.com'},
    {'nome': 'Carlos', 'age': 35, 'email': 'carlos@gmail.com'},
    {'nome': 'Gabriel', 'age': 19, 'email': 'Gabril@gmail.com'},
    {'nome': 'Bruninha', 'age': 24, 'email': 'Bruninha@gmail.com'},
    ]

print("\nNome dos usuários:\n")
for user in users:
    print(f"Nome: {user['nome']}")

print("\nDetalhes dos usuários:\n")
for user in users:
    print(f"Nome: {user['nome']}, Idade: {user['age']}, Email: {user['email']}")

filtered_users_by_age = filter_users_by_age(users, 25)

print("\nDetalhes dos usuários maiores de 25 anos:\n")
printUsers(filtered_users_by_age)

