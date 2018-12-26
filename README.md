# ccbxray
Notes and Tools for Analyzing MX Datasets from the CCB X-Ray Facility

The Department of Chemistry and Chemical Biology (CCB) maintains an X-ray [facility](https://chemistry.harvard.edu/pages/x-ray-laboratory) for small molecule crystallography.
Occasionally, we would like to use their facility to collect and analyze macromolecular crystallography datasets. 
The major tool for crystallographic analyses in the lab is Wolfgang Kabsch's [XDS](http://xds.mpimf-heidelberg.mpg.de/). 
This repository contains notes on the process of analyzing datasets from the D8 Venture microdiffractometer in the CCB facility with XDS. 

### Geometric Parameters and Coordinate System
In order for XDS to process D8 Venture data, the coordinate system relating the detector and sample geometry needs to be expressed in a format that XDS understands. 

By convention, we designate the incident X-ray beam direction as the Z-axis (0 0 1). While this doesn't have to be the case, it is also what we use for non-swing detectors
(such as at synchrotrons) and  is a very logical convention. The X- and Y-axis in the lab coordinate system are then specified as the orthogonal axes to the X-ray beam. 

-- to do --
- Add images describing neccessary geometric parameters using the 3D models of the experimental configuration.

### Tutorial/Notes for Data Collection using the  D8 Venture
A tutorial for data collection can be found [here](/tutorial/tutorial.md). This goes through the steps of crystal centering, screening, data collection, and image conversion for
processing in XDS. After image conversion, the scripts in this repository can be used to generate an XDS.INP file for data processing..

### Dependencies for Python scripts
- Python 3
- [Numpy](http://www.numpy.org/)
- [Matplolitlib](https://matplotlib.org/)
- [XDS](http://xds.mpimf-heidelberg.mpg.de/) if you wish to plot the experiment geometry.

### Example Input
The example directory  contains an example input for XDS (XDS.INP). This corresponds to an experiment at the CCB facility with the following parameters:
- Detector distance = 70
- 2 theta = -10
- chi = 54.717
- omega = 0

The D8 goniometer is fixed to chi = 54.717 degrees. The following parameters are compatible with the Photon 100 detector on the D8 Venture:
- QX = 0.096
- QY = 0.096
- NX = 1024
- NY = 1024

The XDS.INP file, as provided, can be used for data processing in XDS. However, keep in mind that this script only
outputs the section of the XDS.INP that describe the experiment's geometric parameters.
