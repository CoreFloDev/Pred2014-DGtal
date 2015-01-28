#!/usr/bin/python
# vim: set fileencoding=utf-8
import clang.cindex
import sys
import os
import pprint
import traceback
from mako.template import Template

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# function to parse AST
def traverse(node,parent,filename):

    ret = {}

    try:
        # do compute here
        if node.location.file.name == filename:

            # All templates
            if node.kind == CK.CLASS_TEMPLATE:
                parameterOfTemplate = []
                for child in node.get_children():
                    if child.kind in [CK.TEMPLATE_TYPE_PARAMETER,CK.TEMPLATE_TEMPLATE_PARAMETER,CK.TEMPLATE_NON_TYPE_PARAMETER]:
                        parameterOfTemplate.append(child.displayname)
                ret[node.spelling] = parameterOfTemplate

    except:
        pass

    for child_node in node.get_children():
        trav = traverse(child_node,node,filename)
        ret = dict(ret.items() + trav.items())
        
    return ret


if len(sys.argv) != 2:
    print("Usage: list_type.py [dgtal src]")
    sys.exit()

# load Clang
clang.cindex.Config.set_library_file('/usr/lib/llvm-3.6/lib/libclang.so')
index = clang.cindex.Index.create()

allowedExt = ['.h','.cpp','.ih']
CK = clang.cindex.CursorKind

print bcolors.OKGREEN+"--- Starting list type generation ---"+bcolors.ENDC

# list of all file of DGTal
for dirname, dirnames, filenames in os.walk(sys.argv[1]):

    # print path to all filenames.
    for filename in filenames:
        if filename.endswith(tuple(allowedExt)):
            sourcePath = os.path.join(dirname, filename)
            # print sourcePath
            
            translation_unit = index.parse(sourcePath, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])
            ret = traverse(translation_unit.cursor,None,sourcePath)
            if len(ret) != 0:
                print bcolors.OKBLUE+sourcePath+bcolors.ENDC
                pprint.pprint(ret)

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')
    
    if 'doc' in dirnames:
        dirnames.remove('doc')
