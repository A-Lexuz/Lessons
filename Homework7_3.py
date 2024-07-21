import re # импортируем библиотеку для удаления пунктуационных знаков
class WordsFinder():
    def __init__(self, *files):
        self.files_list = []
        for file in files:      #цикл для создания списка из наименований файлов
            self.files_list.append(file)

    def get_all_words(self):
        all_words = {}
        for opened_file in self.files_list:
            with open(opened_file, mode='r', encoding='utf-8') as file: #открываем каждый файл из списка файлов
                file_lower = file.read().lower()    #переводим текст файла в нижний регистр
                file_lower_no_symbol = re.sub('[,.\n=!?;: - ]',' ',file_lower)  #убираем пунктуационные
                                                                            #знаки через re.sub
                all_words[opened_file] = file_lower_no_symbol.split()   #разбиваем текст файла и заносим в словарь
        return all_words

    def find(self, word):
        find_word = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word_lower:
                    find_word[name] = i + 1
                    break
        return find_word

    def count(self, word):
        word_lower = word.lower()
        count_words = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in range(len(words)):
                if words[i] == word_lower:
                    count += 1
                    count_words[name] = count
            return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

