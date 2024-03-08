.. _erda-jupyter-start:

Jupyter
=======

ERDA integrates a set of `Jupyter <https://jupyter.org/>`_ services, which can be used to easily perform a wide range of data analysis and visualization tasks directly on your ERDA data. We rely on the `JupyterLab <https://jupyterlab.readthedocs.io/en/stable/>`_ web interface to provide interactive and flexible *notebooks* with direct and efficient access to your ERDA home directory. In the notebooks you can use various programming languages like `Python` or `R` to explore, analyze or present your data, e.g. for your own research, for interactive presentations or even for teaching purposes.

To get access to these services, click the **Jupyter** button in the navigation menu on the ERDA homepage. Upon clicking it, you are presented with a page where you can select either DAG or MODI.

⏩️ :doc:`DAG </sections/erda/jupyter/dag/index>`
    Data Analysis Gateway (DAG) is a service which provides a set of interactive data analysis nodes for intermediate computation, which can be completed in a short time frame.
    This means that any spawned instance is limited to 2 hours of inactivity before it will be terminated. DAG instances have access to 8 compute threads/cores and 16 GB of memory.
    The spawned instances are non-persistent, meaning that any change made during a session is lost once the server is terminated.
    The only exception to this is the data that is saved in the provided mount directory (i.e. ~/work).

⏩️ :doc:`MODI </sections/erda/jupyter/modi/index>`
    MPI Oriented Development and Investigation (MODI) provides a cluster of 8 compute nodes that can be utilized for long running batch jobs.
    Each node offers dual AMD EPYC 32-core CPUs and 256GB of memory. Nodes are connected with a 25Gbit network providing RoCE for efficient communication.
    The system is configured as a SLURM cluster so that regular SLURM commands like sbatch, squeue, sinfo and friends should be used to schedule and monitor
    your programs running as batch jobs.

    The current setup does not at the moment support interactive functionalities such as srun and similar.

.. important::
   It's particularly important to pay attention to the part about running sbatch commands using the shared modi_mount directory for jobs to succeed.

.. toctree::
   :maxdepth: 3
   :hidden:

   DAG </sections/erda/jupyter/dag/index>
   MODI </sections/erda/jupyter/modi/index>
   MODI Helper scripts <https://modi-helper-scripts.readthedocs.io/en/latest/index.html>
