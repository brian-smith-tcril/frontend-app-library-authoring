library_authoring_mfe plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

This plugin will setup Blockstore and the Library Authoring MFE, so you can
start using it to create v2 Libraries using Blockstore.

Installation and usage
----------------------

**IMPORTANT**: First, you must be using `Tutor Nightly <https://docs.tutor.overhang.io/tutorials/nightly.html>`_, a
recent (July 2022 or newer) version of edx-platform (`master` branch), and the
`Tutor MFE plugin <https://github.com/overhangio/tutor-mfe/>`_.

Then, follow these instructions to enable this microfrontend:

1. Install/enable the blockstore plugin (todo: details)
2. Install this plugin: ``pip install -e 'git+https://github.com/openedx/frontend-app-library-authoring.git#egg=tutor-contrib-library-authoring-mfe&subdirectory=tutor-contrib-library-authoring-mfe'``
3. Enable the plugin: ``tutor plugins enable library_authoring_mfe``
4. Run ``tutor config save``.
5. ``tutor local launch``
6. hopefully everything works? (todo: make it work)

If you want to run this MFE in
`development mode <https://github.com/overhangio/tutor-mfe/#mfe-development>`
(to make changes to the code), instead of step 5 above, do this::

   cd /path/to/frontend-app-library-authoring
   tutor dev run --mount=. library-authoring npm install  # Ensure NPM requirements are installed into your fork.
   tutor dev start --mount=. library-authoring
