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

It will also be necessary to convert the collected images to MCCD format
from the default Bruker format (.sfrm) prior to processing. This conversion is
covered in the last section of this tutorial. 

### 1) Centering Crystal

In the APEX3 GUI, one can make a new sample using the Sample menu. It is good
practice to make a new sample for each crystal that is screened because it ensures
that the working directory is distinct for each sample. After making a new sample, one
can navigate to the "Center Crystal" window of the "Set Up" options.

If the shutter to the D8 cabinet is closed, one can open the cabinet and
place the goniobase on the magnetic goniometer mount. Prior to opening the
cabinet, it is often useful to click the "Right" option in the lower right corner of the
GUI (boxed in red, in screenshot below). This moves the detector and goniometer to ensure there is space for placing the crystal.
It also positions the goniometer mount such that the initial two pegs are available for centering
the crystal along the phi axis.

The camera can be toggled on using the green/blue button in the top bar of the GUI or toggled off
using the red/blue button. Crosshairs can also be overlaid on the image using the target-shaped button. For
details of the GUI, see the screenshot below. While adjusting the goniometer, it is useful to spin the phi
angle to ensure that the crystal remains at the center of the crosshairs. This can be done using the large buttons on the
right-hand side. To avoid moving while centering the crystal, note that there is an additional mouse in the D8 cabinet. 

![Screenshot: Centering Crystal](/tutorial/images/GUI_CenterCrystal.PNG)

### 2) Screening Crystal

After centering the crystal, navigate to the "Screen Crystal" option in the "Set Up" menu. This mode is handy for taking test
shots at the crystal. This should be used to assess the desired exposure time (often 30-60 seconds), and to adjust the detector distance, detector
swing angle, and goniometer omega angle according to the resolution.

To start, I usually set the detector distance to 70 mm, the omega angle to 0 degrees, and the 2theta angle to -10 degrees. Be careful when moving
the detector and goniometer that they do not bump each other. If they are set to the same angle they are perpendicular to one another, so it is always
safe to move them to the same angle. If you want to move the detector in further, it may be necessary to adjust the omega angle to compensate. Finally,
I usually set the scan range to 1 to take a single image, and change the image width to 1.

A screenshot of the  GUI for screening mode is shown below. The default colormap is a bit irritating, but can it can be switched to black/white (ADXV convention)
by right-clicking the colorbar on the right-hand side. The image thresholding can be adjusted using the sliding bar on the bottom of the image.

![Screenshot: Screening Crystal](/tutorial/images/GUI_ScreenCrystal.PNG)

### 3) Data Collection

Once the desired data collection settings have been determined, go to the "Run Experiment" option in the "Collect" menu. Here, one can write a series of phi sweeps
as rows in the spreadsheet. This way, one can collect wedges in different phi ranges in order to improve the odds of successful indexing. If you know something about
the space group of your crystal, you could also design a better strategy for data collection.

To ensure that your settings are consistent with the instrument, I often
click the "Validate" button at the bottom of the window. **I also typically use the "Save Table" button to save a ".exp" file in the directory that describes the experiment.**
I find this useful so that I can always come back to the directory and understand what was done. It's worth noting that this file is plain-text so it can be interpreted
without the need for any special applications. Also, be sure to **copy this file along with your images**. You will need it to create an XDS input file.

When you are happy with the settings, you can click the "Execute" button at the bottom right corner of the GUI. Here is a screenshot of the "Run Experiment" window:

![Screenshot: Data Collection](/tutorial/images/GUI_PhiSweep.PNG)

### 4) Image Conversion

**NOTE**: As of 2022, Jack and Dennis have determined that conversion to `.MCCD`-format images is not necessary, and may actually lead to errors in the image headers. If you'll be continuing with the [XDS data processing tutorial](/tutorial/2_processing_tutorial.md), sticking with `.sfrm`-format images is fine and probably easiest.

After data collection, we can convert the images in batch to MCCD format that we can process the images using XDS. This is handled using the "Unwarp and Convert Images"
option in the "Reduce Data" menu. Here, one can view the images that are being converted. On the right-hand side of the GUI, one can select the desired batches of images
for conversion, set a output format (for XDS processing, specify MCCD format), and designate a desired folder to which the new images will be written. I usually make a
"mccd" image within the directory used for data collection so that the provenance of the images is clear. See GUI screenshot below:

![Screenshot: Image Conversion](/tutorial/images/GUI_ImageConversion.PNG)
