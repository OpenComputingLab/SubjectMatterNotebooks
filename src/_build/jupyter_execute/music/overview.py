# Music Overview

The *music* topic area is rich in opportunity for the creation of one piece production workflows. Musical scores can be created within the body of the document then rendered as sheet music as well audio files that can be played via an embedded audio player.

## `music21`

The [`music21`](https://web.mit.edu/music21/) package provides a wide ranging toolkit for computer-aided musicology. 

%%capture
try:
    import music21
except:
    %pip install --upgrade music21

from music21 import *

c = chord.Chord("C4 E4 G4")
c

c.show()

import os
from IPython.display import Audio

c = chord.Chord("C4 E4 G4")


c.show('midi')

from music21 import converter
s = converter.parse('tinyNotation: 4/4 C4 D4 E4 F4 G4 A4 B4 c4')
s.show()

s.show('midi')

## Tiny Notation

from music21 import chord

c = chord.Chord("C4 E4 G4")
c.isConsonant()

c.show()

from music21 import converter

s = converter.parse('tinyNotation: 4/4 C4 D4 E4 F4 G4 A4 B4 c4')

s.show()

from music21 import corpus

myBach = corpus.parse('bach/bwv57.8')
alto = myBach.parts['Alto']

alto.show()

alto.show('midi')

