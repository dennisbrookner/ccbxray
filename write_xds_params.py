from detector_geo import swing_diffractometer
import argparse

parser = argparse.ArgumentParser(description="Write out XDS geometry paramters for a swing angle detector setup.")
parser.add_argument('QX', type=float, help='Pixel x-dimension in mm')
parser.add_argument('QY', type=float, help='Pixel y-dimension in mm')
parser.add_argument('NX', type=float, help='Number of pixels in the x-direction')
parser.add_argument('NY', type=float, help='Number of pixels in the y-direction')
parser.add_argument('F', type=float, help='Detector distance in mm')
parser.add_argument('CHI', type=float, help='Detector swing angle')
parser.add_argument('-o', type=str, help='Output filename', default='XDS.INP')

args = parser.parse_args()
g = swing_diffractometer(args.QX, args.QY, args.F, args.NX, args.NY, args.CHI)


with open(args.o, 'w') as out:
    out.write(g.generate_xds_in())
