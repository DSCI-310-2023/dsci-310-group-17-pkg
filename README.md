# group17pkg

<!-- badges: start -->
![Github Actions Coverage](https://github.com/DSCI-310/dsci-310-group-17-pkg/actions/workflows/main.yml/badge.svg)
[![Codecov](https://codecov.io/gh/DSCI-310/dsci-310-group-17-pkg/branch/main/graph/badge.svg)](https://app.codecov.io/gh/DSCI-310/dsci-310-group-17-pkg?branch=main)
<!-- badges: end -->

## Overview
A python package designed for performing analysis on hyperthyroid disease data in order to classify individuals with hyperthyroid disease. This package includes functions to produce exploratory data analysis figures such as a description of the dataframe and a correlation matrix for all numeric variables. The package also includes a function to visualize the classification of data points based on TSH and TT4 concentration. There are many similar packages within the python ecosystem, specifically other disease classification packages. The main difference between this package and other is that our package does not have functions to directly classify data points, as only visualization functions are provided in group17pkg. 

## Installation
To install the package, clone this repository using `git clone url` with the repository url as url.
```
git clone https://github.com/DSCI-310/dsci-310-group-17-pkg.git
```

Then navigate to the repository on your local computer:

```
cd dsci-310-group-17-pkg
```

Then run the following to install the package locally:

```
pip install .

# OR

pip install -i https://test.pypi.org/simple/ group17pkg==0.0.0
```
The package should be installed on your local computer and usable for relevant projects and notebooks.

## Usage

Firstly import the package into the specific file you want to run the functions
```python
import group17pkg as grp
```

The most basic usage for the package is to cleans and correctly labels the provided UCI thyroid dataset: (http://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/)
```python
hyperthyroid_df = grp.relabel_bclass(hyperthyroid_df)
```

The next usage is to reformat the datasets column datatypes for classification analysis
```python
# Changing Dtype of the columns to numeric/categorical
num_cols = ['age', 'TSH', 'TT4', 'T4U', 'FTI']
cat_cols = ['sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
            'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid',
            'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'psych', 'binaryClass', 'hypopituitary']

hyper_clean = grp.col_dtype_reformat(num_cols, cat_cols, hyper_clean)
```
Furthermore, in the exploratory data analysis we can plot correlations between the different attributes:
```python
grp.plot_correlations(hyper_clean).show()
```

Finally, the package allows visualization of the classification analysis performed
```python
# X_train is the subsetted training set
# train_preds is the training set predictions made by your classification model
grp.visualize_classification(X_train, train_preds).show()
```

## Contributions
For contribution guidelines, please refer to the guidlines listed in this document [here](https://github.com/DSCI-310/dsci-310-group-17-pkg/blob/main/CONTRIBUTIONS.md). You can also find this document in our main project [here](https://github.com/DSCI-310/dsci-310-group-17/blob/main/CONTRIBUTING.md).

## Code of Conduct
Please note that the package is released with a [Contributor Code of Conduct](https://github.com/DSCI-310/dsci-310-group-17-pkg/blob/main/CODE_OF_CONDUCT.md). By contributing to this repository, you agree to abide by its terms and conditions.

## License
This project uses the MIT license for its code. Refer to the [license file](https://github.com/DSCI-310/dsci-310-group-17-pkg/blob/main/LICENSE) for more information.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
