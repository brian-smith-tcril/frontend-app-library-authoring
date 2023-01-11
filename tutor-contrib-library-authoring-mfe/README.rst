library_authoring_mfe plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

Installation
------------

Follow these instructions to enable this microfrontend:

1. Install `tutor nightly <https://github.com/overhangio/tutor/tree/nightly>`_: ``pip install -e 'git+https://github.com/overhangio/tutor.git@nightly#egg=tutor'``
2. Install `tutor-mfe nightly <https://github.com/overhangio/tutor-mfe/tree/nightly>`_: ``pip install -e 'git+https://github.com/overhangio/tutor-mfe.git@nightly#egg=tutor-mfe'``
3. Install `tutor-contrib-blockstore <https://github.com/brian-smith-tcril/tutor-contrib-blockstore/>`_: ``pip install -e 'git+https://github.com/brian-smith-tcril/tutor-contrib-blockstore#egg=tutor-contrib-blockstore'``
4. Install this plugin: ``pip install -e 'git+https://github.com/brian-smith-tcril/frontend-app-library-authoring.git@tutor-prod#egg=tutor-contrib-library-authoring-mfe&subdirectory=tutor-contrib-library-authoring-mfe'``
5. Enable the blockstore plugin: ``tutor plugins enable blockstore``
6. Enable this plugin: ``tutor plugins enable library_authoring_mfe``
7. Save the tutor config: ``tutor config save``
8. Build mfe image: ``tutor images build mfe`` (if you have trouble here you may need to run it with ``--no-cache``) 
9. Launch tutor: ``tutor local launch``

If you want to run this MFE in
`development mode <https://github.com/overhangio/tutor-mfe/#mfe-development>`
(to make changes to the code), instead of step 9 above, do this::

   cd /path/to/frontend-app-library-authoring
   tutor dev run --mount=. library-authoring npm install  # Ensure NPM requirements are installed into your fork.
   tutor dev start --mount=. library-authoring

Setup
-----
1. Ensure you have created a user: https://docs.tutor.overhang.io/local.html#creating-a-new-user-with-staff-and-admin-rights
2. Ensure you have created an organization: http://studio.local.overhang.io/admin/organizations/organization/
3. Log in to studio: http://studio.local.overhang.io/home/
4. Click on the libraries tab
