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

    for point in data['points']:
        p[0].append(point[args.xdata])
        p[1].append(point[args.ydata])

    for point in data2['points']:
        p2[0].append(point[args.xdata])
        p2[1].append(point[args.ydata])

    plt.plot(p[0], p[1], 'ro', p2[0], p2[1], 'bo')

    plt.show()

main()
