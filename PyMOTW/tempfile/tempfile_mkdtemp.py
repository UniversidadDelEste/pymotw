#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import os
import tempfile

directory_name = tempfile.mkdtemp()
print directory_name
# Clean up the directory yourself
os.removedirs(directory_name)