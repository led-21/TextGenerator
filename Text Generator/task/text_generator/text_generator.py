# Write your code here
import random
from collections import defaultdict

# Open File
text = input()
#text = "../test/corpus.txt"

with open(text, "r", encoding="utf-8") as f:
    tokens = f.read().split()

# Bigrams dictionary
trigrams_dict = defaultdict(lambda: defaultdict(int))

for i in range(len(tokens) - 2):
    head = tokens[i]+" "+tokens[i+1]
    tail = tokens[i + 2]
    trigrams_dict[head][tail] += 1

# Bigram words
sentence_bigram = list(trigrams_dict.keys())

# Starts with capitalized words without punctuation
sentence_starts = []

# Ends with punctuation
sentence_endings = set()

for word in sentence_bigram:
    word_split = word.split(" ")
    if word[0].isupper() and not word_split[0].endswith(('.','!','?')) and not word_split[1].endswith(('.','!','?')):
        sentence_starts.append(word)
    elif word.endswith(('.','!','?')):
        sentence_endings.add(word)

# Starts
for i in range(10):
    # Random word
    current_word = random.choice(sentence_starts)

    # Sentence
    sentence = current_word

    while len(sentence.split())<5 or current_word not in sentence_endings:
        tails = trigrams_dict[current_word]
        tail = max(tails, key=tails.get)
        sentence += " " + tail
        current_word = current_word.split()[1] + " " + tail

    print(sentence)
