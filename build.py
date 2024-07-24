"""
See build instructions:
https://github.com/BSMU-ITLab/vision/blob/main/build.py
"""


from pathlib import Path

import bsmu.bone_age.app
import bsmu.bone_age.plugins
from bsmu.vision.app.builder import AppBuilder

if __name__ == '__main__':
    app_builder = AppBuilder(
        file_dir=Path(__file__).parent,
        script_path_relative_to_file_dir=Path('src/bsmu/bone_age/app/__main__.py'),

        app_name=bsmu.bone_age.app.__title__,
        app_version=bsmu.bone_age.app.__version__,
        app_description='Application to predict bone age on hand X-ray images.',

        add_packages=['bsmu.bone_age.app', 'bsmu.bone_age.plugins'],
        add_packages_with_data=[bsmu.bone_age.app, bsmu.bone_age.plugins],
    )
    app_builder.build()
