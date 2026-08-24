from cx_Freeze import setup, Executable

files = {
    "packages": ["pygame", "domain"],
    "include_files": [
        "asset/",
        "database/"
    ]
}

executables = [
    Executable(
        "main.py",
        target_name="main.exe"
    )
]

setup(
    name="Overcooked",
    version="1.0",
    description="Restaurant app",
    options={"build_exe": files},
    executables=executables
)