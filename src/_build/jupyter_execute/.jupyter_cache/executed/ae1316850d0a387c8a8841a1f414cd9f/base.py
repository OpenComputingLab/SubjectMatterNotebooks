from lcapy import Circuit

cct = Circuit()
cct.add("""
Vi 1 0_1 step 20; down
C 1 2; right, size=1.5
R 2 0; down
W 0_1 0; right
W 0 0_2; right, size=0.5
P1 2_2 0_2; down
W 2 2_2;right, size=0.5""")
 
cct.draw(style='american')

from lcapy import R, C, L
 
cct2 = (R(1e6) + L(2e-3)) | C(3e-6)

cct2.draw()

cct2.sch()

# Or as a string: cct2.netlist()

cct2.netlist()

from lcapy import Circuit

# Create a file containing a circuit netlist
sch='''
Vi 1 0_1 {sin(t)}; down
R1 1 2 22e3; right, size=1.5
R2 2 0 1e3; down
P1 2_2 0_2; down, v=V_{o}
W 2 2_2; right, size=1.5
W 0_1 0; right
W 0 0_2; right
'''
 
fn="voltageDivider.sch"
with open(fn, "w") as text_file:
    text_file.write(sch)

# Create a circuit from a netlist file
netlist_cct = Circuit(fn)

netlist_cct.draw()

import numpy as np

t = np.linspace(0, 5, 1000)
vr = netlist_cct.R2.v.evaluate(t)

from matplotlib.pyplot import figure, savefig

fig = figure()
ax = fig.add_subplot(111, title='Resistor R2 voltage')

# The response voltage across R2
ax.plot(t, vr, linewidth=2)

# The input voltage, Vi
ax.plot(t, netlist_cct.Vi.v.evaluate(t), linewidth=2, color='red')

# The voltage aceoss R1
ax.plot(t, netlist_cct.R1.v.evaluate(t), linewidth=2, color='green')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Resistor voltage (V)');

from ipywidgets import interact

@interact(R=(1,10,1))
def response(R=1):
    cct = Circuit()

    cct.add('V 0_1 0 step 10;down')
    cct.add('L 0_1 0_2 1e-3;right')
    cct.add('C 0_2 1 1e-4;right')
    cct.add('R 1 0_4 {R};down'.format(R=R))
    cct.add('W 0_4 0; left')

    import numpy as np
    t = np.linspace(0, 0.01, 1000)
    vr = cct.R.v.evaluate(t)

    from matplotlib.pyplot import figure, savefig
    fig = figure()
    ax = fig.add_subplot(111, title='Resistor voltage (R={}$\Omega$)'.format(R))
    ax.plot(t, vr, linewidth=2)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Resistor voltage (V)')
    ax.grid(True)
    
    cct.draw()

from lcapy import Vstep, R, C, L
from numpy import linspace

underDampedRLC = Vstep(10) + R(0.1) + L(0.2, 0)+ C(0.4, 0)
underDampedRLC.draw();

t = linspace(0, 10, 1000)

underDampedRLC.Isc.transient_response().plot(t);

n = Vstep(20) + R(5) + C(10)
n.draw()

vf = linspace(0, 1, 4000)
n.Isc.frequency_response().plot(vf, log_scale=True);

@interact(R1=(0.1, 10),L1=(0.01, 1),C1=(0.01,0.5))
def damping(R1=0.1,L1=0.2,C1=0.4):
    underDampedRLC = Vstep(10) + R(R1) + L(L1)+ C(C1)
    underDampedRLC.draw();

    t = linspace(0, 10, 1000)

    underDampedRLC.Isc.transient_response().plot(t);

parallelR = R('R_1') | R('R_2')
parallelR.draw()


parallelR.simplify().R

parallelC = C('C_1') | C('C_2')
parallelC.draw()

parallelC.simplify().C

from IPython.display import Latex
# Hmmm, could we make some cell block magic for this

txt = f"The overall resistance value simplifies to: {parallelR.simplify().R._repr_latex_()}"

Latex( txt)

from lcapy import Vac, t, s, pi

#Representation of AC voltage source in time domain
#Vac(amplitude, phase)
Vac(20, pi/2).Voc(t)

#Representation of AC voltage source in s domain
Vac(20).Voc(s)

cct.draw()

f'{cct[0].V.s}, {cct[1].V.s}, {cct[2].V.s}'

cct[1].name

#pole-zero plot
from lcapy import s, j, transfer
from matplotlib.pyplot import savefig, show

H = transfer((s - 2) * (s + 3) / (s * (s - 2 * j) * (s + 2 * j)))
H.plot();

H

from lcapy import s, j, pi, f, transfer

from numpy import logspace
import matplotlib.pyplot as plt

H = transfer((s - 2) * (s + 3) / (s * (s - 2 * j) * (s + 2 * j)))

H(s), H(f), H(j * 2 * pi * f)

fv = logspace(-1, 3, 400)

# db vs frequency
H(f).dB.plot(fv, log_scale=True)

# Phase
H(f).phase_degrees.plot(fv,log_scale=True);

#%pip install control slycot
import control
import slycot # Makes for more efficent computation

control.tf([1,2,3], [4,5,6])


num = [[[1., 2.], [3., 4.]], [[5., 6.], [7., 8.]]]
den = [[[9., 8., 7.], [6., 5., 4.]], [[3., 2., 1.], [-1., -2., -3.]]]
sys1 = control.tf(num, den)

sys1

#State space system definition
sys = control.ss("1. -2; 3. -4", "5.; 7", "6. 8", "9.")

sys

sys.A

control.nyquist_plot(sys, omega=None, plot=True, color='b');

mag, phase, omega = control.bode(sys)

