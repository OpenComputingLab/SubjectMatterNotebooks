%load_ext blockdiag_magic

%%blockdiag
A -> B -> C;
B -> D;

%%nwdiag --outfile demo1.svg
{
  network dmz {
      address = "210.x.x.x/24"

      web01 [address = "210.x.x.1"];
      web02 [address = "210.x.x.2"];
  }
  network internal {
      address = "172.x.x.x/24";

      web01 [address = "172.x.x.1"];
      db01;
      app01;
  }
}

from IPython.display import SVG
SVG('demo1.svg')

## 

#%pip install git+https://github.com/innovationOUtside/flowchart_js_jp_proxy_widget

import jp_flowchartjs.jp_flowchartjs

%%flowchart_magic

st=>start: Start
e=>end: End
op1=>operation: Generate
op2=>parallel: Evaluate
st(right)->op1(right)->op2
op2(path1, top)->op1
op2(path2, right)->e

%%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Set counter to 0
op2=>operation: Draw side code
op3=>operation: Turn ninety degrees code
op4=>operation: Add 1 to counter
cond=>condition: Is counter < 4?
st(right)->op1(right)->op2->op3->cond
cond(yes, right)->op2
cond(no, bottom)->e

