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

    for folder, subfolder, file_names in os.walk(path_formats):
        if folder.endswith('.git'):
            continue
        if folder.endswith('.circleci'):
            continue
        if folder.endswith('_build'):
            continue

        # compile each
        for file_name in file_names:
            if not file_name.endswith('.ksy'):
                continue
            if file_name in exceptions:
                continue

            path_ksy = os.path.join(folder, file_name)
            file_name_ksy = os.path.split(path_ksy)[1]
            path_py = os.path.join(path_out, file_name_ksy.replace('ksy','py'))

            path_rel = os.path.relpath(os.path.split(path_ksy)[0], path_formats)
            depth_path_rel = len(path_rel.split('/'))
            print(f'{path_rel} ({depth_path_rel} deep from path_formats)')
            
            module_name = file_name[0:-4]
            class_name = ''.join(map(lambda x: x.capitalize(), module_name.split('_')))
            import_statements.append(f'from formats.{module_name} import {class_name}')

            if os.path.exists(path_py):
                if os.path.getmtime(path_ksy) <= os.path.getmtime(path_py):
                    print('%s up to date, skipping' % path_py)
                    continue

            cmd = (f'{path_compiler} --debug --target python '
                   f'--import-path {path_formats} '
                   f'--python-package . {path_ksy} '
                   f'--outdir {path_out}')
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
