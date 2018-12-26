# ccbxray
Notes and Tools for Analyzing MX Datasets from the CCB X-Ray Facility

The Department of Chemistry and Chemical Biology (CCB) maintains an X-ray [facility](https://chemistry.harvard.edu/pages/x-ray-laboratory) for small molecule crystallography.
Occasionally, we would like to use their facility to collect and analyze macromolecular crystallography datasets. 
The major tool for crystallographic analyses in the lab is Wolfgang Kabsch's [XDS](http://xds.mpimf-heidelberg.mpg.de/). 
This repository contains notes on the process of analyzing datasets from the D8 Venture microdiffractometer in the CCB facility with XDS. 

### Geometric Parameters and Coordinate System
In order for XDS to process D8 Venture data, the coordinate system relating the detector and sample geometry needs to be expressed in a format that XDS understands. 
This is described in the [Coordinate Systems](http://xds.mpimf-heidelberg.mpg.de/html_doc/coordinate_systems.html) section of the XDS documentation, but this will provide
a more detailed description as it pertains to the D8 Venture. 

By convention, we designate the incident X-ray beam direction as the Z-axis (0 0 1). While this doesn't have to be the case, it is also what we use for non-swing detectors
(such as at synchrotrons) and is a logical convention. The X- and Y-axis in the lab coordinate system are then specified as the orthogonal axes to the X-ray beam.

Given this setup for the lab coordinate system in real space, we need to express the relationship between X- and Y- direction of the detector and the lab coordinate system. In
XDS, this is specified as the parameters [DIRECTION_OF_DETECTOR_X-AXIS](http://xds.mpimf-heidelberg.mpg.de/html_doc/xds_parameters.html#DIRECTION_OF_DETECTOR_X-AXIS=) and
[DIRECTION_OF_DETECTOR_Y-AXIS](http://xds.mpimf-heidelberg.mpg.de/html_doc/xds_parameters.html#DIRECTION_OF_DETECTOR_Y-AXIS=). Since the swing angle of the detector (denoted as
2Theta) rotates about the Y-axis at the point of the sample, the DIRECTION_OF_DETECTOR_Y_AXIS is unchanged by the swing angle and can be given as (0, 1, 0). Specifically,
2Theta is the angle between the X-ray beam direction (Z-axis) and the normal to the plane of the detector.

For a graphical representation of these parameters, see the image below. The lab coordinate system is shown on the left-hand side, with the axes defined using the incident X-ray
beam (red line) and the right-hand rule to define the X-axis and Y-axis. The detector panel is highlighted in blue, with the 2Theta angle (swing angle) indicated. Note: the 2Theta
angle is defined as if one is looking down the Y-axis, which is the opposite direction of the top-down view of the experimental setup shown in the image. As such, as shown, the 2Theta
angle would be negative. The other detector
parameters -- [ORGX](http://xds.mpimf-heidelberg.mpg.de/html_doc/xds_parameters.html#ORGX=) and [ORGY](http://xds.mpimf-heidelberg.mpg.de/html_doc/xds_parameters.html#ORGY=) -- are
defined as the closest point on the detector to the sample. 

![Lab Coordinate System -- Detector](/tutorial/images/expt_coordinateSystem.png)

Finally, we can relate the goniometer axis to the lab coordinate system. This is required so that XDS can correctly interpret the series of images and their geometric
relationship to each other. The first goniometer parameter, chi, is the angle of the 3-axis goniometer with the XZ-plane. On the D8 Venture at CCB, this value is
fixed at 54.717 degrees. The next parameter is omega, which is the rotation angle of the goniometer around the Y-axis, measured relative to the X-axis. This angle is analogous to 2Theta
for the detector, but is defined as the angle relative to the X-axis, rather than the incident X-ray beam (Z-axis). Because of this, the goniometer and detector are orthogonal to each other
when 2Theta=omega. Finally, it is necessary to know the direction of the phi rotation, which is rotation about the goniometer axis.

These 3 experimental parameters for the goniometer axis are used to define the [ROTATION_AXIS](http://xds.mpimf-heidelberg.mpg.de/html_doc/xds_parameters.html#ROTATION_AXIS=). The
goniometer parameters are depicted in the image below. The goniometer axis is shown in green. Rotation about that axis is given by phi, which is defined as negative in the counter clockwise
direction when viewed from the sample to the goniometer base. As such, when one does a 1 degree wedge starting at phi=90 on the D8 Venture, the goniometer will rotate from phi=90 to phi=89. The chi
and omega angles are also shown.

![Lab Coordinate System -- Goniometer](/tutorial/images/expt_coordinateSystem2.png)

### Tutorial/Notes for Data Collection using the  D8 Venture
A tutorial for data collection can be found [here](/tutorial/tutorial.md). This goes through the steps of crystal centering, screening, data collection, and image conversion for
processing in XDS. After image conversion, the scripts in this repository can be used to generate an XDS.INP file for data processing..

### Dependencies for Python scripts
- Python2 or Python3
- [Numpy](http://www.numpy.org/)
- [Matplolitlib](https://matplotlib.org/)
- [XDS](http://xds.mpimf-heidelberg.mpg.de/) if you wish to plot the experiment geometry.

### Example Input
The example directory  contains an example input for XDS (XDS.INP). This corresponds to an experiment at the CCB facility with the following parameters:
- Detector distance = 70
- 2Theta = -10
- chi = 54.717
- omega = 0

The D8 goniometer is fixed to chi = 54.717 degrees. The following parameters are compatible with the Photon 100 detector on the D8 Venture:
- QX = 0.096
- QY = 0.096
- NX = 1024
- NY = 1024

The XDS.INP file, as provided, can be used for data processing in XDS. However, keep in mind that this script only
outputs the section of the XDS.INP that describe the experiment's geometric parameters.
