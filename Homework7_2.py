def custom_write(file_name, strings):
    strings_positions = {}
    string_number = 0
    file_name = f'{file_name}.txt'
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        string_number += 1
        strings_positions[string_number, file.tell()] = string
        file.write(f'{string}\n')
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
