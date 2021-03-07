# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['view.py'],
             pathex=['/Users/yuya/python-master/study03_teisyutu'],
             binaries=[],
             datas=[('/Users/yuya/.pyenv/versions/3.8.7/lib/python3.8/site-packages/eel/eel.js', 'eel'), ('html', 'html')],
             hiddenimports=['bottle_websocket', 'cmath'],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='view',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
