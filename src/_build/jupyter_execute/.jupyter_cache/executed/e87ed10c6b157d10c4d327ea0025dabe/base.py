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

aladin.target='M82'

aladin.fov=0.3

aladin.show_layers_control=True

aladin.survey = 'P/2MASS/color'

from astroquery.simbad import Simbad

table = Simbad.query_region("M82", radius="4 arcmin")

aladin.add_table(table)

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

wwt.constellation_boundaries = True

wwt.constellation_figures = True

wwt.available_layers[:5]

from astropy import units as u
from astropy.coordinates import SkyCoord

coord = SkyCoord.from_name('Alpha Centauri')
wwt.center_on_coordinates(coord, fov=10 * u.deg)

wwt.background = wwt.imagery.gamma.fermi
wwt.foreground = wwt.imagery.other.planck
wwt.foreground_opacity = .75

wwt.layer_controls

wwt.available_views

wwt.set_view('jupiter')

wwt.set_view('milky way')

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