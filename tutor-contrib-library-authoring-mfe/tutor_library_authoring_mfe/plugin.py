from glob import glob
import os
import pkg_resources

from tutor import hooks as tutor_hooks

from .__about__ import __version__

########################################
# CONFIGURATION
########################################

tutor_hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        ("LIBRARY_AUTHORING_MICROFRONTEND_VERSION", __version__),
        ("LIBRARY_AUTHORING_MFE_APP", {
            "name": "library-authoring",
            "repository": "https://github.com/openedx/frontend-app-library-authoring",
            "port": 3001,
            # "version": "me/my-custom-branch", # optional
        })
    ]
)


########################################
# INITIALIZATION TASKS
########################################

MY_INIT_TASKS: list[tuple[str, tuple[str, ...]]] = [
    ("cms", ("library_authoring_mfe", "jobs", "init", "cms.sh")),
]

# For each task added to MY_INIT_TASKS, we load the task template
# and add it to the CLI_DO_INIT_TASKS filter, which tells Tutor to
# run it as part of the `init` job.
for service, template_path in MY_INIT_TASKS:
    full_path: str = pkg_resources.resource_filename(
        "tutor_library_authoring_mfe", os.path.join("templates", *template_path)
    )
    with open(full_path, encoding="utf-8") as init_task_file:
        init_task: str = init_task_file.read()
    tutor_hooks.Filters.CLI_DO_INIT_TASKS.add_item((service, init_task))

########################################
# TEMPLATE RENDERING
########################################

tutor_hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        pkg_resources.resource_filename("tutor_library_authoring_mfe", "templates"),
    ]
)

########################################
# PATCH LOADING
########################################

# For each file in tutor_library_authoring_mfe/patches,
# apply a patch based on the file's name and contents.
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutor_library_authoring_mfe", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        tutor_hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))


########################################
# DOCKER IMAGE BUILD/PULL/PUSH
########################################

# Build, pull and push the library authoring mfe image

# IMAGES_BUILD: Filter[list[tuple[str, tuple[str, ...], str, tuple[str, ...]]], [Config]]= Filter('images:build')
# List of images to be built when we run tutor images build ....

# Parameters
# tasks (list[tuple[str, tuple[str, ...], str, tuple[str, ...]]]) –

# list of (name, path, tag, args) tuples.

# name is the name of the image, as in tutor images build myimage.

# path is the relative path to the folder that contains the Dockerfile. For instance ("myplugin", "build", "myservice") indicates that the template will be read from myplugin/build/myservice/Dockerfile

# tag is the Docker tag that will be applied to the image. It will be rendered at runtime with the user configuration. Thus, the image tag could be "{{ DOCKER_REGISTRY }}/myimage:{{ TUTOR_VERSION }}".

# args is a list of arguments that will be passed to docker build ....

# config (dict) – user configuration.


# tutor_hooks.Filters.IMAGES_BUILD.add_item(
#     (
#         "library-authoring-mfe",
#         ("plugins", "mfe", "build", "mfe"),
#         "{{ DOCKER_REGISTRY }}bsmithtcril/library-authoring-mfe:{{ MFE_VERSION }}",
#         (),
#     )
# )

# IMAGES_PULL: Filter[list[tuple[str, str]], [Config]]= Filter('images:pull')
# List of images to be pulled when we run tutor images pull ....

# Parameters
# tasks (list[tuple[str, str]]) –

# list of (name, tag) tuples.

# name is the name of the image, as in tutor images pull myimage.

# tag is the Docker tag that will be applied to the image. (see IMAGES_BUILD).

# config (dict) – user configuration.

# tutor_hooks.Filters.IMAGES_PULL.add_item(
#     (
#         "library-authoring-mfe",
#         "{{ DOCKER_REGISTRY }}bsmithtcril/library-authoring-mfe:{{ MFE_VERSION }}",
#     )
# )

# IMAGES_PUSH: Filter[list[tuple[str, str]], [Config]]= Filter('images:push')
# List of images to be pushed when we run tutor images push .... Parameters are the same as for IMAGES_PULL.

# tutor_hooks.Filters.IMAGES_PUSH.add_item(
#     (
#         "library-authoring-mfe",
#         "{{ DOCKER_REGISTRY }}bsmithtcril/library-authoring-mfe:{{ MFE_VERSION }}",
#     )
# )

# ENDENDEND
# ENDENDEND
# ENDENDEND
# ENDENDEND
# ENDENDEND
# ENDENDEND
# ENDENDEND
# ENDENDEND


# # Enable the MFE in the CMS FEATURES configuration
# hooks.Filters.ENV_PATCHES.add_item(("cms-env-features",
#     "ENABLE_LIBRARY_AUTHORING_MICROFRONTEND: true"
# ))

# # Set the URL of the MFE:
# hooks.Filters.ENV_PATCHES.add_item(("cms-env",
#     'LIBRARY_AUTHORING_MICROFRONTEND_URL = "http://blarg.com"'
# ))

# # Currently Tutor does not set CMS_BASE correctly - it still defaults to 'localhost:18010' not 'localhost:8001' like we need
# hooks.Filters.ENV_PATCHES.add_item(("openedx-cms-development-settings",
#     'CMS_BASE = "studio.local.overhang.io:8001"'
# ))

# # Fix blockstore's file storage; by default it initializes
# # BUNDLE_ASSET_STORAGE_SETTINGS using MEDIA_ROOT but before Tutor gets a chance
# # to change MEDIA_ROOT so it defaults to /edx/var/edxapp/media/ which will give
# # a permissions error.
# hooks.Filters.ENV_PATCHES.add_item(("openedx-development-settings",
#     'BUNDLE_ASSET_STORAGE_SETTINGS = dict(STORAGE_CLASS="django.core.files.storage.FileSystemStorage", STORAGE_KWARGS=dict(location="/openedx/media/blockstore/", base_url="http://localhost:8000/media/blockstore/"))'
# ))

# # Tell the tutor-mfe plugin about this MFE so we can build, run, and use it:
# hooks.Filters.CONFIG_DEFAULTS.add_item(("LIBRARY_AUTHORING_MFE_APP", {
#     "name": "library-authoring",
#     "repository": "https://github.com/openedx/frontend-app-library-authoring",
#     "port": 3001,
#     "env": {
#         "development": {
#             # Tutor requires the name of the MFE in the URL so this file won't be found at /xblock-bootstrap.html,
#             # which is the default location for development.
#             "SECURE_ORIGIN_XBLOCK_BOOTSTRAP_HTML_URL": "/library-authoring/xblock-bootstrap.html",
#             "LMS_BASE_URL": "http://local.overhang.io:8000",
#             "STUDIO_BASE_URL": "http://studio.local.overhang.io:8001",
#         },
#     }
# }))

# # Tutor overwrites webpack.dev.config.js, but this MFE depends on some code in that file to work correctly in
# # development, so we have to restore it here manually.
# # https://github.com/openedx/frontend-app-library-authoring/blob/b95c198b/webpack.dev.config.js
# hooks.Filters.ENV_PATCHES.add_item(("mfe-webpack-dev-config","""
# const fs = require('fs');

# // If this is the Library Authoring MFE, apply this fix:
# if (fs.existsSync("src/library-authoring/edit-block/LibraryBlock/xblock-bootstrap.html")) {
#     const path = require('path');
#     const CopyWebpackPlugin = require('copy-webpack-plugin');
#     module.exports = merge(module.exports, {
#     plugins: [
#         new CopyWebpackPlugin({
#         patterns: [{
#             context: path.resolve(__dirname, 'src/library-authoring/edit-block/LibraryBlock'),
#             from: 'xblock-bootstrap.html',
#         }],
#         }),
#     ],
#     });
# }
# """))