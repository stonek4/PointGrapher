import argparse
import json
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="the first data file")
    parser.add_argument("file2", help="the second data file")
    parser.add_argument("xdata", help="data type for x axis")
    parser.add_argument("ydata", help="data type for y axis")


    args = parser.parse_args()

    data = ""
    data2 = ""

    with open(args.file1) as json_file:
        data = json.load(json_file)

    with open(args.file2) as json_file:
        data2 = json.load(json_file)

    p = [[],[]]
    p2 = [[],[]]
    p0 = [[],[]]
    p20 = [[],[]]

    for point in data['points']:
        if (point[args.ydata] == 0):
            p0[0].append(point[args.xdata])
            p0[1].append(point[args.ydata])
        else:
            p[0].append(point[args.xdata])
            p[1].append(point[args.ydata])

    for point in data2['points']:
        if (point[args.ydata] == 0):
            p20[0].append(point[args.xdata])
            p20[1].append(point[args.ydata])
        else:
            p2[0].append(point[args.xdata])
            p2[1].append(point[args.ydata])

    plt.figure(figsize=(12,12), dpi=326)
    plt.plot(p[0], p[1], 'ro', label=args.file1)
    plt.plot(p2[0], p2[1], 'bo', label=args.file2)
    plt.plot(p0[0], p0[1], 'rs', label=(args.file1 + " y = 0"))
    plt.plot(p20[0], p20[1], 'b^', label=(args.file2 + " y = 0"))
    plt.xlabel(args.xdata)
    plt.ylabel(args.ydata)
    plt.legend()
    plt.savefig(args.xdata + "_vs_" + args.ydata + ".png")
    plt.show()

main()
