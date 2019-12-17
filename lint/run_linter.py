
import os
from yamllint.config import YamlLintConfig
from yamllint import linter

rootdir = '.'
conf = YamlLintConfig('extends: default')
rep = open('./lint/report.txt', "a+")
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if '.yml' in file:
            f = open(os.path.join(subdir, file))
            rep.write(linter.run(f, conf))
