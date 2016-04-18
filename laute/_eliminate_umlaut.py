#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import glob
import shutil
import sys
reload(sys)  
sys.setdefaultencoding('iso-8859-1')
names = os.listdir(".")
print sys.getdefaultencoding()
for filename in names:
  print "Renaming: %s" % filename
  shutil.move(filename,filename.decode('iso-8859-1').replace(u'ä', 'ae').replace(u'ü', 'ue').replace(u'ö', 'oe').replace(u'Ü', 'Ue').replace('Ö', 'Oe'))
