"""cx_Freeze Build configuration for Windows MSI Installer."""

import sys
import os
from pathlib import Path
from cx_Freeze import setup, Executable


def find_data_file(filename):
    if getattr(sys, "frozen", False):
        # The application is frozen
        data_dir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        data_dir = os.path.dirname(__file__)
    return os.path.join(data_dir, filename)


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    # "build_exe": "Installers",
    "includes": [],
    "excludes": ["html", "tcl8", "tcl8.6", "tk8.6", "tkinter", "unittest"],
    "zip_include_packages": [
        "PyQt6",
    ],
    "include_files": [(Path("CC_GUI", "resources").resolve(), "resources")],
    "include_msvcr": True,
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

bdist_msi_options = {
    "add_to_path": False,
    "initial_target_dir": "C:\\CarbonCheck",
    "target_name": "CarbonCheck.msi",
}

icon_file = find_data_file(
    Path("CC_GUI", "resources", "logo_CarbonCheck.ico").resolve()
)
setup(
    name="CarbonCheck",
    version="0.1",
    description="Passive House Model Baseliner and Reporting.",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=[
        Executable(
            "CarbonCheck.py",
            copyright="Copyright (C) 2023 Passive House Accelerator",
            base=base,
            icon=icon_file,
        )
    ],
)
