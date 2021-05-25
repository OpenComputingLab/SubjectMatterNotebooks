%%capture
try:
    import chemlib
except:
    %pip install chemlib

from chemlib import Element

silicon = Element('Si')
silicon.properties

from chemlib import chemistry

chemistry.pte.head()

from chemlib import Compound

water = Compound("H2O")

water.coefficient, water.elements, water.formula, water.get_amounts(grams = 2), \
water.get_amounts(molecules = 2e+24), \
water.molar_mass(), water.occurences, water.percentage_by_mass('H')

#Get the empirical formula of a compound that is composed of 80.6% C, and 19.4% H by mass:

from chemlib import empirical_formula_by_percent_comp as efbpc
efbpc(C = 80.6, H = 19.4)

from chemlib import Compound, Reaction

N2O5 = Compound("N2O5")
H2O = Compound("H2O")
HNO3 = Compound("HNO3")
r = Reaction([N2O5, H2O], [HNO3])
r.formula, r.is_balanced, r.balance(), r.formula

r.coefficients, r.constituents

subscript = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")

r.product_formulas[0].translate(subscript)

r.reactant_formulas, r.product_formulas

from chemlib import Compound, Combustion

methane = Compound('CH4')
c = Combustion(methane)
c.formula, c.is_balanced

c.formula, c.is_balanced

#Currently broken
#from chemlib import Galvanic_Cell
#g = Galvanic_Cell("Pb", "Zn")

%%capture
try:
    import pymatgen
except:
    %pip install pymatgen

import pymatgen.core as mgc

si = mgc.Element('Si')

si.atomic_mass, si.melting_point, si.boiling_point

for p in ['alkali', 'halogen', 'lanthanoid', 'metalloid', 'noble_gas', 'quadrupolar', \
    'rare_earth_metal', 'transition_metal']:
    print(f"{p}: {getattr(si, 'is_'+p)}")

si.value, si.valence, si.row, si.number, si.group

si.full_electronic_structure

comp = mgc.Composition('Fe2O3')

for p in ['is_element', 'weight','num_atoms', 'elements']:
    print(f"{p}: {getattr(comp, p)}")

for f in ["formula", "alphabetical_formula", "reduced_formula",
          "hill_formula","element_composition",  "reduced_composition"]:
    print(f"{f}: {getattr(comp, f)}")

comp.fractional_composition,  comp.get_atomic_fraction('Fe'),  comp.get_atomic_fraction('O')

comp.total_electrons, comp.weight

mgc.Element.print_periodic_table()

mgc.Element.from_row_and_group(3, 14)

%%capture
#https://github.com/osscar-org/widget-periodictable/
try:
    import widget_periodictable
except:
    %pip install widget_periodictable
    !jupyter nbextension enable --py widget_periodictable

from widget_periodictable import PTableWidget

widget = PTableWidget(states = 3, selected_elements = {"C": 0, "Si": 1, "Ge": 2}, 
                      selected_colors = ['pink', 'yellow', 'lightblue'], 
                      disabled_elements = ['B', 'Al', 'Ga'],
                      unselected_color='white', border_color = 'black', width = '20px')
display(widget)

%%capture
try:
    import mendeleev
except:
    %pip install mendeleev

from mendeleev import Si, Fe, O

print("Si's name: ", Si.name)
print("Fe's atomic number:", Fe.atomic_number)
print("O's atomic weight: ", O.atomic_weight)

from mendeleev import element

si, al,o  = [element('Si'), element(13), element('Oxygen') ]
si.name, al.name,o.name, al.oxistates

for iso in Fe.isotopes:
    print('{0:4d} {1:4d} {2:10.5f} {3:8.2e} {4:6.2f} {5:}'.format(
        iso.atomic_number, iso.mass_number, iso.mass, iso.mass_uncertainty, iso.abundance * 100.0, iso.is_radioactive))

%%capture
try:
    import bokeh
except:
    %pip install bokeh

from bokeh.plotting import output_notebook, output_file
# Note that the periodic table widget will still render in a Jupyter Book display
output_notebook()

from mendeleev.fetch import fetch_table
from mendeleev.plotting import periodic_plot

ptable = fetch_table('elements')
periodic_plot(ptable)

periodic_plot(ptable, colorby='jmol_color', title="JMol Colors", decimals=3, width=700)
#periodic_plot(ptable, colorby='cpk_color', title='CPK Colors')
#periodic_plot(ptable, colorby='molcas_gv_color', title='MOLCAS GV Colors')

import seaborn as sns
from matplotlib import colors

blockcmap = {b : colors.rgb2hex(c) for b, c in zip(['s', 'p', 'd', 'f'], sns.color_palette('deep'))}
ptable['block_color'] = ptable['block'].map(blockcmap)

periodic_plot(ptable, colorby='block_color',
              width=700)

periodic_plot(ptable, attribute='covalent_radius_pyykko',
              colorby='attribute', title="Covalent Radii of Pyykko",
              width=700)

