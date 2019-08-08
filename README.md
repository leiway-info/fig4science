# fig4science
It provides a simple way to plot figures that are ready for scientific publication and presentation. It is based on Matplotlib.

1. It supports subplots.
2. It is mainly for plotting lines, because it is based on `ax.plot()` from `matplotlib.pyplot`.
3. It also serves as an example based on which the users can freely adapt for their own usage.

## Figure Quality

* Concise while informative
    * Keep it simple and direct to the point.
    * No need of special effect.
    * Try to avoid duplicate information.
* Rigorous and precise
    * Curves are within the limits of x and y axes.
    * Legends are not covering the curves.
* Visible
    * Labels and legends are big enough.
    * Lines are thick enough.
    * Think about for color-blind people, low-quality beamer or screen, and black-white printouts.
    * Save the figure as vector format (e.g. pdf or eps) than bitmap format (e.g. png or jpg).
    
## Example Figures
The following 3 figures demonstrate the results of using the proposed way of making figures. Note that although I suggest using vector images (e.g. pdf-format), these 3 examples are png-format because I upload them to github.

<img src="https://github.com/leiway-info/fig4science/blob/example_images/screenshots/paper.png" width="200" height="400" />
![](https://github.com/leiway-info/fig4science/blob/example_images/screenshots/three_subplots.png)
![](https://github.com/leiway-info/fig4science/blob/example_images/screenshots/two_subplots_log.png)



## Prerequisities
Main package is based on 
```python
matplotlib
```

The examples also use
```python
numpy
```


## Installation
This package is not yet uploaded to the Python Package Index. So simply download or git clone the whole package to your computer,
and use it as your own package. 


## General Usage
The following code shows how to use `figure.py`. Note that the code just shows the general concept, so all detailed arguments in functions are ignored.
```python
new_plot()  # Start a new figure
add_subplot()
add_a_line()
add_legend()
set_axes()
add_axes_labels()
use_tight_layout()
save()
```

# Detailed Usage
Please see the examples in `example.py` file.
