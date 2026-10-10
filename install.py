#!/usr/bin/env python3
"""Install six class replacements into a local JAR after making a backup."""
import argparse
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil,sys,tempfile,os

def main():
    ap=argparse.ArgumentParser(description='Patch an existing Urtuk desktop JAR (original backup is preserved).')
    ap.add_argument('jar',type=Path)
    args=ap.parse_args()
    jar=args.jar.expanduser().resolve()
    patch_dir=Path(__file__).resolve().parent/'patch'
    replacements={str(f.relative_to(patch_dir)).replace(os.sep,'/'):f.read_bytes() for f in patch_dir.rglob('*.class')}
    if not jar.is_file(): sys.exit(f'Game JAR not found: {jar}')
    if not replacements: sys.exit('No patches found.')
    backup=jar.with_name(jar.name+'.before-urtuk-qol.bak')
    if backup.exists(): sys.exit(f'Backup already exists, please move it first: {backup}')
    with ZipFile(jar) as src:
        names=set(src.namelist())
        missing=sorted(set(replacements)-names)
        if missing: sys.exit('Incompatible JAR — missing original classes:\n'+'\n'.join(missing))
        if src.testzip() is not None: sys.exit('Original JAR archive integrity check failed.')
    shutil.copy2(jar,backup)
    fd,tempname=tempfile.mkstemp(prefix='urtuk-patch-',suffix='.jar',dir=str(jar.parent));os.close(fd)
    try:
        with ZipFile(jar) as src, ZipFile(tempname,'w') as dst:
            for info in src.infolist():
                contents=replacements.get(info.filename)
                if contents is None: contents=src.read(info.filename)
                dst.writestr(info,contents)
        with ZipFile(tempname) as verify:
            for name,data in replacements.items():
                if verify.read(name)!=data: raise RuntimeError(f'Verification failed: {name}')
        os.replace(tempname,jar)
    except Exception:
        if os.path.exists(tempname):os.unlink(tempname)
        raise
    print(f'Patched {len(replacements)} classes in {jar}')
    print(f'Original backup: {backup}')

if __name__=='__main__': main()
