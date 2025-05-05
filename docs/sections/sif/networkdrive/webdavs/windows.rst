.. _sif-networkdrive-wdavs:

Setup WebDAVS on Windows
========================

.. _sif-networkdrive-wdavssetup:

Setup WebDAVS via Windows File Manager
--------------------------------------

In Windows it is possible to access WebDAVS services directly from the built-in file manager. With the **Map network drive** or the **Add a network location** button available navigating to the **Computer** location.
Please note that Windows 7 only provides the latter functionality inside the **Map network drive** wizard while Windows 8 and later exposes it as a dedicated button.

First click **Map network drive** to launch the wizard.

Select which drive letter you want to use (Z: in the example) and enter the SIF server URL from the **WebDAVS** setup tab and click **Finish** to actually connect.
In most cases the server URL `https://sif-io.erda.dk <https://sif-io.erda.dk>`_ is used.

You will then be prompted for your automatic username and the password you entered on the **WebDAVS** setup tab. The automated username will be *yourmail@projectName*.

Click OK to login and complete the wizard. Your SIF files and folders should appear up in the standard file manager mapped as the chosen drive letter.

As long as you are online you can use the files there just like your local files. When you are done working on the data, you can right-click the mapped drive and select *Disconnect* to close the mapping.

Next time you start your computer you can easily access the project data again using the saved mapped drive from the same **Computer** location.

Importantly you need to always log in first and provide your two-factor token on the SIF web page before you can access the mapped drive.

It is also possible to make the remote content available as a so-called network location by filling in the server URL from above directly in the *Folder* field of the **Add network location** wizard.


