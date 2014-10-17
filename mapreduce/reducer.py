#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file):
    for line in file:
        yield line.strip().split('\t')

def main():
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin)

    for key, group in groupby(data, itemgetter(0)):
        try:
            group_list=list(group)
            total_sum = sum(float(sum) for key, sum, min, max, count in group_list)
            total_min = min(float(min) for key, sum, min, max, count in group_list)
            total_max = max(float(max) for key, sum, min, max, count in group_list)
            total_count = sum(int(count) for key, sum, min, max, count in group_list)
            print "%s\tcount:%s\tavg:%s\tmin:%s\tmax:%s" % (key, total_count, total_sum / total_count , total_min, total_max)

        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    main()
