# Astronomy — Interactive Viewers

Several interactive widgets are available that allow interactive exploration of various astronomical image collections.


```{warning}
Many interactive `ipywidgets` will only work in the context of a live notebook.
```

## `ipyaladin`

%%capture
try:
    import ipyaladin
except:
    %pip install ipyaladin
    %pip install astroquery
    !jupyter nbextension enable --py widgetsnbextension
    !jupyter nbextension enable --py --sys-prefix ipyaladin

import ipyaladin as ipyal

aladin= ipyal.Aladin(target='messier 51', fov=1)

# When using this in an interactive notebook,
# we can use https://github.com/innovationOUtside/nb_cell_dialog extension
# to pop the cell or cell ouput out into a floating widget 
# rather than have it anchored in a fixed place in the linear flow of a notebook
aladin

```{note}
If the [`nb_cell_dialog`](https://github.com/innovationOUtside/nb_cell_dialog) extension is installed, the widget can be popped out of the code cell output area and into its own floating widget. This allows the widget to remain in view as commands are issued throughout the notebook to change the WWT view rendered by it.
```

Set a new target object by name:

aladin.target='M82'

Set the zoom level:

aladin.fov=0.3

Enable the layers control in the widget:

aladin.show_layers_control=True

Set a layer explicitly:

aladin.survey = 'P/2MASS/color'

Look up objects in a particular area:

from astroquery.simbad import Simbad

table = Simbad.query_region("M82", radius="4 arcmin")

And overlay objects on the image in the widget viewer:

aladin.add_table(table)

## `pywwt`

The [`pywwt`](https://pywwt.readthedocs.io/en/stable/settings.html) package provides an interactive widget for making observations using the [AAS World Wide Telescope](http://www.worldwidetelescope.org/home/), a suite of tools that provide access to a wide variety of astronomical visualisations.

Start by loading the default widget:

%%capture
try:
    import pywwt
except:
    %pip install pywwt
    !jupyter nbextension install --py --symlink --sys-prefix pywwt
    !jupyter nbextension enable --py --sys-prefix pywwt
    !jupyter serverextension enable --py --sys-prefix pywwt
    %pip install git+https://github.com/innovationOUtside/nb_cell_dialog.git

from pywwt.jupyter import WWTJupyterWidget

wwt = WWTJupyterWidget()

# When using this in an interactive notebook,
# we can use https://github.com/innovationOUtside/nb_cell_dialog extension
# to pop the cell or cell ouput out into a floating widget 
# rather than have it anchored in a fixed place in the linear flow of a notebook
wwt

A series of code cell commands then configure the view displayed by the widget.

```{note}
If the [`nb_cell_dialog`](https://github.com/innovationOUtside/nb_cell_dialog) extension is installed, the widget can be popped out of the code cell output area and into its own floating widget. This allows the widget to remain in view as commands are issued throughout the notebook to change the WWT view rendered by it.
```

Enable constellation boundaries:

wwt.constellation_boundaries = True

Enable constellation figures:

wwt.constellation_figures = True

View telescope layers that are available:

wwt.available_layers[:5]

Bring a particular object into view at a specified magnification:

from astropy import units as u
from astropy.coordinates import SkyCoord

coord = SkyCoord.from_name('Alpha Centauri')
wwt.center_on_coordinates(coord, fov=10 * u.deg)

Enable foreground and background layers:

wwt.background = wwt.imagery.gamma.fermi
wwt.foreground = wwt.imagery.other.planck
wwt.foreground_opacity = .75

Foreground and background layer views, and the relative opoacity, can also be controlled via interactive widgets:

wwt.layer_controls

## Change of View

Onservations can be rendered for particular views:

wwt.available_views

For example, we can view Saturn:

wwt.set_view('jupiter')

Or the whole Milky Way:

wwt.set_view('milky way')

We can also draw constellations:

from astropy import units as u
from astropy.coordinates import concatenate, SkyCoord

bd = concatenate((SkyCoord.from_name('Alkaid'),  # stars in Big Dipper
                  SkyCoord.from_name('Mizar'),
                  SkyCoord.from_name('Alioth'),
                  SkyCoord.from_name('Megrez'),
                  SkyCoord.from_name('Phecda'),
                  SkyCoord.from_name('Merak'),
                  SkyCoord.from_name('Dubhe')))

wwt.center_on_coordinates(SkyCoord.from_name('Megrez'))
line = wwt.add_line(bd, width=3 * u.pixel)

A particular view can be save as an HTML bundle with the command: `wwt.save_as_html_bundle()`