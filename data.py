def roman_to_integer(s: str) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        value = roman_values[s[i]]
        if i < n - 1 and value < roman_values[s[i + 1]]:
            total -= value
        else:
            total += value
            
    return total

user_input = input("Введіть римське число: ")
result = roman_to_integer(user_input)
print(f"Цілочисельне значення: {result}")
