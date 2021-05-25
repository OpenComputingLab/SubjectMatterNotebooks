%%capture
try:
    import poliastro
except:
    %pip install --upgrade https://github.com/poliastro/poliastro/archive/main.zip

from poliastro.bodies import Earth, Sun

from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris
solar_system_ephemeris.set("jpl")

EPOCH = Time("2021-05-21 12:05:50", scale="tdb")

Earth.plot(EPOCH);

from poliastro.plotting.misc import plot_solar_system

plot_solar_system(epoch=EPOCH);

from poliastro.examples import molniya

molniya.plot();

from astropy import units as u

from poliastro.twobody import Orbit

# Data from Curtis, example 4.3
r = [-6045, -3490, 2500] * u.km
v = [-3.457, 6.618, 2.533] * u.km / u.s

orb = Orbit.from_vectors(Earth, r, v)

orb

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

from poliastro.examples import churi, iss

churi.plot(interactive=True, use_3d=True)

from poliastro.plotting import OrbitPlotter3D

frame = OrbitPlotter3D()

frame.plot(molniya)
frame.plot(iss)

%%capture
try:
    import ephem
except:
    %pip install --no-cache pyephem

import ephem
import numpy as np

#Define an observer
obs = ephem.city('London')

#Get current time
ephem.localtime(obs.date).strftime("%Y-%m-%d %H:%M")

sol = ephem.Sun()

sol.compute(obs)

print(obs.next_setting(sol, use_center=True))
print(obs.next_rising(sol, use_center=True))

#Plotting the altitude

# For example, this could perhaps be used as a the basis for a student exercise
# in which students learn how to plot the altitude of various bodies relative to various
# locations on various dates
# Other flavours of exercise are also possible.
# For example, a parameter sweep where you try to optimise or learn something about
# the altitude of a body from a particular location over a range of dates?
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