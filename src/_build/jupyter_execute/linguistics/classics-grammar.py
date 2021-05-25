# Classical Languages — Grammar

When discussing and analysing texts in terms of grammar, a one piece generative document workflow provides us with a means for reducing the number of errors in terms of incorrectly presented matters of fact (for example, the analysis of a specific piece of text).

For example, inflection patterns of arbitrary regular verbs and nouns can be generated directly for a particular root word (lemma), or when analysing the syllabic structure of a peice of text.

Where the means of production are shared with learners, the ability to check declensions and conjugations for arbitrary words, or analyse a text for its syllabic structure, provides an opportunity to support curiosty driven, self-directed learning.

To provide a few examples of what's possible, let's use the `cltk` package and expore some simple Latix texts.

from cltk.data.fetch import FetchCorpus
corpus_downloader = FetchCorpus('lat')
path = '/Users/tonyhirst/cltk_data/lat/text/lat_text_latin_library'

corpus_downloader.import_corpus('lat_models_cltk')

## Inflection Patterns 

We can automatically generate the inflection (declension / conjugation) for a given word / lemma.

*(Lemma - "the canonical form of an inflected word".)*

The morphological character of a word is encoded using a nine character code string (- is used as the null character):

 	1: 	part of speech
 		n	noun
 		v	verb
 		t	participle
 		a	adjective
 		d	adverb
 		c	conjunction
 		r	preposition
 		p	pronoun
 		m	numeral
 		i	interjection
 		e	exclamation
 		u	punctuation
 	2: 	person
 		1	first person
 		2	second person
 		3	third person
 	3: 	number
 		s	singular
 		p	plural
 	4: 	tense
 		p	present
 		i	imperfect
 		r	perfect
 		l	pluperfect
 		t	future perfect
 		f	future
 	5: 	mood
 		i	indicative
 		s	subjunctive
 		n	infinitive
 		m	imperative
 		p	participle
 		d	gerund
 		g	gerundive
 		u	supine
 	6: 	voice
 		a	active
 		p	passive
 	7:	gender
 		m	masculine
 		f	feminine
 		n	neuter
 	8: 	case
 		n	nominative
 		g	genitive
 		d	dative
 		a	accusative
 		b	ablative
 		v	vocative
 		l	locative
 	9: 	degree
 		c	comparative
 		s	superlative
 
Via: https://github.com/cltk/latin_treebank_perseus#readme

Consider *amo*. How does it go?

from cltk.morphology.lat import CollatinusDecliner
decliner = CollatinusDecliner()

decliner.decline("amo")[:20]

Or how anout *canis*?

decliner.decline("canis")

We can decode the strings to more easily describe the morphological character of a word.

#Taken from https://github.com/alpheios-project/pyperseus-treebank/blob/master/pyperseus_treebank/latin.py#L44#
#Maybe use https://github.com/jazzband/inflect for natural language code2text description?
import re

# Conversion table for CONLL
# Thanks to @epageperron
#??Some divergence from README?
_CONLL_LA_CONV_DICT = { "a": "adjective", "c": "conjunction",
                        "d": "adverb", "e": "exclamation", "g": "PART",
                        "i": "interjection", "l": "DET",
                        "m": "numeral", "n": "noun","p": "pronoun",
                        "r": "preposition", "t": "VERB", "u": "punctuation",
                        "v": "verb", "x": "X" }

_NUMBER = {"s": "singular", "p": "plural"}
_TENSE = {"p": "present", "f": "future", "r": "perfect", "l": "pluperfect",
          "i": "imperfect", "t": "future perfect"}
_MOOD = {"i": "indicative", "s": "subjunctive", "m": "imperative", 'd':'gerund',
         "g": "gerundive", "p": "participle", "u": "supine", "n": "infinitive"}
_VOICE = {"a": "active", "p": "passive", "d": "Dep"}
_GENDER = {"f": "feminine", "m": "masculine", "n": "neuter", "c": "Com"}
_CASE = {"g": "genitive", "d": "dative", "a": "accusative", "v": "vocative",
         "n": "nominative", "b": "ablative", "i": "Ins", "l": "locative"}
_DEGREE = {"p": "Pos", "c": "comparative", "s": "superlative"}

_PERSON = {"1":'first person', "2":'second person', "3":'third person'}

NOTWORD = re.compile("^\W+$")

_NULL_CHAR="-"

def parse_features(features):
    """ Parse features from the POSTAG of Perseus Latin XML
    .. example :: self.parse_features("n-p---na-")
    :param features: A string containing morphological informations
    :type features: str
    :return: Parsed features
    :rtype: dict
    """

    if features is None or features.lower()=='unk':
        return {}
    
    features = features.lower()
    
    feats = {}

    feats['POS'] = _CONLL_LA_CONV_DICT[features[0]]

    # Person handling : 3 possibilities
    if features[1] != _NULL_CHAR:
        feats["Person"] = _PERSON[features[1]]

    # Number handling : two possibilities
    if features[2] != _NULL_CHAR:
        feats["Number"] = _NUMBER[features[2]]

    # Tense
    if features[3] != _NULL_CHAR:
        feats["Tense"] = _TENSE[features[3]]

    # Mood
    if features[4] != _NULL_CHAR:
        feats["Mood"] = _MOOD[features[4]]

    # Voice
    if features[5] != _NULL_CHAR:
        feats["Voice"] = _VOICE[features[5]]

    # Tense
    if features[6] != _NULL_CHAR:
        feats["Gender"] = _GENDER[features[6]]

    # Tense
    if features[7] != _NULL_CHAR:
        feats["Case"] = _CASE[features[7]]

    # Degree
    if features[8] != _NULL_CHAR:
        feats["Degree"] = _DEGREE[features[8]]

    return feats

For example, how should we interpret the following morphological data feature string?

#Example
parse_features('v3plia---')

Looking up words in the decliner provides a way of getting the morphological data for a word. For example, we could look up *amabitis* and get back something like `('amo', 'v2pfia---')`:

#hacky way that assumes you know the root
def lookupInflection(word, lemma):
    ''' Find the inflection of a given word, given its lemma. '''
    result=[]
    if lemma is None:
        return result
    
    lemma = [lemma] if isinstance(lemma,str) else lemma
    for l in lemma:
        try:
            words = decliner.decline(l)
            result.append([(w,d) for w,d in words if w==word])
        except:
            result.append((l, None))
    return result

If we know the root, we can lookup the inflection:

lookupInflection('amabitis', 'amo')

## Lemmatizing a Word

Let's see if we can find the root of a word with a simple lemmatizer. The lemmatizer works with tokens, so we need a recipe for generating tokens out of words:

from cltk.tokenizers.lat.lat import LatinWordTokenizer

latin_word_tokenizer = LatinWordTokenizer()

latin_word_tokenizer.tokenize('amabitis')

If we create a lemmatizer:

from cltk.lemmatize.lat import LatinBackoffLemmatizer

latin_lemmatizer = LatinBackoffLemmatizer()

We can then see what it makes of *amabitis*:

latin_lemmatizer.lemmatize(latin_word_tokenizer.tokenize('amabitis'))

We can also lemmatize all the words in a sentence.

As before, we need to tokenize the words we present to the lemmatizer, so let's convert our sentence to a list of separate (word) tokens:

sentence = 'Progeniem sed enim Troiano a sanguine duci audierat'

sentence_tokens = latin_word_tokenizer.tokenize(sentence.lower())
sentence_tokens

Then we can lemmatize those tokens:

latin_lemmatizer.lemmatize(sentence_tokens)

We can also lemmatize Roman numerals:

from cltk.lemmatize.lat import RomanNumeralLemmatizer

#Lemmatizer for identifying roman numerals in Latin text based on regex.
lemmatizer = RomanNumeralLemmatizer()

lemmatizer.lemmatize("i ii iii iv v vi vii vii ix x xx xxx xl l lx c cc".split())

## Syllables

One way of helping students read a text is to split the syllables out.m

with open(f'{path}/vergil/aen1.txt') as f:
    aeneid_1 = f.read()

#Here's a manual way of doing a concordance, though we need to clean it for the tokeniser?
from cltk.alphabet.text_normalization import remove_non_ascii
from cltk.alphabet.text_normalization import remove_non_latin

aen1_clean = remove_non_ascii(aeneid_1)
aen1_clean = remove_non_latin(aen1_clean)
print(aen1_clean[:1000])

from nltk.text import Text

tokens = latin_word_tokenizer.tokenize(aen1_clean)
textList = Text(tokens)
textList.concordance('Libyae')

from cltk.languages.example_texts import get_example_text

example_lat = get_example_text('lat')
example_lat

from cltk.sentence.lat import LatinPunktSentenceTokenizer

latin_splitter = LatinPunktSentenceTokenizer()

sentences = latin_splitter.tokenize(example_lat)

sentences

from cltk.prosody.lat.syllabifier import Syllabifier

syllabifier = Syllabifier()

clean_sentence = remove_non_ascii(remove_non_latin(sentences[0])).lower()

#Extract syllables for each word
for word in latin_word_tokenizer.tokenize(clean_sentence):
    syllables = syllabifier.syllabify(word)
    print(word, syllables)

## Pipeline processing

from cltk import NLP
cltk_nlp = NLP(language="lat")

# This can be slow
# First run, prompts to allow download of Stanza NLP library models
# to ~/stanza_resources/la/ (~250MB)
# Also word embedding models from the Fasttext project to
# ~/cltk_data/lat/embeddings/fasttext 365MB
# Also Lewis's *An Elementary Latin Dictionary* (1890)
cltk_doc = cltk_nlp.analyze(text=example_lat)

cltk_doc.stanza_doc

# Also: cltk_doc.raw
cltk_doc.normalized_text

cltk_doc.sentences_strings

cltk_doc.sentences_tokens

[ p for p in zip(cltk_doc.tokens, cltk_doc.lemmata,
                 cltk_doc.pos, cltk_doc.morphosyntactic_features)]

