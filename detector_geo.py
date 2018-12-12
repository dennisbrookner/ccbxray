import numpy as np

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
        self.X_AXIS = np.array([-np.cos(np.deg2rad(self.CHI)), 0, -np.sin(np.deg2rad(self.CHI))])
        self.Y_AXIS = np.array([0, 1, 0])
        self.DETECTOR_ORG = np.array([-self.F*np.sin(np.deg2rad(self.CHI)),0,self.F*np.cos(np.deg2rad(self.CHI))])

    def plot_panel(self, stride=None):
        if stride is None:
            stride = 10
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import pyplot as plt
        x,y = np.meshgrid(np.arange(self.NX) + 1, np.arange(self.NY) +1)
        x = np.concatenate((np.arange(self.NX) +1, self.NX*np.ones(self.NY), np.arange(self.NX)[::-1] +1, np.ones(self.NY) ))
        y = np.concatenate((np.zeros(self.NX), np.arange(self.NY) + 1, self.NY*np.ones(self.NX), np.arange(self.NY)[::-1] +1))
        x,y = x.flatten(),y.flatten()
        x,y,z = self(x, y).T
        f = plt.figure()
        ax = f.add_subplot(111, projection='3d')
        ax.scatter(x[::stride], y[::stride], z[::stride])
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
        plt.show()

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
        
