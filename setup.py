from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": [],
    "zip_include_packages": ["os", "requests"],
}
setup(

       name="WowSimsAutoUpdater",

       version="1.0",

       description="Updates the Cataclysm wowsims exe from github",
       options={"build_exe": build_exe_options},
       executables=[Executable("updater.py")],

   )   