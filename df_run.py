import os
import subprocess
import sys

rel = [['0'] * 11 for _ in range(1,32,2)]

for i in range(1, 17, 2):
	ratio = i/31
	output = subprocess.check_output("python3 ./benchmark.py dataframe {}".format(ratio), shell=True).decode(sys.stdout.encoding)
	row = (i-1) // 2
	for line in output.splitlines():
		if line.startswith('Step'):
			p_it_us = line.split(' ')
			s = int(p_it_us[1][0])
			us = p_it_us[2]
			rel[row][s+1] = us
		if 'Major (requiring I/O) page faults' in line:
			maf = line.rsplit(' ', 1)[-1]
			rel[row][1] = maf
		if 'Minor (reclaiming a frame) page faults' in line:
			mif = line.rsplit(' ', 1)[-1]
			rel[row][0] = mif

with open('tmp_rel.txt', 'w') as r:
	for dat in rel:
		print(dat)
		r.write(', '.join(dat) + '\n')
