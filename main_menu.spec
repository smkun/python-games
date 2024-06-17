# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main_menu.py'],
             pathex=['/path/to/your/project'],
             binaries=[],
             datas=[('Hangman', 'Hangman'),
                    ('Landscaper', 'Landscaper'),
                    ('pong', 'pong'),
                    ('Tic_Tac_Toe', 'Tic_Tac_Toe')],
             hiddenimports=[],
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
          name='main_menu',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)