#!/usr/bin/python
# vim: set fileencoding=utf-8
import clang.cindex
import sys
import os
import pprint


# function to parse AST
def traverse(node,parent,filename):
    
    try:
        # do compute here
        # All templates
        if node.kind == clang.cindex.CursorKind.CLASS_TEMPLATE and node.location.file.name == filename:
            pprint.pprint(node.displayname)
        
        # ALL templates parameter
        if node.kind in [CK.TEMPLATE_TYPE_PARAMETER,CK.TEMPLATE_TEMPLATE_PARAMETER,CK.TEMPLATE_NON_TYPE_PARAMETER] and parent.kind == clang.cindex.CursorKind.CLASS_TEMPLATE and node.location.file.name == filename:
            # show class name
            pprint.pprint('type : '+node.displayname)
    except:
        pass

    for child_node in node.get_children():
        traverse(child_node,node,filename)


if len(sys.argv) != 2:
    print("Usage: dump_ast.py [dir file]")
    sys.exit()

# load Clang
clang.cindex.Config.set_library_file('/usr/lib/llvm-3.6/lib/libclang.so')
index = clang.cindex.Index.create()

#pprint.pprint(dir(clang.cindex.CursorKind))
#exit()
allowedExt = ['.h','.cpp','.ih']
CK = clang.cindex.CursorKind

# list of all file of DGTal
for dirname, dirnames, filenames in os.walk(sys.argv[1]):

    # print path to all filenames.
    for filename in filenames:
        if filename.endswith(tuple(allowedExt)):
            sourcePath = os.path.join(dirname, filename)
            #print sourcePath
            translation_unit = index.parse(sourcePath, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])
            pprint.pprint(sourcePath)
            traverse(translation_unit.cursor,None,sourcePath)

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')
    
    if 'doc' in dirnames:
        dirnames.remove('doc')
