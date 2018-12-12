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
