.. _erda-jupyter-dag:

DAG
===

Welcome to the page dedicated to Data Analysis Gateway (DAG) user documentation.

DAG provides a set of interactive data analysis nodes for intermediate computation, which can be completed in a short timeframe.
This means that any spawned instance is limited to **2 hours of inactivity before it will be terminated**.
DAG instances have access to 8 compute threads/cores and 16GB of memory.
The spawned instances are non-persistent, meaning that **any change made during a session is lost once the server is terminated**.
The only exception to this is the data that is saved in the provided mount directory (i.e. ~/work).


You can run interactive data analysis sessions e.g. in a Python or R environment with direct access to all your ERDA data.
The built-in Jupyter Terminal extends the options with a multitude of command line tools.
A number of software packages are already available in the different Jupyter instances, but sometimes you may still want to run additional software there.
Please refer to :ref:`erda-jupyter-dag-installation` for details on how to install packages on DAG, either momentarily or more permanently via adding it to the docker stack that runs similar packages.

.. NOTE:
   We are working on a solution whith greater DIY customization of the notebook images, but for now please contact us at our support email if you have additional permanent software wishes.


.. _erda-jupyter-dag-installation:

Installing packages (session)
-----------------------------

To install packages which last throughout the current session, you may simply open a terminal while within the DAG environment, and install it via the relevant package installer.
For the Python notebooks, please refer to :ref:`erda-jupyter-dag-python`, whereas for the Julia packages, refer to :ref:`erda-jupyter-dag-julia`.

.. _erda-jupyter-dag-python:

Python
^^^^^^

For Python and Jupyter extension packages it may work to simply install temporarily with pip or
pip3 inside the session via the Terminal in the main Jupyter Launcher window, or by writing a
standard Python requirements.txt file in your ERDA home and run it interactively like
``pip3 install -r requirements.txt``
from the Jupyter Terminal.
Please note that you need to use python2 or python3 specifically if you want to use such pip or pip3
installed packages respectively directly from the Terminal.

Alternatively you can install Python software dependencies like e.g. the scikit-image package
directly in the Jupyter Notebook itself by evaluating
``!pip3 install scikit-image``
in a cell.

At the moment installing software that requires compilation or come with other external
dependencies is not generally supported for your own sessions.
To ensure that packages you install will stick around between different sessions, pass the ``--user`` flag
to the pip or pip3 install command. This will ensure that the package is installed into your own
home ``__{service}_config__`` directory, which persists between the individual Jupyter sessions.

.. _erda-jupyter-dag-r:

R / RStudio
^^^^^^^^^^^

For R packages, DAG supports personal persistent installation into your own workspace.
When utilizing the ``install.packages()`` command in the Terminal, Notebook, or R-Studio the designated
packages will be installed into your local ~/work/__dag_config__/R/libs/ directory, which is hosted
on ERDA and thus preserved across DAG sessions.
Subsequent to updates being released to DAG notebooks, issues might be encountered with version
conflicts between your old persistent packages and the updates. The most straight-forward solution
then is to clear out your old packages and install a new version of them. This can be done either
through the Terminal with
``rm -fr ~/work/__dag_config__/R/libs/*``
or in an R environment with:
``unlink(“~/work/__dag_config/R/libs/*”, recursive=TRUE)``
Afterwards the packages can be installed with the mentioned install.packages() command if needed.

.. _erda-jupyter-dag-julia:

Julia
^^^^^

For Julia packages, DAG supports both installation directly into your notebook environment, or through the command terminal.
To install in a notebook, you can use ``using Pkg`` and then ``Pkg.add(x)`` where ``x`` is the wanted package, before executing the block it is placed in.
To install it through the command terminal, you can run Julia before using the same commands as with the notebook.

.. _erda-jupyter-dag-other:

Other packages and install
^^^^^^^^^^^^^^^^^^^^^^^^^^

It is also possible to use the conda package manager to install additional software in running sessions.
You can use
``conda install -y -n ENV PACKAGE``
from the Jupyter Terminal where ENV is typically python2, python3 or r depending on the notebook
and your working environment.
Similarly use
``conda search NAME``
to search for available packages.


.. _erda-jupyter-dag-installation-persistent:

Suggesting packages and adding new notebooks
--------------------------------------------

If you want something available to more people in an easy-to-use manner, you can either contact us via our support mail, or check out our `GitHub <https://github.com/ucphhpc/nbi-jupyter-docker-stacks>`_ and create a pull request.
