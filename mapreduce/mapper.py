#!/usr/bin/env python

import sys

def read_input(file):
    for line in file:
        # split the line into words
        yield line.strip().split(',')

def main():
    # definition for data type and initial value
    m_tem={}; m_tem['cnt'] = 0

    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        tm, sat, lon, z, tem, sat, u, v, dep, ele = words
        if (float(tem) <> -999.0 ) and (int(z) < 3) :
            if m_tem['cnt'] == 0 : m_tem['sum'] = float(0); m_tem['max'] = float(tem); m_tem['min'] = float(tem)
            m_tem['sum'] += float(tem)
            if m_tem['max'] < float(tem): m_tem['max'] = float(tem)
            if m_tem['min'] > float(tem): m_tem['min'] = float(tem)
            m_tem['cnt'] += 1
    if m_tem['cnt'] <> 0 : print '%s\t%s\t%s\t%s\t%s' % ('TEM', m_tem['sum'], m_tem['min'], m_tem['max'], m_tem['cnt'])

if __name__ == "__main__":
    main()

 ---------   reducer.py -----------
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
