from sre_parse import WHITESPACE


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
        
        WHITESPACE = ' \n\t'
        DIGITS = '0123456789'
        
    def advance(self):
        try:
            self.current_char = next(self.text)
        except:
            self.current_char = None
            
    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()