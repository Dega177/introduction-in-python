from translate import Translator

translator = Translator(from_lang='en',  to_lang="ru")

with open('text_4.txt', 'r', encoding='utf-8') as source_text:
    content = source_text.readlines()

with open('text_output_4.txt', 'w', encoding='utf-8') as output_text:
    output_text.writelines(translator.translate(line[:line.index(' ')]) + line[line.index(' '):] for line in content)
