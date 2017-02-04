#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from no_raspi import sample

def main():
    sample.main()
    print('raspi')


if __name__ == '__main__':
    main()
