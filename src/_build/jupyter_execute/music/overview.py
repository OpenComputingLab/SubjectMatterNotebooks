# Music Overview

The *music* topic area is rich in opportunity for the creation of one piece production workflows. A computational representation of a piece of music can be created within the body of the document and then rendered as sheet music. The same musical object can be used to generate audio files that can be play the piece of music via an embedded audio player.

If required, created audio files can be converted to waveforms that can be analysed using a variety of signal processing techniques.

## `music21`

The [`music21`](https://web.mit.edu/music21/) package provides a wide ranging toolkit for computer-aided musicology. 

%%capture
try:
    import music21
except:
    %pip install --upgrade music21

Import packages from `music21`:

from music21 import *

### Create a simple score using *TinyNotation*

[*TinyNotation*](http://web.mit.edu/music21/doc/usersGuide/usersGuide_16_tinyNotation.html) is a simple notation for representing music.

Whilst *TinyNotation* may be be appropriate for representing complex pieces of music, the straightforward syntax provides a veery quick and easy way creating a simple piece of music.

from music21 import converter

s = converter.parse('tinyNotation: 4/4 C4 D2 E4 F4 G4 A4 B4 c4')
s.show()

Other visualisations of the music are also possible. For example, we can look at the pitch and note length:

s.plot()

Or analyse the key:

s.plot('key')

We can listen to the same piece of music creating a MIDI file from it and passing that file to an embedded audio player:

s.show('midi')

### Constructing Music From Primitives

If we need more control over the music, we can construct things like chords directly:

from music21 import chord

c = chord.Chord("C4 E4 G4")
c

We can render the object visually as piece of music:

c.show()

Or listen to it:

c.show('midi')

We can test for particular musical properties of the object:

c.isConsonant()

## Access to Scores

The `music21` includes a wide corpus of scores that we can work with without having to download any additional files:

from music21 import corpus

corpus.getPaths()[:3]

Select a random piece:

import random

selected_piece = random.choice(corpus.getPaths())

p = corpus.parse(selected_piece)

p.show()

Metadata is associated with each piece that we can extract directly:

p.metadata.title, p.metadata.composer

We can load in a piece by known reference:



myBach = corpus.parse('bach/bwv57.8')
alto = myBach.parts['Alto']

alto.show()

As you might expect, we can also listen to the piece:

alto.show('midi')

### Searching Through Scores

We can search through these scores to find a piece of music that we can then use within the notebook.

For example, we can search by composer:

a = [c for c in corpus.search('carolan', 'composer')]
a[0].metadata.all()

Searches return a metadata bundle, which cas also be search within by chaining the search queries:

c = corpus.search('carolan', 'composer').search('Princess Royal', 'title')

c[0].parse().show()

c[0].show('midi')

### Viewing Part of a Score

When discussing a particular piece, we may want to focus on particular parts of it. We can reference into particular measures and just focus on those. For example, suppose we want to just inspect the opening measures of a piece:

c[0].parse().measures(0,4).show()

Visualising the pitch and duration of notes in the opening:

c[0].parse().measures(0,4).plot()

## Converting Midi Files to Audio Files

We can convert a MIDI file to an audio file (eg a `.wav` file) using the [*fluisynth*](https://www.fluidsynth.org/) cross-platfrom command line application.

This application also requires the installation of a [soundfont](https://github.com/FluidSynth/fluidsynth/wiki/SoundFont) such as the [*GeneralUser* soundfont](http://www.schristiancollins.com/generaluser.php ).

#  fluidsynth: https://www.fluidsynth.org/
#!brew install fluidsynth
# Requires a soundfont: https://github.com/FluidSynth/fluidsynth/wiki/SoundFont -> https://www.dropbox.com/s/4x27l49kxcwamp5/GeneralUser_GS_1.471.zip?dl=1
#http://www.schristiancollins.com/generaluser.php 
#%pip install git+https://github.com/nwhitehead/pyfluidsynth.git

The following utility function will handle the conversion for us:

#Based on: https://gist.github.com/devonbryant/1810984
import os
import subprocess

def to_audio(midi_file, sf2="GeneralUser/GeneralUser.sf2",
             out_dir=".", out_type='wav', txt_file=None, append=True):
    """ 
    Convert a single midi file to an audio file.  If a text file is specified,
    the first line of text in the file will be used in the name of the output
    audio file.  For example, with a MIDI file named '01.mid' and a text file
    with 'A    major', the output audio file would be 'A_major_01.wav'.  If
    append is false, the output name will just use the text (e.g. 'A_major.wav')
    
    Args:
        midi_file (str):  the file path for the .mid midi file to convert
        sf2 (str):        the file path for a .sf2 soundfont file
        out_dir (str):    the directory path for where to write the audio out
        out_type (str):   the output audio type (see 'fluidsynth -T help' for options)
        txt_file (str):   optional text file with additional information of how to name 
                          the output file
        append (bool):    whether or not to append the optional text to the original
                          .mid file name or replace it
    """
    fbase = os.path.splitext(os.path.basename(midi_file))[0]
    if not txt_file:
        out_file = out_dir + '/' + fbase + '.' + out_type
    else:
        line = 'out'
        with open(txt_file, 'r') as f:
            line = re.sub(r'\s', '_', f.readline().strip())
            
        if append:
            out_file = out_dir + '/' + line + '_' + fbase + '.' + out_type
        else:
            out_file = out_dir + '/' + line + '.' + out_type

    subprocess.call(['fluidsynth', '-T', out_type, '-F', out_file, '-ni', sf2, midi_file])

Pass the name of the sound file and create a `.wav` file:

to_audio("alto.mid")

We can now embed an audio player to play the wav file:

from IPython.display import Audio

Audio("alto.wav")

### Visualising Audio Files

Haiving got an audio file representation, we can then process it as a sound file. For example, we can look at the waveform: 

from scipy.io import wavfile
%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np

samplerate, data = wavfile.read('alto.wav')

times = np.arange(len(data)/float(samplerate))

plt.plot(data[:4000]);

### `abc.js`

[`abc.js`](https://github.com/paulrosen/abcjs) is a simple notatin and Javascript rendered for working with music.

We can use a simple IPython cell block magic to allow us to write and render `abc.js` scores:

#https://github.com/akaihola/jupyter_abc
%%capture
try:
    %load_ext jupyter_abc
except:
    %pip install git+https://github.com/akaihola/jupyter_abc.git

%reload_ext jupyter_abc

%%abc
%%score (R1 R2) (L)
X: 1
T: Blue Bells of Scotland
M: 4/4
L: 1/8
K: C
V:R
G2|c4B2A2|G4A2Bc|z8|z4z2G2|
V:L
z2|z8|z8|E2E2E2D2|C6z2|
V:R
|c4B2A2|G4A2Bc|z8|z8|
V:L
|z8|z8|E2E2F2D2|C6G2|
V:R
z8|c4G2Bc|B2G2A2B2|G4A2B2|
V:L
E2C2E2G2|z8|z8|z8|
V:R
c4B2A2|G4A2Bc|z8|z6|]
V:L
z8|z8|E2E2F2D2|C6|]

The `music21` package is also capable of parsing `abcjs` notation in a saved file:

abcjs = '''
X: 1
T: Blue Bells of Scotland
M: 4/4
L: 1/8
K: C
V:R
G2|c4B2A2|G4A2Bc|z8|z4z2G2|
V:L
z2|z8|z8|E2E2E2D2|C6z2|
V:R
|c4B2A2|G4A2Bc|z8|z8|
V:L
|z8|z8|E2E2F2D2|C6G2|
V:R
z8|c4G2Bc|B2G2A2B2|G4A2B2|
V:L
E2C2E2G2|z8|z8|z8|
V:R
c4B2A2|G4A2Bc|z8|z6|]
V:L
z8|z8|E2E2F2D2|C6|]
'''

abc_fn = 'demo.abc'
with open(abc_fn, 'w') as outfile:
    outfile.write(abcjs)

Simply use the `music21.converter.parse()` function with the file name:

converter.parse(abc_fn).show()

