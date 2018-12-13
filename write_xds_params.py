from detector_geo import swing_diffractometer,experiment,three_axis_goniometer
import argparse

parser = argparse.ArgumentParser(description="Write out XDS geometry paramters for a swing angle detector setup.")
parser.add_argument('QX', type=float, help='Pixel x-dimension in mm')
parser.add_argument('QY', type=float, help='Pixel y-dimension in mm')
parser.add_argument('NX', type=int, help='Number of pixels in the x-direction')
parser.add_argument('NY', type=int, help='Number of pixels in the y-direction')
parser.add_argument('Distance', type=float, help='Detector distance in mm')
parser.add_argument('TwoTheta', type=float, help='Detector swing angle')
parser.add_argument('Chi', type=float, help='Goniometer angle between phi axis and xz plane.')
parser.add_argument('Omega', type=float, help='Goniometer angle between the phi axis and the xy plane.')
parser.add_argument('-o', type=str, help='Output filename', default='XDS.INP')
parser.add_argument('-p', action='store_true', help='Plot experimental system', default=False)

args = parser.parse_args()
d = swing_diffractometer(args.QX, args.QY, args.Distance, args.NX, args.NY, args.TwoTheta)
g = three_axis_goniometer(0., args.Chi, args.Omega)

e = experiment(d, g)
if args.p:
    e.plot()


with open(args.o, 'w') as out:
    out.write(e.generate_xds_in())
