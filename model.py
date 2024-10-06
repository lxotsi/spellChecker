from textblob import TextBlob
from gingerit.gingerit import GingerIt

class SpellCheckerModule:
    def __init__(self):
        self.ginger_parser = GingerIt()
        self.spell_check = TextBlob("")

    def correct_spelling(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)
    
    def correct_grammar(self, text):
        matches = self.ginger_parser.parse(text)
        mistakes = []
        for mistake in matches['corrections']:
            mistakes.append(mistake['text'])
        mistakes_count = len(mistakes)
        return mistakes, mistakes_count
    
if __name__ == "__main__":
    obj = SpellCheckerModule()
    text = "I'm going to the store to buy some milk."
    print(obj.correct_grammar(text))
    print(obj.correct_spelling(text))
