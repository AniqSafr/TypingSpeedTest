from cx_Freeze import *
import sys
includefiles=['icon.ico']
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Typing Test",
     "TARGETDIR",
     "[TARGETDIR]\main.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Typing Speed Test",
    author="Xyla",
    name="Typing Test",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='icon.ico',
        )
    ]
)
