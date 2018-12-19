# ccbxray
Notes and Tools for Analyzing MX Datasets from the CCB X-Ray Facility

The Department of Chemistry and Chemical Biology (CCB) maintains an X-ray [facility](https://chemistry.harvard.edu/pages/x-ray-laboratory) for small molecule crystallography.
Occasionally, we would like to use their facility to collect and analyze macromolecular crystallography datasets. 
The major tool for crystallographic analyses in the lab is Wolfgang Kabsch's [XDS](http://xds.mpimf-heidelberg.mpg.de/). 
This repository contains notes on the process of analyzing datasets from the D8 Venture microdiffractometer in the CCB facility with XDS. 


### File Formatting Requirements
The Bruker software for controlling the D8 Venture can export MCCD format diffraction images. 
 -- More on this later --

### Geometric Parameters
In order for XDS to process D8 Venture data, the coordinate system relating the detector and sample geometry needs to be expressed in a format that XDS understands. 

### Tutorial/Notes for Using D8 Venture
A tutorial for data collection using the D8 Venture can be found [here](/tutorial/tutorial.md).

### Dependencies for Python scripts
- Python 3
- [Numpy](http://www.numpy.org/)
- [Matplolitlib](https://matplotlib.org/)
- [XDS](http://xds.mpimf-heidelberg.mpg.de/) if you wish to plot the experiment geometry.

### Sample Input
This directory contains an example input for XDS (XDS.INP). This corresponds to an experiment at the CCB facility with the following parameters:
- 2 theta = -10
- omega = 0
- Detector distance = 70
The following parameters are compatible with the photon 100 detector on the D8 Venture:
- QX = 0.096
- QY = 0.096
- NX = 1024
- NY = 1024

The D8 goniometer is fixed to chi = 54.717 degrees.
