# Tutorial for Data Collection at CCB

This tutorial will walk you through some of the useful steps of
collecting data at the CCB X-ray facility using the D8 Venture. This
is mainly intended as a reminder of useful settings and options for the
relatively infrequent times that we screen crystals using a home source. 

### Things to note for processing data

If the goal of data collection at CCB is to process data in XDS
(i.e. index the collected data), it is necessary to keep track of the
following instrument settings:

- Goniometer:
    - omega angle
    - phi range (total range) and width (per image oscillation)

- Detector:
    - 2Theta angle (swing angle of detector)
    - Detector distance

### 1) Centering Crystal

In the APEX3 GUI, one can make a new sample using the Sample menu. It is good
practice to make a new sample for each crystal that is screened because it ensures
that the working directory is distinct for each sample. After making a new sample, one
can navigate to the "Center Crystal" window of the "Set Up" options.

If the shutter to the D8 cabinet is closed, one can open the cabinet and
place the goniobase on the magnetic goniometer mount. Prior to opening the
cabinet, it is often useful to click the "Right" option in the lower right corner of the
GUI. This moves the detector and goniometer to ensure there is space for placing the crystal.
It also positions the goniometer mount such that the initial two pegs are available for centering
the crystal along the phi axis.

The camera can be toggled on using the green/blue button in the top bar of the GUI or toggled off
using the red/blue button. Crosshairs can also be overlaid on the image using the target-shaped button. For
details of the GUI, see the screenshot below. While adjusting the goniometer, it is useful to spin the phi
angle to ensure that the crystal remains at the center of the crosshairs.

![Screenshot: Centering Crystal](/tutorial/images/GUI_CenterCrystal.PNG)