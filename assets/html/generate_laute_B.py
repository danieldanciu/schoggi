#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from sys import argv
import re
import generate_laute_common as common
import os


name, infile = argv

inp = open(infile)
old = inp.read()
inp.close()
old = common.eliminate_junk(old)
common.generate_word_list(old)
old = common.create_highlighted_wordlist2(old)

old = common.PREFIX2 + old

outfile_mac = infile.split('.')[0] + '_tmp.html'
outfile_utf8 = infile.split('.')[0] + 'B.html'
out = open(outfile_mac, 'w')
out.write(old)
out.close()
os.system("iconv -f macintosh -t utf-8 %s > %s" % (outfile_mac, outfile_utf8))
os.system("rm %s" % outfile_mac)