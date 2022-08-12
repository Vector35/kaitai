#!/usr/bin/env python

# script to compile all kaitai struct formats to ./formats
# eg:
# ./compile-all ~/Downloads/kaitai_struct_formats

import os
import sys

exceptions = ['icc_4.ksy']

if __name__ == '__main__':
    HOME = os.environ['HOME']

    path_formats = sys.argv[1]
    path_out = os.path.join('./formats')
    path_compiler = 'kaitai-struct-compiler'

    import_statements = []

    for folder, subfolder, fnames in os.walk(path_formats):
        if folder.endswith('.git'):
            continue
        if folder.endswith('.circleci'):
            continue
        if folder.endswith('_build'):
            continue

        # compile each
        for fname in fnames:
            if not fname.endswith('.ksy'):
                continue
            if fname in exceptions:
                continue

            path_ksy = os.path.join(folder, fname)
            fname_ksy = os.path.split(path_ksy)[1]
            path_py = os.path.join(path_out, fname_ksy.replace('ksy','py'))

            path_rel = os.path.relpath(os.path.split(path_ksy)[0], path_formats)
            depth_path_rel = len(path_rel.split('/'))
            print('%s (%d deep from path_formats)' % (path_rel, depth_path_rel))
            
            module_name = fname[0:-4]
            class_name = ''.join(map(lambda x: x.capitalize(), module_name.split('_')))
            #import_statements.append('from kaitai_struct_formats.' + path_rel.replace('/','.') + '.' + module_name + ' import ' + class_name)
            import_statements.append('from formats.%s import %s' % (module_name, class_name))

            if os.path.exists(path_py):
                if os.path.getmtime(path_ksy) <= os.path.getmtime(path_py):
                    print('%s up to date, skipping' % path_py)
                    continue

            cmd = '%s --debug --target python --import-path %s --python-package . %s --outdir %s' % \
                (path_compiler, path_formats, path_ksy, path_out)
            print(cmd)
            os.system(cmd)

            lines = None
            with open(path_py, 'r') as fp:
                lines = fp.readlines()

    print('writing import-all.py')
    with open('import-all.py', 'w') as fp:
        fp.write('#!/usr/bin/env python\n')
        fp.write('# generated from compile-all.py\n')
        fp.write('import sys\n')
        fp.write('sys.path.append(\'corelogic\')\n')
        for import_statement in sorted(import_statements):
            fp.write('try:\n')
            fp.write(f'    {import_statement}\n')
            fp.write(f'except Exception as e:\n')
            fp.write(f'    print("ERROR: {import_statement}")\n')
        fp.write('print(\'DONE\')\n')
