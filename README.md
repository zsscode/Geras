# Geras
Accuracy comparison of a Bayesian Network, a Dense Neural Network and an LSTM in detecting Alzheimer's symptoms on the Pitt Corpus: https://dementia.talkbank.org/access/English/Pitt.html

## Brief guide
The dataset has been pre-processed to extract relevant features and keep only lemmatized content words (verbs, nouns, adverbs and adjectives).
The Bayesian Network and the Dense Network classify using only features.
The LSTM classifies using both features and embedded text.

To embed the text, download the pre-trained Wiki News 300d vectors from https://fasttext.cc/docs/en/english-vectors.html, unzip the compressed file and add it to the project folder.
Run `lstm.py --embed`. The embedded matrix will be saved to file; all further tests can be run without embedding (with `lstm.py`).

### Extracted features:
 * Age
 * Number of utterances
 * Mean length of utterances
 * Number of sentences
 * Number of unique words
 * Number of predicates
 * Number of coordinated sentences
 * Number of subordinated sentences
 * Repetitions ratio
 * Revisions ratio
 * Unintelligible words ratio
 * Filler words ratio
 * Trailing offs ratio
 * Incomplete words ratio
 * Prolonged syllables ratio
 * Pauses between syllables ratio
 * Pauses between words ratio
 * Overlaps ratio
 * Adjectives and adverbs ratio
 * Type-token ratio
 * Idea density
 * Word2Vec distance

## Performance
The algorithms perform with the following accuracy on the test set:

| Model | Accuracy | Precision | Recall |
|-------|----------|-----------|--------|
| BN    | 72.1%    | 69.4%     | 74.2%  |
| DNN   | 81.1%    | 75.5%     | 85.5%  |
| LSTM  | 86.5%    | 87.8%     | 85.5%  |
  
The dataset was split into 64% - 16% - 20% training/validation/test set.

