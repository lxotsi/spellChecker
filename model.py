from textblob import TextBlob
import language_tool_python

class SpellCheckerModule:
    def __init__(self):
        # Initialize the grammar checker tool (language_tool_python)
        self.tool = language_tool_python.LanguageTool('en-US')

    def correct_spelling(self, text):
        """
        Corrects the spelling of each word in the text.
        """
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())  # Use TextBlob to correct spelling
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        """
        Corrects grammar issues in the text.
        """
        matches = self.tool.check(text)  # Use language_tool_python for grammar correction
        corrected_text = language_tool_python.utils.correct(text, matches)  # Get the corrected text
        mistakes_count = len(matches)  # Count the number of mistakes
        return corrected_text, mistakes_count

# Test the functionality
if __name__ == "__main__":
    obj = SpellCheckerModule()
    text = "I'm going to the store to buy some milk."
    
    # Correct spelling
    corrected_spelling = obj.correct_spelling(text)
    print(f"Corrected Spelling: {corrected_spelling}")
    
    # Correct grammar
    corrected_grammar, grammar_mistakes = obj.correct_grammar(text)
    print(f"Corrected Grammar: {corrected_grammar}")
    print(f"Number of Grammar Mistakes: {grammar_mistakes}")
