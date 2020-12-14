#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

# sys.argv.append('C:\\Users\\lambda_school_loaner_110\\programming\\Computer-Architecture\\ls8\\examples\call.ls8')
sys.argv.append('C:/Users/lambda_school_loaner_110/programming/Computer-Architecture/ls8/examples/call.ls8')

if len(sys.argv) > 1:
    cpu.load(sys.argv[1])
    cpu.run()
else:
    print('select program to run')
