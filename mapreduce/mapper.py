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
