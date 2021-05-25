#%pip install git+https://github.com/innovationOUtside/ipython_magic_tikz.git
%load_ext tikz_magic

%%tikz
\usetikzlibrary{shapes.geometric, calc}
\def\numsides{7} % regular polygon sides
\node (a) 
[draw,  blue!0!black,rotate=90,minimum size=3cm,regular polygon, regular polygon sides=\numsides] at (0, 0) {}; 

\foreach \x in {1,2,...,\numsides}
  \fill (a.corner \x) circle[radius=.5pt];
  \foreach \x in {1,2,...,\numsides}{
  \draw [red,dashed, shorten <=-0.5cm,shorten >=-0.5cm](a.center) -- (a.side \x);
  \draw [red,dashed, shorten <=-0.5cm,shorten >=-0.5cm](a.center) -- (a.corner \x);}