# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['test.py'],
             pathex=['D:\\Shared drives\\Shubh Data\\Everything Python\\Completed\\Study Time\\Scripts'],
             binaries=[],
             datas=[('Python.ico', '.')],
             hiddenimports=[],
             hookspath=['D:\\Shared drives\\Shubh Data\\Everything Python\\Completed\\Study Time\\Scripts'],
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
          name='Study Buddy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='Python.ico')
