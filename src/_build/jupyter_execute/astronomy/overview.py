# Astronomy Overview

#%pip install astropy

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

