.. _erda-archiving-start:

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

============================
Archives and backups in ERDA
============================
This section shows how to secure your data inside ERDA itself. It can increase long-term accessibility, and prevent data loss.

An *archive* is a snapshot of one or more files in ERDA. They are preserved in the state of creation time.
Think of a taking a still picture or creating a zip file; the original files are subject to change, while the archive are frozen in time.

.. raw:: html

   <details>
   <summary><a>Fold ud, fold ind eksempel</a></summary>

.. code-block:: python

   lots_of_code = "this text block"

.. raw:: html

   </details>

Benefits of copying files into an archive:
 * frozen archives are stored in separate physical location
 * extra secure, long-term storage guaranteed (10 years)
 * attach Digital Object Identifier (DOI) to your publications
 * archives can be set up as recurring backup 

Example cases for using archives:
 * Mandatory when handing in PhD theses
 * Useful or required when submitting a paper to a conference or journal
 * Protecting a (historic) dataset from getting altered
 * Making backups on daily, weekly or say monthly basis

There are two types of archives in ERDA:

 #. **Backup archives** - Allows for one-time or recurring backups, and manual recovery of data.
 #. **Frozen archives** - Provides a snapshot of one or more files, frozen in time. Two subtypes
 
    #. Private, frozen archives - Snapshots are held in private archives.
    #. Public, frozen archives -  Snapshot for papers, public datasets, etc. Archive can obtain a DOI.


.. Note:: Archiving does not remove the files you may have selected from ERDA, but only saves a snapshot of the current contents. That is, you are free to keep working on such files afterwards and without causing changes to the archived version.

.. important:: 
   - ERDA archives provides extra data security **inside** ERDA itself.
   - Always keep data securely stored in copies/backups **outside** ERDA as well.
   - Remember "One is none, two is one" when it comes to data security

| 

Overview of Frozen Archives
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Initially your archives list is empty, but after adding a
few different archives, it could look like the example below.

.. image:: /images/archives/archives-frozenarchives.png
   :alt: Frozen Archives screenshot with example archives.
   :class: with-border
   :width: 90%
   :align: center
	   
|	   
	   
You can inspect a frozen archive with the green info icon |info|, edit unfinished archives with the green
wrench icon |wrench|, and, if the system is configured to allow deletion of archives, you can remove them
again with the red remove icon |delete|.

|

Creating an archive
^^^^^^^^^^^^^^^^^^^
**Step 1: Create**

  New archives can be created with the **Create a new frozen archive** link at the bottom of the page.

  As an example, we could create a new archive called "Article Data ..." by filling out the resulting form
  like this:

.. image:: /images/archives/archives-createnew.png
   :alt: Creating a new archive screenshot
   :class: with-border
   :width: 90% 
   :align: center

|
		 
**Step 2: Add files/directories**

  Existing private or shared ERDA files can be added with the **Add file/directory** button, and new
  files can be uploaded directly to the archive with the **Add upload** button. The former button brings
  up a file select dialog in which you can select from your ERDA files: double-click individual files
  or right-click and choose select to pick entire folders. The latter button opens an upload dialog like
  the one from **Files**. When you are done adding files and have marked if you want the archive files to
  be published, you can click **Save and Preview** to inspect the current contents.

.. image:: /images/archives/archives-create-freezearchive.png
   :alt: Creating a new archive screenshot
   :class: with-border
   :width: 90%
   :align: center
	   
|	   

**Step 3: Preview & Finalise**
  If you selected Make Dataset Publicly available you can use the Preview publishing button to see
  a draft of the published archive. At this point, you can continue modifying the archive contents like
  above through the Edit archive button, until at last you click Finalize archive to actually
  permanently freeze it and thereby mark it ready for additional tape archiving. This is necessary to
  get the extra data safety and guarantee that it will remain available for at least 10 years.


.. image:: /images/archives/archives-finalizearchive.png
   :alt: Screenshot of page which allows user to modify, preview, and finalize creation of public archive
   :class: with-border
   :width: 90%	   
   :align: center
	   
|

**Step 4: View the resulting archive**
  After finalizing you can use the "View details" button to see all the details registered about it on the
  view archive page and use the links to access the associated files.

.. image:: /images/archives/archives-show-freezearchive-details.png
   :alt: Screenshot of the page View details, which shows the finalized archive
   :class: with-border
   :width: 90%	   
   :align: center
      
|

DOI for public archives
^^^^^^^^^^^^^^^^^^^^^^^
For archives with publish enabled, we also integrate access to request a Digital Object Identifier
(DOI) after finalizing the archive. From view archive you click "Register Archive DOI" at the
bottom to reach the central UCPH DOI registration portal. Typically, this involves clicking through a
standard UCPH login and small DOI intro dialogue to get to the actual DOI metadata schema shown.

.. image:: /images/archives/archives-register-doi.png
   :alt: Screenshot of Digital Object Identifier registration form
   :class: with-border
   :width: 90%
   :align: center	   

Once filled and submitted the request is sent through the UCPH validation procedure and if
everything is okay you receive a permanent ``https://dx.doi.org/XYZ`` URL alias for your published
archive data. From then on you can e.g. use it as a reference in research papers or provide it to
research colleagues interested in re-using your published data.
