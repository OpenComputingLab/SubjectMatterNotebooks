# Introduction

This online interactive books reviews some of the wide range of Python packages that can be used to create rich and interactive media outputs as part of a Jupyter publishing system.

Whilst Python programming used may be used to generate the various outputs, the code is not required in order to view the outputs.

In this way, a Jupyter publishing system may be used to provide an environment in which asset generation is scripted and reproducible, as well as providing "source code" documents that can be updated and modified in order to update original assets or generate further assets derived from or inspired by them.

However, the publishing syste, becomes more powerful if scripts are used inline in a document to create document assets (even if the scripts are hidden or removed from the final document). This allows assets to be created in context as part of the execution of the original document. In this way, we can produce publications where there is a very high degree of coupling between each component of the original document. Updating one part of the source code in the document and then reflowing the document will all dependent outputs in the document to be updated automatically.

Note that there is no need for the originating code to be included in the published work. Whilst the originating code can be revelaed and made explicit in the rendered work, it might alos be hidden but still available in a collapsed view be made or removed entirely from the final rendered page view.

It should also be remembered that not only can the publishing process produce standalone HTML pages: static print style document formats, such `.docx` or PDF dcocuments, can also be generated.

cell

:::{admonition} Want to use RMarkdown directly?
:class: tip
Seeasasa  sdsd
:::

more cell

## Single Piece Flow

Self-contained, delf-generating, single piece document flow.


```{toctree}
:hidden:
:titlesonly:
:caption: STEM

astronomy/overview
chemistry/overview
chemistry/compound_lookups
chemistry/material_properties
chemistry/visualising-compounds
chemistry/recipes
electronics/overview
electronics/worked-example
engineering/overview
maths/overview
```


```{toctree}
:hidden:
:titlesonly:
:caption: Arts & Humanities

art/overview
linguistics/overview
music/overview
```


```{toctree}
:hidden:
:titlesonly:
:caption: Map Generation

geo/overview
```


```{toctree}
:hidden:
:titlesonly:
:caption: Chart Generation

chart/overview
```


```{toctree}
:hidden:
:titlesonly:
:caption: Diagram Generation

diagram/overview
```


```{toctree}
:hidden:
:titlesonly:
:caption: Image Generation and Manipulation

image/overview
```


```{toctree}
:hidden:
:titlesonly:
:caption: Audio Generation and Manipulation

audio/overview
```


```{toctree}
:hidden:
:titlesonly:
:caption: LaTeX

latex/overview
```
