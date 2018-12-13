import numpy as np


class experiment():
    diffractometer = None
    goniometer = None
    def __init__(self, diffractometer=None, goniometer=None):
        self.diffractometer = diffractometer
        self.goniometer = goniometer

    def generate_xds_in(self):
        text = ''
        if self.diffractometer is not None:
            text += self.diffractometer.generate_xds_in()
        if self.goniometer is not None:
            text += self.goniometer.generate_xds_in()
        return text

    def plot(self):
        from matplotlib import pyplot as plt
        if self.diffractometer is not None:
            ax = self.diffractometer.plot_panel()
            ax = self.goniometer.plot(ax)
            x,y,z = self.goniometer.rotation_axis[:,None]*np.linspace(-1, 1, 100)*self.diffractometer.F/5.
            ax.plot(x, y, z, c='violet')
            plt.show()

class three_axis_goniometer():
    phi = None
    kappa = None #Angle between phi axis and X-axis in the YZ plane in the lab frame
    omega = None #Angle between phi axis and X-axis in the XZ plane in the lab frame
    rotation_axis = None

    def __init__(self, phi, kappa, omega, sign=None):
        """
        PARAMETERS
        ----------
        phi : float
        kappa : float
        omega : float
        sign : float (optional)
            The direction of phi axis rotation. The default sign is -1. Input either a positive or negative float. Internally, the class will multiply the rotation axis by np.sign(sign)*rotation_axis.
        """
        self.phi = phi
        self.kappa = kappa
        self.omega = omega
        self.rotation_axis = np.array([np.cos(np.deg2rad(self.omega)), np.sin(np.deg2rad(self.kappa)), np.sin(np.deg2rad(self.omega))])
        self.rotation_axis = self.rotation_axis/np.linalg.norm(self.rotation_axis, 2)
        sign = -1. if sign is None else np.sign(sign)
        self.rotation_axis = sign*self.rotation_axis

    def generate_xds_in(self):
        return "ROTATION_AXIS= {} {} {}\n".format(*self.rotation_axis)

    def plot(self, axis):
        x,y,z = self.rotation_axis[:,None]*np.linspace(0, 1, 100)
        axis.scatter(x, y, z, c='violet')
        return axis

class swing_diffractometer():
    """This very simple class represents a diffraction experiment with a single detector that has a swing axis allowing rotation about the sample in the X plane."""
    QX = None #Pixel size
    QY = None #Pixel size
    F  = None #Detector distance
    NX = None
    NY = None
    ORGX = None
    ORGY = None
    CHI = None
    goniometer = None

    def __init__(self, QX, QY, F, NX, NY, CHI):
        """
        PARAMETERS
        ----------
        QX : float
            pixel x-dimension in mm
        QY : float
            pixel y-dimension in mm
        F : float
            detector distance in mm
        NX : int
            number of pixels in the x direction
        NY : int
            number of pixels in the y direction
        CHI : float
            swing angle of the detector
        """
        self.QX = QX
        self.QY = QY
        self.F = F
        self.NX = NX
        self.NY = NY
        self.CHI = CHI
        self.X_AXIS = np.array([np.cos(np.deg2rad(self.CHI)), 0, np.sin(np.deg2rad(self.CHI))])
        self.X_AXIS = self.X_AXIS/np.linalg.norm(self.X_AXIS, 2)
        self.Y_AXIS = np.array([0, 1, 0])
        self.DETECTOR_ORG = np.array([-self.F*np.sin(np.deg2rad(self.CHI)),0,self.F*np.cos(np.deg2rad(self.CHI))])

    def plot_panel(self, stride=None):
        if stride is None:
            stride = 10
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import pyplot as plt
        f = plt.figure()
        ax = f.add_subplot(111, projection='3d')
        x,y,z = self.panel_edge_xyz(stride).T
        ax.scatter(x[::stride], y[::stride], z[::stride])

        x,y,z = self.pix2lab(*self.panel_edge_pixels(stride)).T
        ax.plot(x[::stride], y[::stride], z[::stride], c='goldenrod')


        x,y,z = self.DETECTOR_ORG[:,None] * np.linspace(0, 1, 100)
        ax.scatter(x[::stride], y[::stride], z[::stride], c='r')
        ax.scatter(0, 0, 0, c='k')
        x,y,z = self.DETECTOR_ORG
        ax.scatter(x, y, z, c='k')
        x,y,z = np.zeros(100), np.zeros(100), np.linspace(0, self.F, 100)
        ax.scatter(x, y, z, c='y')
        ax.set_xlabel("X (mm)")
        ax.set_ylabel("Y (mm)")
        ax.set_zlabel("Z (mm)")
        return ax

    def panel_edge_pixels(self, stride=None):
        """
        Return the indices of the pixels at the edge of the detector in the lab frame. 
        PARAMTERS
        ---------
        stride : int (optional)
            Subsample the detector edge by only reporting every stride'th pixel.
        RETURNS
        -------
        x : np.ndarray
            The x-indices of the detector edge pixels. 
        y : np.ndarray
            The y-indices of the detector edge pixels. 
        """
        if stride is None:
            stride = 1
        x,y = np.meshgrid(np.arange(self.NX) + 1, np.arange(self.NY) +1)
        x = np.concatenate((np.arange(self.NX) +1, self.NX*np.ones(self.NY), np.arange(self.NX)[::-1] +1, np.ones(self.NY) ))
        y = np.concatenate((np.zeros(self.NX), np.arange(self.NY) + 1, self.NY*np.ones(self.NX), np.arange(self.NY)[::-1] +1))
        x,y = x.flatten(),y.flatten()
        return x,y


    def panel_edge_xyz(self, stride=None):
        """
        Return the coordinates of the pixels at the edge of the detector in the lab frame. 
        PARAMTERS
        ---------
        stride : int (optional)
            Subsample the detector edge by only reporting every stride'th pixel.
        RETURNS
        -------
        coordinates : np.ndarray
            The coordinates of the detector edge pixels. coordinates.shape = (number of pixels, 3)

        """
        if stride is None:
            stride = 1
        x,y = np.meshgrid(np.arange(self.NX) + 1, np.arange(self.NY) +1)
        x = np.concatenate((np.arange(self.NX) +1, self.NX*np.ones(self.NY), np.arange(self.NX)[::-1] +1, np.ones(self.NY) ))
        y = np.concatenate((np.zeros(self.NX), np.arange(self.NY) + 1, self.NY*np.ones(self.NX), np.arange(self.NY)[::-1] +1))
        x,y = x.flatten(),y.flatten()
        return self(x, y)

    def generate_xds_in(self):
        text = ""
        text = text + "ORGX= {} ".format(self.NX / 2)
        text = text + "ORGY= {} \n".format(self.NY / 2)
        text = text + "DETECTOR_DISTANCE= {}\n".format(self.F)
        text = text + "NX= {} ".format(self.NY)
        text = text + "NY= {} ".format(self.NY)
        text = text + "QX= {} ".format(self.QY)
        text = text + "QY= {}\n".format(self.QY)
        text = text + "DIRECTION_OF_DETECTOR_X-AXIS= {} {} {}\n".format(*self.X_AXIS)
        text = text + "DIRECTION_OF_DETECTOR_Y-AXIS= {} {} {}\n".format(*self.Y_AXIS)
        text = text + "INCIDENT_BEAM_DIRECTION= 0 0 1\n"
        return text

    def pix2lab(self, x, y):
        """
        Use the pix2lab program from XDS to compute the lab frame coordinates for detector pixels. 
        PARAMTERS
        ---------
        x : numerical or array-like
            An integer or array of integers corresponding to pixel x-inidces. Non-integers will be coerced to int. 
        y : numerical or array-like
            An integer or array of integers corresponding to pixel y-indices. Non-integers will be coerced to int. 

        RETURNS
        -------
        r : np.ndarray
            Array of lab frame coordinates for the detector pixels. These will be computed by the pix2lab program.
        """
        xdsin = self.generate_xds_in()
        with open('XDS.INP', 'w') as out:
            out.write(xdsin)
        from subprocess import Popen,PIPE
        p = Popen('pix2lab', stdin=PIPE, stdout=PIPE, encoding='utf-8')
        pix = '\n'.join(('{} {} 1'.format(i,j) for i,j in zip(x,y)))
        pix += '1 1 -1' #This kills the pix2lab session
        stdout,stderr = p.communicate(pix)
        pos = np.array([i.split()[-3:] for i in stdout.split('\n')[3::4]], dtype=float)
        return pos

    def __call__(self, x, y):
        """
        Return the lab coordinates of pixel position, x, y.
        PARAMETERS
        ----------
        x : numerical or array-like
            pixel x index
        y : numerical or array-like
            pixel y index

        RETURNS
        -------
        r : np.ndarray
            array of x,y,z coordinates in the lab frame. r.shape = (n pixels, 3)
        """
        if np.ndim(x) == 0:
            x = np.array([x])
            y = np.array([y])
        x = x - self.NX / 2
        y = y - self.NY / 2
        return self.DETECTOR_ORG + self.QX*x[:,None]*self.X_AXIS + self.QY*y[:,None]*self.Y_AXIS
        
