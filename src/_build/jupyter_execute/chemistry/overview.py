# Chemistry Overview

A wide range of tools exist that support workflows in Chemistry, from looking up the structure and properties of a wide variety of elements and compounds, to visualising their structure using interactive HTML widgets.

Using automation to help us generate the the lookup of compund structures from their names allows us to creative narratives where correctness is guaranteed when moving from one consideration, such as the formula for a particular compound given its common name, to the visualisation of that structure.

The following example includes the code inline to show how the automation proceeds. In a finished would the code could be hidden but revealable, for eample in collapsed code cells, or have all mention of the code removed from the final output document.

#Provide the common name of a compound
compound_name = "ethanol"

# Create a reference to a value we can use in our markdown text
from myst_nb import glue

glue("compound", compound_name, display=False)

Having declared the compound we want to investigate in code, we can refer to it directly inline in our text — {glue:}`compound` is the thing we are interested in, for example — and we can also automatically look-up various things about it and even render a 3D visualisation of it.

import pubchempy as pcp

_compound = pcp.get_compounds(compound_name, 'name')[0]
_compound.canonical_smiles
_compound_latex = '$\ce{'+_compound.molecular_formula+'}$' 

$$\require{mhchem}$$ 

from IPython.display import Latex
Latex('$\ce{'+_compound.molecular_formula+'}$')

glue("compound_latex", Latex('$\ce{'+_compound.molecular_formula+'}$'), display=False)

Let's start with something simple: a rendering of the chemical equation for {glue:text}`compound`: 

{glue:math}`compound_latex`

import py3Dmol

# Lookup a molecule using its CID (PubChem Compound Identification) code
p=py3Dmol.view(query = f'cid:{_compound.cid}')

# Set the render style
p.setStyle({'stick': {'radius': .1}, 'sphere': {'scale': 0.25}})
p.show()

If we were to change the name of the compound in the first code cell in our original source document and reflow the notebook, *everything* would be updated and there would be no mismatches between the compound name, it's formula, or its visualised structure.

:::{admonition} Code visibility in rendered documents
:class: tip
Recall that there is no requirement for the original generating code to be visible, or even present, in the final rendered document.
:::
