"""
This script demonstrates operations on lists and dictionaries including
product management, sales tracking, and student counting.
"""

# Constants
PRODUCTS_INITIAL = ["молоко", "хліб", "яйця", "сир", "м'ясо"]
SALES_INITIAL = {"молоко": 20, "хліб": 30, "яйця": 50, "сир": 10, "м'ясо": 5}
NEW_PRODUCTS = ["овочі", "фрукти"]
REMOVED_PRODUCT = "молоко"
STUDENT_NAME = 'Андрій'
CONTINENTS_MAS = ['івнічна Америка', 'Південа Америка']
CONTINENTS_NAS = ['Євразія', 'Африка', 'Австралія', 'Антарктида']
NAME_PROMPT = 'Введіть ім\'я: '
STUDENT_COUNT_MESSAGE = "Кількість Андріїв в групі:"
CONTINENT_SORT_MESSAGE = "Сортування континентів:"

# Initial product list and sales data
products = PRODUCTS_INITIAL.copy()
sales = SALES_INITIAL.copy()

# Display all products
print("Усі товари:")
for product in products:
    print(product)

# Add new products
products.extend(NEW_PRODUCTS)

print("\nТовари з новими елементами:")
for product in products:
    print(product)

# Remove a product
products.remove(REMOVED_PRODUCT)

print("\nТовари з видаленим елементом:")
for product in products:
    print(product)

# Insert a product at the beginning
products.insert(0, REMOVED_PRODUCT)

print("\nТовари з новим елементом на початку списку:")
for product in products:
    print(product)

# Display sales data
print("\nСписок проданих продуктів за день:")
for product, amount in sales.items():
    print(f"{product}: {amount}")

# Count occurrences of 'Андрій' in student list
students = [
    ['Іван', 'Петров'],
    ['Олександр', 'Ковальчук'],
    ['Марія', 'Сидоренко'],
    ['Андрій', 'Іванов'],
    ['Андрій', 'Соколов'],
    ['Олег', 'Петренко'],
    ['Наталія', 'Коваль'],
    ['Андрій', 'Кузьменко'],
    ['Юлія', 'Семенченко']
]

COUNT_ANDRIY = 0
for student in students:
    if student[0] == STUDENT_NAME:
        COUNT_ANDRIY += 1

print(STUDENT_COUNT_MESSAGE, COUNT_ANDRIY)

# Merge and sort continents
continents = CONTINENTS_MAS + CONTINENTS_NAS
continents.sort()

print("\n", CONTINENT_SORT_MESSAGE)
for continent in continents:
    print(continent)
