from collections import Counter

tokens = [
    'excellent',
    'battery',
    'excellent',
    'delivery'
]

unigram_counts = Counter(tokens)

total_words = len(tokens)

for word in unigram_counts:

    probability = unigram_counts[word] / total_words

    print(word, probability)