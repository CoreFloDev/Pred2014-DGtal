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
    print("Usage: dump_ast.py [dir file]")
    sys.exit()

# load Clang
clang.cindex.Config.set_library_file('/usr/lib/llvm-3.6/lib/libclang.so')
index = clang.cindex.Index.create()


allowedExt = ['.h','.cpp','.ih']
CK = clang.cindex.CursorKind

types = {"TInteger"  : {"Type":"DGTal::int64_t","Renommage":"i64"},
         "TQuotient" : {"Type":"DGTal::int64_t","Renommage":"i64"},
         "TMap"      : {"Type":"StdMapRebinder","Renommage":"MapRebinder","requireInclude":["/home/florent/projet/DGtal/src/DGtal/base/StdRebinders.h"]}}


print bcolors.OKGREEN+"--- Starting swig generation ---"+bcolors.ENDC

# test with only one source
sourcePath = '/home/florent/projet/DGtal/src/DGtal/arithmetic/LighterSternBrocot.h'
translation_unit = index.parse(sourcePath, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])
templateFound = traverse(translation_unit.cursor,None,sourcePath)
templates = []
includes = [sourcePath]

# generate template name and template instance
for t in templateFound:
    instance = t+"<"
    instanceName = t
    parameters = templateFound[t]
    for p in parameters:
    
        if instanceName != t:
            instance = instance+","
        instance = instance + types[p]["Type"]
        instanceName = instanceName + types[p]["Renommage"]

        # if the type require include, we add them
        if types[p].has_key("requireInclude"):
            for i in types[p]["requireInclude"]:
                if i not in includes:
                    includes.append(i)

    instance = instance + ">"
    templates.append({"instance":instance,"instanceName":instanceName})

# generate the swig interface
tpl = Template(filename='swig.mako')
output = tpl.render(templates=templates,
                    includes=includes)
print output

f = open('dgtal.i','w')
f.write(output)
f.close()

## list of all file of DGTal
#for dirname, dirnames, filenames in os.walk(sys.argv[1]):

#    # print path to all filenames.
#    for filename in filenames:
#        if filename.endswith(tuple(allowedExt)):
#            sourcePath = os.path.join(dirname, filename)
#            # print sourcePath
#            print sourcePath
#            translation_unit = index.parse(sourcePath, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])
#            traverse(translation_unit.cursor,None,sourcePath)

#    # Advanced usage:
#    # editing the 'dirnames' list will stop os.walk() from recursing into there.
#    if '.git' in dirnames:
#        # don't go into any .git directories.
#        dirnames.remove('.git')
#    
#    if 'doc' in dirnames:
#        dirnames.remove('doc')
