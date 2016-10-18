import os
import sys
import git
from datetime import datetime as dt
from datetime import timedelta


git.Git().clone("git@github.com:Harshdeep1996/test-data.git")
g = git.Git('test-data')
file_age = dt.strptime(g.log('-1', '--pretty="%cI"', 'test.xml')[1:-7], "%Y-%m-%dT%H:%M:%S") + timedelta(minutes=60)
sys.stderr.write("Total time lapsed : %s \n" %str((dt.now() - file_age).total_seconds()))