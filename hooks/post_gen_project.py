import os
import subprocess

print(os.getcwd())

dirs = [
    './src/sql',
    './plot'
]
for d in dirs:
  os.mkdir(d)

subprocess.call(['git', 'init'])
subprocess.call(['git', 'flow', 'init'])

