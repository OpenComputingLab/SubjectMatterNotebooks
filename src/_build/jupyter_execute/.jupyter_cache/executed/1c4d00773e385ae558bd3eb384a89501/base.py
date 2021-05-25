%%capture
try:
    import cltk
except:
    %pip install matplotlib
    %pip install cltk

import cltk

cltk.languages.utils.find_iso_name('Middle English')

from cltk.languages.glottolog import LANGUAGES

for l in list(LANGUAGES)[:10]:
    print(f'{LANGUAGES[l].name} ({l}) [{LANGUAGES[l].latitude}, {LANGUAGES[l].longitude}]')

import folium

m = folium.Map()

for lang in list(LANGUAGES):
    folium.Marker(location=[LANGUAGES[lang].latitude, LANGUAGES[lang].longitude],
                            popup=f'{LANGUAGES[lang].name} (iso-code: {lang})').add_to(m)

m

# Pipelines are also supported for processing certain specific languages
from cltk.nlp import iso_to_pipeline
iso_to_pipeline

from cltk.languages.example_texts import get_example_text

get_example_text('lat')

get_example_text('grc')

from cltk.data.fetch import FetchCorpus

FetchCorpus('grc').list_corpora  # Latin: lat, Greek: grc

corpus_downloader = FetchCorpus('lat')
corpus_downloader.list_corpora

corpus_downloader.import_corpus('lat_text_latin_library')

from cltk import NLP

# Load the default Pipeline for Latin
cltk_nlp = NLP(language="lat")

cltk_nlp.pipeline.processes

path = '/Users/tonyhirst/cltk_data/lat/text/lat_text_latin_library'
!ls $path/vergil

with open(f'{path}/vergil/aen1.txt') as f:
    aeneid_1 = f.read()

print(aeneid_1[1000:1200])