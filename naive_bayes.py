import math
from collections import defaultdict

training_data = [

    ("excellent battery", "positive"),
    ("good product", "positive"),

    ("bad delivery", "negative"),
    ("worst quality", "negative"),

    ("average product", "neutral"),
    ("okay delivery", "neutral")
]

word_counts = defaultdict(
    lambda: defaultdict(int)
)

class_counts = defaultdict(int)

vocab = set()

# Training
for text, label in training_data:

    class_counts[label] += 1

    for word in text.split():

        word_counts[label][word] += 1

        vocab.add(word)

total_docs = len(training_data)

# Prediction
def predict(sentence):

    scores = {}

    for label in class_counts:

        log_prob = math.log(

            class_counts[label] / total_docs
        )

        total_words = sum(

            word_counts[label].values()
        )

        for word in sentence.split():

            word_freq = (

                word_counts[label][word] + 1
            )

            prob = word_freq / (

                total_words + len(vocab)
            )

            log_prob += math.log(prob)

        scores[label] = log_prob

    return max(scores, key=scores.get)

print(

    predict("excellent product")
)