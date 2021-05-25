%%capture
try:
    import astropy
except:
    %pip install astropy

from astropy.utils.data import download_file
from astropy.io import fits

horsehead_url = 'http://data.astropy.org/tutorials/FITS-images/HorseHead.fits'

#image_file is the path the downloaded and locally stashed file
image_file = download_file(horsehead_url, cache=True )
image_file

hdu_list = fits.open(image_file)
#hdu_list.info()

#save file under another name in the local directory: hh.fits
import os

if 'hh.fits' not in os.listdir():
    hdu_list.writeto('hh.fits')

import matplotlib.pyplot as plt

#Nice styling
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

image_data = fits.getdata('hh.fits')

#Display the image
plt.imshow(image_data, cmap='gray')
plt.colorbar();

%%capture
try:
    import aplpy
except:
    %pip install astropy
    %pip install git+https://github.com/astropy/pyregion.git
    %pip install aplpy 

import aplpy

hh = aplpy.FITSFigure('hh.fits')
hh.show_colorscale()

# Close the previous image session
hh.close()

hh = aplpy.FITSFigure('hh.fits')
hh.show_grayscale()

hh.close()

from astropy import coordinates

hh = aplpy.FITSFigure('hh.fits')
hh.show_grayscale()

# We can lookup data for astronomical objects by name
HORSEHEAD_NEBULA = 'Horsehead Nebula'

horsehead = coordinates.SkyCoord.from_name(HORSEHEAD_NEBULA)
hh.show_markers(horsehead.ra.deg, horsehead.dec.deg, marker='D', c='yellow')

hh.close()

%%capture
try:
    from astroquery.skyview import SkyView
except:
    %pip install astropy astroquery

from astroquery.simbad import Simbad

result_table = Simbad.query_object("Horsehead nebula")

result_table.to_pandas().T

from astroquery.skyview import SkyView

hh2_images = SkyView.get_images(position=HORSEHEAD_NEBULA,
                                survey=['2MASS-K'], pixels=1500)

hh2_images

import os

out_file = 'hh2.fits'

if not os.path.isfile(out_file):
    hh2_images[0].writeto(out_file)

hh2 = aplpy.FITSFigure(out_file)
hh2.show_grayscale()

hh2.close()

%%capture
try:
    import astrowidgets
except:
    %pip install astrowidgets 

from astrowidgets import ImageWidget

image = ImageWidget()

image

image.load_fits(out_file)

from astropy.coordinates import SkyCoord

image.center_on(SkyCoord.from_name(HORSEHEAD_NEBULA))
image.zoom_level = 2

%%capture
try:
    import sunpy.map
except:
    %pip install sunpy

import sunpy.data.sample
import sunpy.map

aia = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
aia.peek()

import matplotlib.pyplot as plt

import sunpy.map

def plot_image(imagefile, limb=False, grid=True, colorbar=True):
    ''' Quick function to help display of solar images. '''
    fig = plt.figure()
    
    m = sunpy.map.Map(imagefile)
    #ax = plt.subplot(111, projection=m)
    m.plot()
    
    if limb:
        m.draw_limb()
    if grid:
        m.draw_grid()
    if colorbar:
        plt.colorbar()

    plt.title=None
    plt.show()

plot_image(sunpy.data.sample.AIA_171_IMAGE)

plot_image(sunpy.data.sample.AIA_193_CUTOUT01_IMAGE,
           colorbar=False, grid=False)