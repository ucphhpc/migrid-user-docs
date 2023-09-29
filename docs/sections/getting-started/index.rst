Getting Started
===============

If you are working within the MODI platform. The modi-helper-scripts and its associated CLI tools should already be installed and available via the regular Terminal shell.
You can test this by trying to tab-expand on the "modi-" prefix, which should give your output similar to this::

    $ modi-
    modi-delete-environment  modi-new-environment     modi-new-job

If you want to install the modi-helper-scripts on your own machine or another platform, you can do so by following the instructions below.
The modi-helper-scripts can be installed in a number of ways, including:

Via pypi::

    pip install modi-helper-scripts

Via the GitHub repository::

    pip install git+https://github.com/ucphhpc/modi-helper-scripts.git

Or via cloning and installing it yourself::

    git clone https://github.com/ucphhpc/modi-helper-scripts.git
    cd modi-helper-scripts
    make install

Either of these methods will install a number of CLI tools, all of which can typically be expanded in a shell environment, given that their installed
destination directory is included in your current PATH::

    $ modi-
    modi-delete-environment  modi-new-environment     modi-new-job
