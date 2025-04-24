import re

def tokenize_gujarati(text):
    patterns = {
        'url': r'https?://\S+',
        'email': r'\b[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}\b',
        'date': r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b|\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b',
        'number': r'\b[\d,]+(?:\.\d+)?\b',
        'fraction': r'\b\d+/\d+\b',
        'social_media': r'@\w+',
        'gujarati_word': r'[\u0A80-\u0AFF]+' ,
        'punctuation': r'[.,!?;:-]'
    }
    
    tokens = []
    for category, pattern in patterns.items():
        matches = re.findall(pattern, text)
        for match in matches:
            tokens.append((category, match))
    
    return tokens

gujarati_text = "મારું ઈમેલ example@email.com છે અને હું @વપરાશકર્તા છું. તારીખ ૧૨/૦૫/૨૦૨૩ છે."
tokens = tokenize_gujarati(gujarati_text)
for token in tokens:
    print(token)