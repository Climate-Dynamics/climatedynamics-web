Projects
========


FACT - Fast/Fortran Atmospheric Model for Complex Terrain
---------------------------------------------------------

.. figure:: img/FACT_dark.png
   :align: left

FACT is an intermediate complexity model for downscaling climate in complex terrain (such as mountain regions). It combines process-based and empirical modelling. For rainfall, the former uses mountain wave theory and builds on the works of Smith and Barstad (2004) and Hergarten and Robl (2022). The latter uses parameter optimisation techniques and concepts from model output statistics. The model is still in early development. It is designed to work as a module for fast post-processing of climate model output.


FPLT - Fortran Plotting Library
-------------------------------

.. figure:: img/FPLT.png
   :align: left

FPLT is a Fortran plotting library built mostly on GMT (Generic Mapping Tools). FPLT includes a Fortran interface for GMT (using GMT's C API). Additional features are provided through an abstraction layer that makes plotting a little easier. These features include derived types for colour maps, font management, options for different kinds of plots (e.g., maps, xy-scatter plots, raster plots), and more. It also includes procedures for automatic construction of colour maps and (the infamously cryptic) GMT argument strings from pre-defined or user-defined option sets. FPLT is currently developed further "as needed" for my research, but I hope it may become useful for other researchers as it continues to grow. However, you are very welcome to contribute (through suggestions, coding, etc.) at any stage.


pyESD - Empirical-Statistical Downscaling with Python
-----------------------------------------------------

.. figure:: img/pyESD-1.png
   :align: left

PyESD is an open-source framework for empirical-statistical downscaling (ESD) of any climate-related variable like rainfall, temperature, and wind speed. The software package implements the whole downscaling cycle, including data preprocessing, predictor selection, constructions, model selection, training, validation and evaluation, and prediction. It includes a range of methods, including well-established multivariate statistical methods, as well as techniques from Machine Learning. The package serves as the means of downscaling General Circulation Models of future climate to high resolution relevant for climate impact assessment such as droughts, flooding, wildfire risk, and others. The model code is available through `GitHub <https://github.com/Dan-Boat/PyESD>`_. The associated publication in *Geoscientific Model Development* can be found `here <https://gmd.copernicus.org/articles/16/6479/2023/>`_ (Boateng and Mutz, 2023).

.. seealso::

   The full documentation of the package, including tutorials and example applications, can be found `here <https://dan-boat.github.io/PyESD/>`_.


INTEGRATE - Climate Science Teaching Package
--------------------------------------------

.. figure:: img/integrateLogo.png
   :align: left

INTEGRATE (INTEGRation of Atmospheric science, Technical and Empirical methods) is an open-access, open-source teaching package that covers the topics of physical climatology, empirical methods and a hands-on approach of collecting and analysing atmospheric data. It promotes an interdisciplinary and didactically multifaceted approach to learning about climatology, modern empirical methods and programming. It comprises a crash course in theory and hands-on approach to collecting atmospheric data and working with readily available climatological records on real problems. This course requires no prior knowledge of the topics covered in the course. The following resources are included in the course and packaged into a single `GitHub repository <https://github.com/sebastian-mutz/integrate>`_:
(1) Accessible graphics and notes for learning about climate science. These are divided into chapters („Building a Climate“), which can be taught as a lecture series or studied as a virtual introductory text to physical climatology.
(2) Materials for the exercise series (including solutions to posed problems, data and code) and tested ideas for group projects.
(3) All code required to compile the teaching materials into a complete course website.
The project was supported by the European Geosciences Union and is listed in the `EGU teaching resources <https://www.egu.eu/education/resources/342/integrate-integration-of-atmospheric-science-technical-and-empirical-methods/>`_.

.. seealso::

   A full demonstration and explanation of the teaching package can be found on a compiled version of the course website that is hosted `here <http://integrate.mutz.science>`_.


ParsQuake - Earthquake Education Materials
------------------------------------------

.. figure:: img/parsquake.jpg
   :align: left

Earthquakes are the pulse of a vibrant and dynamic planet. The livelihood of the Earth can be appreciated through the study of earthquakes and other natural phenomena. With the knowledge we gain from studying earthquakes, we can start to understand and reduce their impact on society. Our earthquake lessons are designed to educate students and teachers with little or no pre-existing knowledge of Earth and space sciences, so that they may protect themselves in the event of an earthquake. Our curriculum consists of pre- and post-assessment activities, six directed inquiry-based science activities describing physical processes related to earthquakes, five interactive activities on earthquake hazards and mitigation strategies, and a codification art/literacy project. Each earthquake hazards lesson includes a Tabletop Exercise, which is a scenario that incorporates the occurrence of a particular type of hazard into a realistic chain of events that a student may experience during an earthquake. All lessons are optimized for scientific content, ease of implementation, appropriateness to the targeted grade levels (middle and high school) and cultural sensitivity. The materials are availble through the `ParsQuake website  <https://parsquake.org/>`_. You can read more about how they were tested `here <https://doi.org/10.5194/gc-4-281-2021>`_ (Mohadjer et al.,2021).

.. seealso::

   The videos, transcripts, supplemental material and news about the initiative can be found `here <https://parsquake.org/>`_.

