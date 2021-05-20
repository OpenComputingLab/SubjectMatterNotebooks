# Astronomy — Ephemeris Data and Orbtial Calculations

Several packages exist that help us work out where things are in the sky, or how to calculate their orbits, or plot trajectories between them.

## `poliastro`

The [`poliastro`](https://docs.poliastro.space/en/stable/) package provides a range of tools to supprt interactive Astrodynamics and Orbital Mechanics activities.

%%capture
try:
    import poliastro
except:
    %pip install --upgrade https://github.com/poliastro/poliastro/archive/main.zip

For example, we can plot an orbit on a particular date:

from poliastro.bodies import Earth, Sun

from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris
solar_system_ephemeris.set("jpl")

EPOCH = Time("2021-05-21 12:05:50", scale="tdb")

Earth.plot(EPOCH);

Or the orbits and locations of planets in the solar system on a particular date:

from poliastro.plotting.misc import plot_solar_system

plot_solar_system(epoch=EPOCH);

We can plot the orbits of various named objects:

from poliastro.examples import molniya

molniya.plot();

We can also define our own orbits:

from astropy import units as u

from poliastro.twobody import Orbit

# Data from Curtis, example 4.3
r = [-6045, -3490, 2500] * u.km
v = [-3.457, 6.618, 2.533] * u.km / u.s

orb = Orbit.from_vectors(Earth, r, v)

orb

We can then plot a 2D representation of the orbit:

orb.plot();

from poliastro.plotting import StaticOrbitPlotter
from poliastro.frames import Planes

ganymed = Orbit.from_sbdb('1036') # Ganymed IAU number
amor = Orbit.from_sbdb('2001221') # Amor SPK-ID
eros = Orbit.from_sbdb('2000433') # Eros SPK-ID

#Play with the style and use a dark background
frame = StaticOrbitPlotter(plane=Planes.EARTH_ECLIPTIC, dark=True)

frame.plot(ganymed, label="Ganymed")
frame.plot(amor, label="Amor")
frame.plot(eros, label="Eros");

We can also render 3D interactive orbits from a demo model:

from poliastro.examples import churi, iss

churi.plot(interactive=True, use_3d=True)

Construct a view from two objects:

from poliastro.plotting import OrbitPlotter3D

frame = OrbitPlotter3D()

frame.plot(molniya)
frame.plot(iss)

## `pyephem`

[`pyephem`](http://rhodesmill.org/pyephem/) is a package that supports basic astronomical computations.

> Given a date and location on the Earth’s surface, it can compute the positions of the Sun and Moon, of the planets and their moons, and of any asteroids, comets, or earth satellites whose orbital elements the user can provide. Additional functions are provided to compute the angular separation between two objects in the sky, to determine the constellation in which an object lies, and to find the times at which an object rises, transits, and sets on a particular day.

Original examples based on: http://nbviewer.jupyter.org/url/www.sc.eso.org/~bdias/pycoffee/codes/20160908/pyephemexamples.ipynb

See also [`pysolar`](https://pysolar.readthedocs.io/en/latest/#examples) for calculating the intensity of solar radiation at different points of the Earth for particular datetimes.

%%capture
try:
    import ephem
except:
    %pip install --no-cache pyephem

What time is it in London?

import ephem
import numpy as np

#Define an observer
obs = ephem.city('London')

#Get current time
ephem.localtime(obs.date).strftime("%Y-%m-%d %H:%M")

When's the next sunset and sunrise?

sol = ephem.Sun()

sol.compute(obs)

print(obs.next_setting(sol, use_center=True))
print(obs.next_rising(sol, use_center=True))

#Plotting the altitude

#This sort of things could be easily reworked as the basis of an exercise
#  where students plot the altitude of various bodies relative to various
#  locations on various dates
#It could then provide the basis for a sweep where you try to optimise
#  something about the altitude from a particular location over a range of dates?
import matplotlib.pyplot as plt

def plotAltitude(obs, obj):
    resolution = 0.1
    datelist = [ephem.date(obs.date + x*ephem.hour) for x in np.arange(0,24,resolution)]
    positions = [0]*len(datelist)
    
    for i in range(len(datelist)):
        obs.date = datelist[i]
        obj.compute(obs)
        positions[i] = obj.alt*(180./3.1415)

    plt.plot(np.arange(0,24,resolution),positions,'-k')
    plt.gca().set_ylim(0,90)
    plt.gca().set_xlim(0,24)
    plt.xticks(np.arange(0,24),rotation='vertical')
    plt.gca().set_xticklabels([ephem.localtime(d).strftime("%H:%M") for d in datelist][::int(1/resolution)])
    plt.grid()
    plt.show()
    
plotAltitude(obs, sol)

moon = ephem.Moon()
plotAltitude(obs, moon)