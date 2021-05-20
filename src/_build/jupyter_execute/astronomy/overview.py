# Astronomy Overview

A wide range of tools are available for obtaining and working with a huge variety of astronomy related images and datasets, as well as performing astronomical calculations.

The complex and exact nature of the subject matter means that being able to script the generation and inclusion of assets into our teaching materials as part of a one piece production workflow is likely to reduce chances of mismatches when assembling publication ready documents.

## `astropy`

The [`astropy`](https://www.astropy.org/) package provides *"a common core package for Astronomy in Python"* with the intention of fostering *"an ecosystem of interoperable astronomy packages"*.

%%capture
try:
    import astropy
except:
    %pip install astropy

Let's start with an example of dowloading an image file in the FITS format from an known location:

from astropy.utils.data import download_file
from astropy.io import fits

horsehead_url = 'http://data.astropy.org/tutorials/FITS-images/HorseHead.fits'

#image_file is the path the downloaded and locally stashed file
image_file = download_file(horsehead_url, cache=True )
image_file

```{note}
FITS, the [Flexible Image Transport System](https://fits.gsfc.nasa.gov/), is an open standard digital file format widely used in astronomy for representing and working with 2D images. 
```

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

