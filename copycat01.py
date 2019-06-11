#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')
# Creates file copy
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
# Copies directory and creates an new directory with the copied content.
shutil.copytree('5g_research/', '5g_research_backup/')
