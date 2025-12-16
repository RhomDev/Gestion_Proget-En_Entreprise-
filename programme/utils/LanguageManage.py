import json
import os

class LanguageManager:
    def __init__(self, default_language='fr-fr'):
        self.languages = {}
        self.current_language = default_language
        self.load_language(default_language)

    def load_language(self, language):
        try:
            lang_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'lang', f'{language}.json')
            with open(lang_file, 'r', encoding='utf-8') as file:
                self.languages[language] = json.load(file)
            self.current_language = language
        except FileNotFoundError:
            print(f"Language file {language}.json not found.")

    def get_text(self, key):
        try:
            return self.languages[self.current_language][key]
        except KeyError:
            print(f"Key '{key}' not found in language file.")
            return key

    def set_language(self, language):
        if language in self.languages:
            self.current_language = language
        else:
            self.load_language(language)