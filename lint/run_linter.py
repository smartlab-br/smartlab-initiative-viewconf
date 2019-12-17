
import os
from yamllint.config import YamlLintConfig
from yamllint import linter

rootdir = '.'
conf = YamlLintConfig('extends: default')
rep = open('./lint/report.txt', "a+")
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if '.yaml' in file:
            rel_path = os.path.join(subdir, file)
            f = open(rel_path)
            gen = linter.run(f, conf)
            for lint in list(gen):
                rep.write(f'{rel_path}:{lint.line}:{lint.column}: [{lint.level}] {lint.desc} ({lint.rule})\n')
rep.close()
