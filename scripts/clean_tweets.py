import re

def clean_string(s):
    s = s.lower()
    s = re.sub(r'@([a-z0-9_]+)', "", s)
    s = re.sub(r'https?://[^ ]+|www.[^ ]+|pic.twitter.[^ ]+|twitter.com[^ ]', "", s)  # remove urls
    matchobj = re.findall(r'#[^ ]+', s)
    s = re.sub(r'[^a-z\s.,?!]', "", s).strip()  # keep only characters, whitespaces and dots
    return s, matchobj




test = 'I like to move it #coronavirus www.kobe.com https://twitter.com #funnyvideos #menumespitipic.twitter.com/iYSaPGnD3H'

clean_text, matchobj = clean_string(test)
print(clean_text)
print(' '.join(matchobj))
