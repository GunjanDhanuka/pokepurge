# attacks/black_box_attack.py

from .base_attack import BaseAttack
import random

class BlackBoxAttack(BaseAttack):
    def __init__(self):
        super().__init__()

    def apply(self, prompt):
        """
        Base method; returns the prompt unchanged.
        """
        return prompt

class SynonymReplacementAttack(BlackBoxAttack):
    def __init__(self):
        super().__init__()
        self.synonym_dict = self.load_synonyms()

    def apply(self, prompt):
        """
        Replaces forbidden words with synonyms.
        """
        words = prompt.split()
        new_words = []
        for word in words:
            lower_word = word.lower()
            if lower_word in self.synonym_dict:
                synonym = random.choice(self.synonym_dict[lower_word])
                print(f"SynonymReplacementAttack: Replacing '{word}' with '{synonym}'.")
                new_words.append(synonym)
            else:
                new_words.append(word)
        return ' '.join(new_words)

    def load_synonyms(self):
        """
        Loads synonyms for forbidden words.
        """
        synonym_dict = {
            'pikachu': ['electric mouse', 'pika', 'yellow rodent'],
            'charizard': ['fire dragon', 'flame lizard'],
            # Add more synonyms as needed
        }
        return synonym_dict

class HomographAttack(BlackBoxAttack):
    def __init__(self):
        super().__init__()
        self.homograph_map = self.create_homograph_map()

    def apply(self, prompt):
        """
        Replaces characters with visually similar Unicode characters.
        """
        new_prompt = ''
        for char in prompt:
            if char.lower() in self.homograph_map and random.random() < 0.5:
                homograph_char = random.choice(self.homograph_map[char.lower()])
                print(f"HomographAttack: Replacing '{char}' with '{homograph_char}'.")
                new_prompt += homograph_char
            else:
                new_prompt += char
        return new_prompt

    def create_homograph_map(self):
        """
        Creates a mapping of characters to their homographs.
        """
        homograph_map = {
            'a': ['а', 'à', 'á', 'â', 'ã', 'ä'],
            'e': ['е', 'è', 'é', 'ê', 'ë'],
            'i': ['і', 'ì', 'í', 'î', 'ï'],
            'o': ['о', 'ò', 'ó', 'ô', 'õ', 'ö'],
            'c': ['с', 'ç'],
            'p': ['р'],
            's': ['ѕ', 'ş'],
            # Add more mappings as needed
        }
        return homograph_map
