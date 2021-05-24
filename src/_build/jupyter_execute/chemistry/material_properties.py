# Chemical Properties

Several packages exist that allow us to automatically retrieve material properties of particlar elments and compounds as well as relating them to the periodic table.

Being able to look up the material properties of chemicals in a one piece generative document workflow allows creators of materials to generate factually correct statements directly from looked up object properties and present those as part of the materials.

For learners in an interactive notebook, the ability to lookup and reference elements allows them to check their understanding and explore the properties of elements that have not been directly referenced in the materials.

The availability of a Periodic Table display with scripted styling means that authors can easily create views over the periodic table that highlight specific concerns, and learners can visually explore properties and patterns of elements in the periodic table context for themselves.

## `chemlib`

[`chemlib`](https://chemlib.readthedocs.io/en/latest/) is a Python package providing a wide range of functions for looking up simple chemical properties and working with simple reactions.

Reference: *H. R. Ambethkar, chemlib - A Python chemistry library , 2020-- . Available at: https://github.com/harirakul/chemlib.*

%%capture
try:
    import chemlib
except:
    %pip install chemlib

from chemlib import Element

silicon = Element('Si')
silicon.properties

A simple *pandas* dataframe summarising the periodic table properties of each element is also available as a summary table of this data over all elements:

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

## `pymatgen`

The [`pymatgen`](https://pymatgen.org/) (*Python Materials Genomics)* provides a wide range of utilities to support materials analysis.

Let's begin by importing the package:

%%capture
try:
    import pymatgen
except:
    %pip install pymatgen

import pymatgen.core as mgc

We can look up various properties of an individual element directly:

si = mgc.Element('Si')

si.atomic_mass, si.melting_point, si.boiling_point

We can also return Boolean flags that describe vrious other properties of a particular element. Such flags could trivially be used as part of a simple quiz, for example.

for p in ['alkali', 'halogen', 'lanthanoid', 'metalloid', 'noble_gas', 'quadrupolar', \
    'rare_earth_metal', 'transition_metal']:
    print(f"{p}: {getattr(si, 'is_'+p)}")

Valence properties as well as periodci table group and row number can be returned for each element:

si.value, si.valence, si.row, si.number, si.group

We can also retrieve the electronic structure of an element:

si.full_electronic_structure

As well as element lookups, we can also look-up properties of compounds based on their formula:

comp = mgc.Composition('Fe2O3')

for p in ['is_element', 'weight','num_atoms', 'elements']:
    print(f"{p}: {getattr(comp, p)}")

We can also explore variants on the formula:

for f in ["formula", "alphabetical_formula", "reduced_formula",
          "hill_formula","element_composition",  "reduced_composition"]:
    print(f"{f}: {getattr(comp, f)}")

We can also lookup the compostion of the compund:

comp.fractional_composition,  comp.get_atomic_fraction('Fe'),  comp.get_atomic_fraction('O')

The compound weight and basic electron structure can also be described:

comp.total_electrons, comp.weight

As well as individual elements and compounds, we can preview a simple text view of the periodic table:

mgc.Element.print_periodic_table()

We can also interrogate the periodic table structure, for example looking up elements by row and group:

mgc.Element.from_row_and_group(3, 14)

## Periodic Table

The [`widget_periodictable`](https://github.com/osscar-org/widget-periodictable/) is an interactive periodic table widget that allows particular elements to be highlighted and identifers for selected elements to be retrieved.

As such, wthe widget could form part of a simple end user application for looking up properties of selected elements, or highlighting elements within the table based on an analysis of a simple compound.

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

The periodic table widget can return symbols for selected elements, which means we could use it as an interface element for an automated lookup of various properties of selected items.

We can also use code to control which elements in the table are highlighted, we means we could also highlight elements in the table that may have been identified through some other lookup service. For example, highlight all the elements in the table contained in a particular compound.

## `mendeleev`

The [`mendeleev`](https://mendeleev.readthedocs.io/en/stable/tutorials.html#jupyter-notebooks) package provides "*an API for accessing various properties of elements from the periodic table of elements*".

%%capture
try:
    import mendeleev
except:
    %pip install mendeleev

For example, we can retrieve key properties associated with the elements referenced by the chemical symbol:

from mendeleev import Si, Fe, O

print("Si's name: ", Si.name)
print("Fe's atomic number:", Fe.atomic_number)
print("O's atomic weight: ", O.atomic_weight)

We can also reference elements by name and atomic number, as well as symbol:

```{note}
Note that we seem to get the American spelling of the name!
```

from mendeleev import element

si, al,o  = [element('Si'), element(13), element('Oxygen') ]
si.name, al.name,o.name, al.oxistates

As well as the basic elements, we can also look up isotopes:

for iso in Fe.isotopes:
    print('{0:4d} {1:4d} {2:10.5f} {3:8.2e} {4:6.2f} {5:}'.format(
        iso.atomic_number, iso.mass_number, iso.mass, iso.mass_uncertainty, iso.abundance * 100.0, iso.is_radioactive))

In addition to the simple API, the `medeleev` package also provides a rich interactive periodic table widget.

The widget has a depnedency on the Boken charting package, which must be loaded in and configured first:

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

We can also configure the periodic table display, for example, adding colour highlights:

periodic_plot(ptable, colorby='jmol_color', title="JMol Colors", decimals=3, width=700)
#periodic_plot(ptable, colorby='cpk_color', title='CPK Colors')
#periodic_plot(ptable, colorby='molcas_gv_color', title='MOLCAS GV Colors')

If required, custom colour maps can also be applied:

import seaborn as sns
from matplotlib import colors

blockcmap = {b : colors.rgb2hex(c) for b, c in zip(['s', 'p', 'd', 'f'], sns.color_palette('deep'))}
ptable['block_color'] = ptable['block'].map(blockcmap)

periodic_plot(ptable, colorby='block_color',
              width=700)

Elements may also be styled in the table according the value of specific properties:

periodic_plot(ptable, attribute='covalent_radius_pyykko',
              colorby='attribute', title="Covalent Radii of Pyykko",
              width=700)

