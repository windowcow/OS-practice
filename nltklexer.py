from nltk import CFG
import nltk
grammar = CFG.fromstring(
    """
      S -> STEM OPTION
      STEM -> STEMSIGN STRING SEMICOLONE
      OPTION -> KEY OPTION | DISTRACTOR OPTION | KEY | DISTRACTOR
      
      KEY -> KEY_SIGN STRING SEMICOLONE
      DISTRACTOR -> DISTRACTOR_SIGN STRING SEMICOLONE
      
      
      SEMICOLONE -> ';'
      KEY_SIGN -> '-[*]'
      DISTRACTOR_SIGN -> '-[ ]'
      STEM_SIGN -> '-#'
    """
)

print(grammar.start())
print(grammar.productions())
parser = nltk.ChartParser(grammar)

sentence = """
    -# 지금 날씨는?;
    -[ ] 비가 온다;
    -[*] 눈이 온다;
"""
