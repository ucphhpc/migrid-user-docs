.. _erda-archiving-start:

================
Archives in ERDA
================

The Archives page provides a method to archive or freeze a snapshot of one or more files.

This is required e.g. in relation to handing in PhD theses and in certain cases required or convenient when
submitting a paper to a conference or journal.

There are two kinds of archives in ERDA

 * **Backup archives** - Allows for one-time or recurring backups, and manual recovery of data
 * **Frozen archives** - Provides a snapshot of a dataset, frozen in time. Two subtypes:
  * *Private, frozen archives* - Snapshot are held in private archives
  * *Public, frozen archives* - Extra secure, long term storage guaranteed + DOI for public data

.. Note:: Archiving does not remove the files you may have selected from ERDA, but only saves a snapshot of the current contents. That is, you are free to keep working on such files afterwards and without causing changes to the archived version.
   
Overview of Frozen Archives
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Initially your archives list is empty but after adding a
few different archives it could look like the example below.

.. image:: /images/archives/archives-frozenarchives.png
   :alt: Frozen Archives screenshot with example archives.
   :class: with-border
   :width: 90%  
	   
You can inspect a frozen archive with the green info icon , edit unfinished archives with the green
wrench icon and if the system is configured to allow deletion of archives you can remove them
again with the red remove icon.

|

Creating an archive
^^^^^^^^^^^^^^^^^^^
**Step 1: Create**

New archives can be created with the **Create a new frozen archive** link at the bottom of the page.

As an example we could create a new archive called Article Data ... by filling out the resulting form
like this:

.. image:: /images/archives/archives-createnew.png
   :alt: Creating a new archive screenshot
   :class: with-border
   :width: 90% 
   
**Step 2: Add files/directories**

Existing private or shared ERDA files can be added with the **Add file/directory** button and new
files can be uploaded directly to the archive with the **Add upload** button. The former button brings
up a file select dialog in which you can select from your ERDA files: double-click individual files
or right-click and choose select to pick entire folders. The latter button opens an upload dialog like
the one from **Files**. When you are done adding files and have marked if you want the archive files to
be published, you can click **Save and Preview** to inspect the current contents.

.. image:: /images/archives/archives-create-freezearchive.png
   :alt: Creating a new archive screenshot
   :class: with-border
   :width: 90%
	   
|	   

**Step 3: Preview & Finalize**

If you selected Make Dataset Publicly available you can use the Preview publishing button to see
a draft of the published archive. At this point you can continue modifying the archive contents like
above through the Edit archive button, until at last you click Finalize archive to actually
permanently freeze it and thereby mark it ready for additional tape archiving. This is necessary to
get the extra data safety and guarantee that it will remain available for at least 10 years.


.. image:: /images/archives/archives-finalizearchive.png
   :alt: Screenshot of page which allows user to modify, preview, and finalize creation of public archive
   :class: with-border
   :width: 90%	   

|

**Step 4: View the resulting archive**
	   
After finalizing you can use the View details button to see all the details registered about it on the
view archive page and use the links to access the associated files.

.. image:: /images/archives/archives-show-freezearchive-details.png
   :alt: Screenshot of the page View details, which shows the finalized archive
   :class: with-border
   :width: 90%	   

|

DOI for public achives
^^^^^^^^^^^^^^^^^^^^^^
For archives with publish enabled we also integrate access to request a Digital Object Identifier
(DOI) after finalizing the archive. From view archive you click Register Archive DOI at the
bottom to reach the central UCPH DOI registration portal. Typically this involves clicking through a
standard UCPH login and small DOI intro dialog to get to the actual DOI metadata schema shown.

.. image:: /images/archives/archives-register-doi.png
   :alt: Screenshot of Digital Object Identifier registration form
   :class: with-border
   :width: 90%	   

Once filled and submitted the request is sent through the UCPH validation procedure and if
everything is okay you receive a permanent https://dx.doi.org/XYZ URL alias for your published
archive data. From then on you can e.g. use it as a reference in research papers or provide it to
research colleagues interested in re-using your published data.
