# Statistics in R

The code that can be executed in Jupyter notebook code cells is determined by the Jupyter kernel with which the notebook is associated and against which it is run.

For the author, this means that a single authoring environment, such as the classic Jupyter notebook interface, can be used to author documents whose outputs may be generated from a wide range of programming languages.

```{note}
Typically, all the code cells will be run against a single langiage kernel.

However, various workarounds are possible that support polyglot notebooks that allow multiple languages to be used across different cells.
```

## An Example in R

The following code cell shows how we can load in an R library to a native R environment:

library(ggplot2)

And then render a rich output from it:

ggplot(mpg, aes(displ, hwy, colour = class)) + 
  geom_point()