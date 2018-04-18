#!/usr/bin/env python3
from __future__ import print_function  # so we can get a friendlier error when people use py2

import subprocess
import hashlib
import sys, glob, os, re

ERR_BAD_PYTHON_VER = 1

update_command = ['wget', '-N', '-nd', '-Apdf,html', '-rl1', '-q', '--show-progress']
source_url = 'https://www.alchemistowl.org/pocorgtfo/'

def remove_unneeded_files(quiet=False):
	for item in glob.glob('*.tmp') + glob.glob('index.html'):
		if not quiet:
			print('removing {}'.format(item), file=sys.stderr)
		
		os.unlink(item)


## remove old .tmp files
remove_unneeded_files()

## get a list of existing PDFs
current_issues = glob.glob('*.pdf')

## download anything new
try:
	stdout, stderr = None, None
	completed = subprocess.run(
		update_command + [ source_url ], 
		stderr=stderr, stdout=stdout, 
		check=True)

except AttributeError:
	print('You must use Python3.5 or newer to use subprocess.run()',file=sys.stderr)
	exit(ERR_BAD_PYTHON_VER)

except subprocess.CalledProcessError as e:
	print(
		"Error with {command} ({code}):".format(
			command=update_command[0], code=e.returncode),
		file=sys.stderr)
	print(e.stdout + e.stderr, file=sys.stderr)
	exit(e.returncode)

## get a list of all issues *now* and then figure out which are new
all_issues = glob.glob('*.pdf')
new_issues = list( set(all_issues).difference(current_issues) )

if new_issues:
	## parse index.html to find SHA sums to compare
	sha256_sum_re = re.compile('SHA256\s+\((.+?)\)\s+=\s+([0-9a-fA-F]+)')
	found_sums = {}
	with open('index.html', 'r') as f:
		html = f.read()
		for match in sha256_sum_re.finditer(html):
			filename = match.group(1)
			digest = match.group(2)
			found_sums[filename] = digest
			# print("claiming: {digest}  {filename}".format(
			# 	digest=digest, filename=filename), file=sys.stderr)

	## generate the hash digests of any new issues
	digests = {}
	print('{count} new issue{pl}, checking digest{pl}:'.format(
		count=len(new_issues),
		pl='s' if len(new_issues) > 1 else ''))

	for issue in new_issues:
		hashf = hashlib.sha256()
		with open(issue, 'rb') as f:
			databytes = f.read()

		hashf.update(databytes)
		digests[issue] = hashf.hexdigest()
		matches = ''

		if issue not in found_sums:
			matches = '!NOT FOUND'
		elif digests[issue] == found_sums[issue]:
			matches = 'OK'
		else:
			matches = 'FAILED (expected: {})'.format(found_sums[issue])

		print('{digest}  {filename}: {result}'.format(
			digest=digests[issue], filename=issue, result=matches))
else:
	## no new issues found
	print('Found no new issues. Finished', file=sys.stderr)

## cleanup: delete *.tmp, *.html
remove_unneeded_files(quiet=True)

