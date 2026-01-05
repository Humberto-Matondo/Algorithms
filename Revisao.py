from array import array

users = [
    {'nome': 'Humberto', 'age': 28, 'email': 'humbertomat77@gmail.com'},
    {'nome': 'Sandra', 'age': 30, 'email': 'sandra@gmail.com'},
    {'nome': 'Carlos', 'age': 35, 'email': 'carlos@gmail.com'},
    {'nome': 'Gabriel', 'age': 19, 'email': 'Gabril@gmail.com'},
    {'nome': 'Bruninha', 'age': 24, 'email': 'Bruninha@gmail.com'},
    ]

filtered_users_by_age = []
for user in users:
    if user['age'] > 25:
        filtered_users_by_age.append(user)

print("Nome dos usuários:\n")
for user in users:
    print(f"Nome: {user['nome']}")

print("\nDetalhes dos usuários:\n")
for user in users:
    print(f"Nome: {user['nome']}, Idade: {user['age']}, Email: {user['email']}")

print("\nDetalhes dos usuários maiores de 25 anis:\n")
for user in filtered_users_by_age:
    print(f"Nome: {user['nome']}, Idade: {user['age']}, Email: {user['email']}")

