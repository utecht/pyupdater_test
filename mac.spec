# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/joseph/work/updater_test/main.py'],
             pathex=['/Users/joseph/work/updater_test', '/Users/joseph/work/updater_test'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/joseph/work/updater_test/env/lib/python3.7/site-packages/pyupdater/hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='mac',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mac')
app = BUNDLE(coll,
             name='mac.app',
             icon=None,
             info_plist={
              'NSHighResolutionCapable': 'True'
             },
             bundle_identifier=None)
