import pandas as pd


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


print(add(1, 2))
print(subtract(2, 5))
print(multiply(2, 10))


data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
