# pyGridCut

[![Build Status](https://travis-ci.org/Borda/GridCut-python.svg?branch=master)](https://travis-ci.org/Borda/GridCut-python)
[![codecov](https://codecov.io/gh/Borda/GridCut-python/branch/master/graph/badge.svg)](https://codecov.io/gh/Borda/GridCut-python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e4562d3e10a94c4fa373630cab2e795f)](https://www.codacy.com/app/Borda/GridCut-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Borda/GridCut-python&amp;utm_campaign=Badge_Grade)
[![Build status](https://ci.appveyor.com/api/projects/status/dp9v07hx6cc6f8r5?svg=true)](https://ci.appveyor.com/project/Borda/pygridcut)

A Python wrapper for the [GridCut C++ library](http://www.gridcut.com/index.php) for solving graph cuts in regular grids.

**Implemented functions:**
 * gridcut.maxflow_2D_4C(...)
 * gridcut.maxflow_2D_4C_potts(...)
 * gridcut.maxflow_2D_8C_potts(...)


## Installation

Actually the latest version is **1.3** as it is set up in the _setup.py_ 

```
python setup.py build_ext --inplace
python setup.py install
```

For installation use previous commands it does following steps:
1. download the source code
1. unzip the package to _code_ folder
1. build the **gridcut**

Note, that downloading the source cede you agree with GridCut [license](http://www.gridcut.com/licensing.php) 

## Show examples

### Source-Sink segmentation

Visualisation of the unary terns for source/sink segmentation

![unary terms](./images/2cls_grid_unary.png)

with the initial labeling (left) and estimated labeling (right) for 4-connectivity

![labeling](./images/2cls_grid_labels_4c.png)

and the initial labeling (left) and estimated labeling (right) for 8-connectivity

![labeling](./images/2cls_grid_labels_8c.png)