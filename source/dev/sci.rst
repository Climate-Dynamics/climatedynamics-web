Science Projects
================

FSML - Fortran Statistics and Machine Learning Library
------------------------------------------------------

.. figure:: img/FSML_dark.png
   :align: left

FSML (Fortran Statistics and Machine Learning) is a scientific toolkit consisting of common statistical and machine learning procedures, including basic descriptive statistics (e.g., mean, variance, correlation), common statistical tests (e.g., t-test, Mann–Whitney U), linear models (e.g., multiple OLS regression), and non-linear algorithmic statistical and machine learning procedures (e.g., k-means clustering).

Key features:

- Common statistics and machine learning techniques (as used in modern research).
- Familiar/intuitive interface (similarities to popular Python or R libs).
- Core procedures are kept pure (to simplify parallelisation and testing), while impure wrappers handle optional arguments and errors for safe conventional use.
- Minimal requirements/dependencies (Fortran 2008 or later, and stdlib).


.. seealso::

   The source code is hosted in a GitHub repository `here <https://github.com/sebastian-mutz/fsml/>`_. Its online documentation can be viewed `here <http://fsml.mutz.science/>`_.


FPLT - Fortran Plotting Library
-------------------------------

.. figure:: img/FPLT_dark.png
   :align: left

FPLT is a a scientific plotting library for producing high-quality ("publication-ready") figures quickly by leveraging the GMT(Generic Mapping Tools) C-API and modern Fortran's derived types. FPLT includes procedures for producing geographical maps, xy-plots, heat maps, animated figures, and more. FPLT includes a Fortran interface for several GMT modules (using GMT’s C API). Additional features, provided through an abstraction layer, include Fortran derived types for colour maps, font management, and options for specific kinds of plots. Furthermore, FPLT includes procedures for the automatic construction of colour maps and (the infamously cryptic) GMT argument strings from pre-defined or user-defined options.

The aim is to create a library that lets you:

- visualise your data directly from your Fortran programme though familiar Fortran-native constructs,
- produce professional figures quickly through the use of templates and automatic argument construction,
- modify or create new templates easily from your programme.

The entire project is hosted on `GitHub <https://github.com/sebastian-mutz/fplt/>`_.

.. seealso::

   The source code is hosted in a GitHub repository `here <https://github.com/sebastian-mutz/fplt/>`_.


pyESD - Empirical-Statistical Downscaling with Python
-----------------------------------------------------

.. figure:: img/pyESD-1.png
   :align: left

PyESD is an open-source framework for empirical-statistical downscaling (ESD) of any climate-related variable like rainfall, temperature, and wind speed. The software package implements the whole downscaling cycle, including data preprocessing, predictor selection, constructions, model selection, training, validation and evaluation, and prediction. It includes a range of methods, including well-established multivariate statistical methods, as well as techniques from Machine Learning. The package serves as the means of downscaling General Circulation Models of future climate to high resolution relevant for climate impact assessment such as droughts, flooding, wildfire risk, and others. The model code is available through `GitHub <https://github.com/Dan-Boat/PyESD>`_. The associated publication in *Geoscientific Model Development* can be found `here <https://gmd.copernicus.org/articles/16/6479/2023/>`_ (Boateng and Mutz, 2023).

.. seealso::

   The full documentation of the package, including tutorials and example applications, can be found `here <https://dan-boat.github.io/PyESD/>`_.


FACT - Fortran Atmospheric Model for Complex Terrain
----------------------------------------------------

.. figure:: img/FACT_dark.png
   :align: left

FACT (Fast/Fortran Atmospheric Model for Complex Terrain) is an intermediate complexity model for downscaling climate in complex terrain (such as mountain regions). It combines process-based and empirical modelling. For rainfall, the former uses mountain wave theory and builds on the works of Smith and Barstad (2004) and Hergarten and Robl (2022). The latter uses parameter optimisation techniques and concepts from model output statistics. The model is still in early development. It is designed to work as a module for fast post-processing of climate model output.
