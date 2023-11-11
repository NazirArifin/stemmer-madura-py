from stemmer_madura import stemmer as stemmerMadura
import re

text = 'abarna';
print(stemmerMadura(text, True, withNgram=True, ngGramThreshold=0.60))

