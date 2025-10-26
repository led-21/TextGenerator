# TextGenerator

TextGenerator is a Natural Language Processing (NLP) solution developed as part of the **“NLP Engineer”** course from JetBrains Academy. The main goal of this project is to **predict the next word** in a textual sequence (pseudo-sentence) using **statistical language models**.

## Overview

The system uses **n-gram models** to analyze word sequences and statistically estimate the probability of the next word based on the previous context. This approach is fundamental in tasks such as **autocomplete**, **spell correction**, and **text generation**.

### Key Features

* Training of n-gram models (bigrams, trigrams, etc.) from a custom text corpus.
* Inference: Suggests the next word in a sequence based on context.
* Text manipulation and preprocessing (tokenization, normalization).
* Support for different n-gram sizes configurable by the user.

## Architecture and Algorithms

The core of the application is composed of:

* **Tokenization:** Splits text into units (tokens) for analysis.
* **n-Gram Model Construction:** Builds a frequency dictionary of n-grams extracted from the corpus.
* **Prediction:** Given a text sequence, the algorithm finds the corresponding n-gram and suggests the next word with the highest probability of occurrence.

The system can be easily adapted for other languages and corpora by changing the input data.

## Dependencies

* Python 3.8+
* Libraries: `nltk`, `numpy`, `pandas` (check `requirements.txt`)

To install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. **Training:**

   * Add your text corpus to the data directory.
   * Run the main script to train the model:

     ```bash
     python main.py --train --corpus data/my_corpus.txt
     ```

2. **Prediction:**

   * Generate the next word by providing a sequence:

     ```bash
     python main.py --predict "Artificial intelligence"
     ```

## Examples

```python
# Example usage in Python
from text_generator import TextGenerator

tg = TextGenerator('data/my_corpus.txt', n=3)
tg.train()
print(tg.predict_next("Artificial intelligence"))
```

## References

* [NLP Engineer Course - JetBrains Academy](https://hyperskill.org/tracks/15)
* Jurafsky, D.; Martin, J. H. - *Speech and Language Processing*, 3rd Edition.

## License

Distributed under the **MIT License**.
