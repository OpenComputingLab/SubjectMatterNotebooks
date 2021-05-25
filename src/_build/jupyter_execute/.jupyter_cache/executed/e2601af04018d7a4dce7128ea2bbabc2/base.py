#Provide the common name of a compound
compound_name = "ethanol"

# Create a reference to a value we can use in our markdown text
from myst_nb import glue

glue("compound", compound_name, display=False)

import pubchempy as pcp

_compound = pcp.get_compounds(compound_name, 'name')[0]
_compound_latex = '$\ce{'+_compound.molecular_formula+'}$' 

from IPython.display import Latex

Latex('$\ce{'+_compound.molecular_formula+'}$')

glue("compound_latex", Latex('$\ce{'+_compound.molecular_formula+'}$'), display=False)

import py3Dmol

# Lookup a molecule using its CID (PubChem Compound Identification) code
p=py3Dmol.view(query = f'cid:{_compound.cid}')

# Set the render style
p.setStyle({'stick': {'radius': .1}, 'sphere': {'scale': 0.25}})
p.show()