import string

def get_letter_range(input_str):
    letters = string.ascii_letters
    parts = input_str.split('-')
    start = parts[0]
    end = parts[1]
    start_index = letters.index(start)
    end_index = letters.index(end)
    result = letters[start_index:end_index+1]
    return result

user_input = input("Введіть дві літери через дефіс (наприклад, a-c): ")
output = get_letter_range(user_input)
print(user_input + " -> " + output)