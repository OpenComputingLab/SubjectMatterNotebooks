# Classical Languages

Some tools to support classics related subject matter, such as retrieving classical texts and searching throuhg them, analysing grammar, inflectng words (declensions, conjugations).

The intention, as with the other notebooks in this collection, is to explore ways in which we might create educational resources that are "reproducible with modification" through making available the means of production of various analyses, diagrams, etc along with the produced resource.

A secondary benefit is that by automating the generation of particular assets or examples, it becomes easier for authors to make use of them, which may open up new teaching lines. A tertiary benefit is that learners may use the same production methods to allow them to explore the topics themselves.

## `cltk`

[`cltk`](https://github.com/cltk/cltk), the *[Classical Language Toolkit*](http://cltk.org/), is a natural language processing (NLP) package designed for use with the languages of Ancient, Classical, and Medieval Eurasia (esp. Greek and Latin). I assume it is based on nltk.

A selection of tutorial notebooks can be found at cltk/tutorials.

cltk provides access to a variety of classical texts in a variety of languages, and as such provides a way for learners to access such texts themselves, if we can find a way of accessing a reliable index to them, or search through metadata provided for them.

The natural language processing tools in the package make it easy to search texts, as well as analyse them in some languages.

There are also language specific tools, such as a declension generator in Latin, that might be useful for helping check declensions and conjugations, or display particular person/tense combinations for a particular word.

OpenLearn units to explore:

- [Discovering Acient Greek and Latin](http://www.open.edu/openlearn/history-the-arts/discovering-ancient-greek-and-latin/content-section-0?active-tab=description-tab)
- [Getting started on classical Latin](http://www.open.edu/openlearn/history-the-arts/getting-started-on-classical-latin/content-section-0?active-tab=description-tab)
- [Continuing classical Latin](http://www.open.edu/openlearn/history-the-arts/history/classical-studies/continuing-classical-latin/content-section-0?active-tab=description-tab)

%%capture
try:
    import cltk
except:
    %pip install matplotlib
    %pip install cltk

```{note}
Corproa in a wide range of classical languages are available. For a list, see [here](https://docs.cltk.org/en/latest/languages.html).
```

We can obtain a list of available Ancient Greek corpora:

from cltk.data.fetch import FetchCorpus

FetchCorpus('grc').list_corpora  # Latin: lat, Greek: grc

Or Latin corpora:

corpus_downloader = FetchCorpus('lat')
corpus_downloader.list_corpora

We can download a corpus from the list of available corpora associated with the selected language:

corpus_downloader.import_corpus('lat_text_latin_library')

```{note}
By default, the data is download to `~/cltk_data`

If we download the Latin corpora, we can find corpus files in:

`~/cltk_data/lat/text/lat_text_latin_library/`
```

from cltk import NLP

# Load the default Pipeline for Latin
cltk_nlp = NLP(language="lat")

cltk_nlp.pipeline.processes

path="/Users/tonyhirst/cltk_data/lat/text/lat_text_latin_library/vergil/aen1.txt"

with open(path) as f:
    aeneid_1 = f.read()

aeneid_1[1000:1200]

