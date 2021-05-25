#%pip install rdkit-pypi
#import rdkit

from rdkit import Chem

m = Chem.MolFromSmiles("C1=NC2=C(N1)C(=NC=N2)N")
m

m = Chem.AddHs(m)
m

from rdkit.Chem import Draw

def smilesH(m):
    return Chem.AddHs(Chem.MolFromSmiles(m))

bromomethane = smilesH('CBr')
bromoethane = smilesH('CCBr')
_2_bromopropane =  smilesH('CC(Br)C')
_2_bromo_2_methylpropane = smilesH('CC(Br)(C)C')

my_molecules = [bromomethane, 
                bromoethane,
                _2_bromopropane,
                _2_bromo_2_methylpropane,
               ]

Draw.MolsToGridImage(my_molecules, useSVG=True)

from rdkit.Chem import RemoveHs

RemoveHs(_2_bromo_2_methylpropane)

#Highlight a substructure
m.GetSubstructMatch(Chem.MolFromSmiles('C(N)'))
m

#Following is needed to render molecule structure views in Jupyter notebook
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import rdChemReactions

IPythonConsole.ipython_useSVG=True  

rdChemReactions.ReactionFromSmarts("C=CCBr>>C=CCI");

%%capture

try:
    import openbabel
except:
    %pip install openbabel-wheel
    ##!brew install open-babel

from openbabel import pybel

mol = pybel.readstring( "smi","C1=NC2=C(N1)C(=NC=N2)N" )

#Add hydrogens
mol.addh()

#By default, we preview a small SVG output graphic
mol

#  Better preview
from IPython.display import SVG

SVG(mol.write("svg"))

mol.write("smi")

from IPython.display import display

def smilesSVG(smi, addH=False, bw=False):
    ''' Render molecule structure from SMILES string as SVG. '''
    
    mol = pybel.readstring( "smi",smi )
    if addH: mol.addh()
    conv = pybel.ob.OBConversion()
    conv.SetOutFormat("svg")
    #Optonally, set black and white output
    #The openbabel SVG export formatter has an -xu option which we can pass
    #Via: https://github.com/openbabel/openbabel/issues/1879#issuecomment-411830813
    if bw:
        conv.SetOptions('u', conv.OUTOPTIONS)
    display(SVG(conv.WriteString(mol.OBMol)))
    #display(SVG(mol.write("svg")))

smilesSVG( "C1=NC2=C(N1)C(=NC=N2)N" )

smilesSVG( "C1=NC2=C(N1)C(=NC=N2)N", addH= True )


smilesSVG( "C1=NC2=C(N1)C(=NC=N2)N", addH=False, bw=True );


%%capture
try:
    import py3Dmol
except:
    %pip install py3Dmol

import py3Dmol

# Lookup a molecule using its CID (PubChem Compound Identification) code
p=py3Dmol.view(query='cid:702')

# Set the render style
p.setStyle({'stick': {'radius': .1}, 'sphere': {'scale': 0.25}})
p.show()

p = py3Dmol.view(query='pdb:1ycr')
p.setStyle({'stick': {'radius': .1}, 'sphere': {'scale': 0.25}})

p.setStyle({'cartoon':{'color':'spectrum'}});

%%capture
try:
    import nglview
except:
    %pip install nglview
    !jupyter-nbextension enable nglview --py --sys-prefix

import nglview as nv

view = nv.show_structure_file(nv.datafiles.PDB)
view

# Useful to pop out in Jupyter notebook context?
view.clear_representations()
view.add_licorice('not hydrogen', color='blue')

view.clear_representations()
view.add_cartoon()
view.add_surface(opacity=0.3)

# Force render here but the original is also updated?
view.render_image()

view.download_image("test.png")

# Downloads to download dir
# To specify a download path requires a workaround of working in a separate thread:
# https://github.com/nglviewer/nglview/blob/master/docs/FAQ.md#how-to-make-nglview-view-object-write-png-file
#from IPython.display import Image
#Image(PATH_TO_IMAGE)