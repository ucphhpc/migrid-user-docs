.. _erda-archiving-start:
.. include:: ../../../shared.rst


.. |delete| image:: /_static/archive_delete.svg
   :width: 16px
   :height: 2ex
   :class: no-scaled-link
.. |info| image:: /_static/archive_information.svg
   :width: 16px
   :class: no-scaled-link
.. |wrench| image:: /_static/archive_wrench.svg
   :width: 16px
   :class: no-scaled-link      

================================
Archives and backups in |migrid|
================================
You can secure your data outside |migrid| itself. Doing so increases long-term accessibility, and
guards against losing data.

An *archive* is a snapshot of one or more files in |migrid|. They are preserved in the state of creation time.
Think of taking a still picture or creating a zip file; the original files are subject to change, while the
archive are frozen in time.


.. accordion:: Why use archives?

 * You have invaluable data that you want to keep safe.
 * Frozen archives are stored extra secure with long-term guarantee (10 years).
 * Attach Digital Object Identifier (DOI) to your data.
 * Recurring backup can be created as archives.

.. accordion:: Which type of data should be archived?

 * Mandatory when handing in PhD theses
 * Data that is used in publications or datasets.
 * Useful or required when submitting a paper to a conference or journal
 * Protecting a (historic) dataset from getting altered
 * Making backups on daily, weekly or say monthly basis

.. accordion:: Two types of archives

 #. **Backup archives** - Allows for one-time or recurring backups, and manual recovery of data.
 #. **Frozen archives** - Provides a snapshot of one or more files, frozen in time. There are two subtypes:
 
    #. Private, frozen archives - Snapshots are held in private archives.
    #. Public, frozen archives -  Snapshot for papers, public datasets, etc. Archive can obtain a DOI.

    Note that frozen archives are not available for user deletion.

|

.. _erda-archiving-overview_frozen_archives:

Getting started with Archives
=============================

Initially your archives list is empty, but after adding a
few different archives, it could look like the example below.

.. lightbox:: archives/archives-frozenarchives.png
   :alt: Frozen Archives screenshot with example archives.
   :caption: Example of Archives page with an finalized, frozen archive.
   :class: with-border
   :percentage: 80 95 95

	   
|	   
	   
You can inspect a frozen archive with the green info icon |info|, edit unfinished archives with the green
wrench icon |wrench|, and, if the system is configured to allow deletion of archives, you can remove them
again with the red remove icon |delete|.

.. _erda-archiving-create_archive:


The following steps will guide you through the process of creating, editing, and finalizing and viewing an archive.

Step 1: Create an archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  New archives can be created with the **Create a new frozen archive** link at the bottom of the page.

  As an example, we could create a new archive called "Article Data ..." by filling out the resulting form
  like this:

.. lightbox:: archives/archives-createnew.png
    :alt: Creating a new archive screenshot
    :class: with-border
    :caption: Example creation of an archive. Name and description has been filled out, and a file welcome.txt is being added. Notice that archive has been set to become publicly available.
    :percentage: 80 95 95


|
		 
Step 2: Add files/directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can add files to your archive in two ways:

1. Use the **Add file/directory** button to select existing files from your |migrid| storage. This opens a file browser where you can:
   - Double-click to select individual files
   - Right-click folders to select their entire contents

2. Use the **Add upload** button to upload new files directly to the archive, similar to the upload feature in the **Files** section.

Once you've added all your files and set your publishing preferences, click **Save and Preview** to review your archive contents.

.. lightbox:: archives/archives-create-freezearchive.png
    :alt: Creating a new archive screenshot
    :class: with-border
    :percentage: 80 95 95

|

.. Note::
  The archiving process creates a snapshot of your selected files while keeping the originals intact in |migrid|.
  You can continue to modify your original files freely - any changes you make will not affect the archived version.

|

.. _erda-archiving-preview_public_archive:

Step 3: Preview & Finalize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  If you selected Make Dataset Publicly available you can use the Preview publishing button to see
  a draft of the published archive. At this point, you can continue modifying the archive contents like
  above through the Edit archive button, until at last you click Finalize archive to actually
  permanently freeze it and thereby mark it ready for additional tape archiving. This is necessary to
  get the extra data safety and guarantee that it will remain available for at least 10 years.


.. lightbox:: archives/archives-finalizearchive.png
    :alt: Screenshot of page which allows user to modify, preview, and finalize creation of public archive
    :class: with-border
    :percentage: 80 95 95

|

.. _erda-archiving-view_resulting_archive:


Step 4: Viewing the finalinzed archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  After finalizing you can use the "View details" button to see all the details registered about it on the
  view archive page and use the links to access the associated files.

.. lightbox:: archives/archives-show-freezearchive-details.png
    :alt: Screenshot of the page View details, which shows the finalized archive
    :class: with-border
    :percentage: 80 95 95
      
|

.. _erda-archiving-doi_for_public_archives:

DOI for public archives
=======================
For archives with publish enabled, we also integrate access to request a Digital Object Identifier
(DOI) after finalizing the archive. From view archive you click "Register Archive DOI" at the
bottom to reach the central UCPH DOI registration portal. Typically, this involves clicking through a
standard UCPH login and small DOI intro dialogue to get to the actual DOI metadata schema shown.

.. lightbox:: archives/archives-register-doi.png
    :alt: Screenshot of Digital Object Identifier registration form
    :class: with-border
    :percentage: 80 95 95

|

Once filled and submitted the request is sent through the UCPH validation procedure and if
everything is okay you receive a permanent ``https://dx.doi.org/XYZ`` URL alias for your published
archive data. From then on you can e.g. use it as a reference in research papers or provide it to
research colleagues interested in re-using your published data.

.. Note::
  | The "minting" of DOIs is done by Data DOI, a service external to |migrid|.
  | |migrid|'s page listing the DOI publications are updated on a daily basis.
  | Once form has been submitted, you can expect to receive an confirmation email from Data DOI within a short time.
  | Please refer `Data DOI's website <https://kunet.ku.dk/work-areas/research/data/data-sharing/data-doi/Pages/default.aspx>`_ for further information and support.



