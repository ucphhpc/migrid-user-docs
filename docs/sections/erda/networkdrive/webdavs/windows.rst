.. _erda-networkdrive-wdavs:
Setup WebDAVS on Windows
========================

.. _erda-networkdrive-wdavssetup:
Setup WebDAVS
-------------

Start by clicking on the green avatar icon at the bottom left corner on the ERDA webpage, and click on "Setup"

.. image:: /images/networkdrive/networkdrive-setup.png

Click on the "WebDAVS" option, and in the Login Details that is also highlighted in the screenshot below, you will
be able to see your personal login details, which you will need to connect WebDAVS as a network drive on your computer.

Create a new, separate password for your WebDAVS access in the field under "Password". The password must consist of at
least eight characters and must contain a combination of lowercase and uppercase letters, numbers, and special characters (at least three of the four types mentioned).

Once you are done, click on "Save WebDAVS Settings."

.. image:: /images/networkdrive/networkdrive-webdavsset.png

that After, click on the fold-out menu on "WebDAVS Network Drive", and copy the URL https://io.erda.dk which you will need shortly.

.. _erda-networkdrive-wdavsmap:
Map Network Drive
-----------------

Click on the File Explorer icon on your computer. Click on "This PC" and from there click on the "Computer" tab.
In that menu, you need to click on "Map network drive" (as shown below)

.. image:: /images/networkdrive/networkdrive-mapfolder.png

Insert the URL https://io.erda.dk in the "Folder" tab and click on "Finish".

You will now be asked to log in using the username written under "Login Details" on the top of the page (your e-mail) and the password you chose. Tick "Remember my credentials" (only do this if you don't share your computer with others) and click "OK".

.. TIP::
   The password is not automatically the same password as the one you use when you log into ERDA's web pages, and we recommend for security reasons that you make these two differ, and thus create a unique password for WebDAVS.

ERDA is now connected as a network drive with a chosen drive name, and you now have access to all your data in ERDA via your computer! When you are connected to the internet, you can work in the files in the same way as with your other local files, and any changes you make are applied directly to the files in ERDA.

.. TIP::
   Your connection will not persist through restarts, so the next time you log into your computer, you need to click on the drive and click "OK" in the popup "Connect to io.erda.dk" if you have previously ticked "Remember my credentials". If not, you need to enter your username and chosen password once again.

.. _erda-networkdrive-wdavsdisc:
Disconnect Network Drive
------------------------

You can disconnect ERDA as a network drive. We recommend this if you share a computer with others.

Right click on the drive, and click on "Disconnect".

.. _erda-networkdrive-wdavsfile:
File size limit of 50 MB
------------------------

Microsoft has set a low limit on the size of the files you can download and upload from WebDAVS locations, which is around 50 MB.

This means that you will receive an error message if you open a file from the network drive that is 50 MB or more.

.. WARNING::
   There is technically a way to increase this limit to 4 GB by applying some modifications in the Registry Editor.
   **We do not support this solution and will not be responsible for any consequences of you using this. We strongly suggest that you instead look into using SSHFS.**

   If you decide to go against our advice, you can find a reference here: `https://www.wintips.org/fix-error-0x800700df-the-file-size-exceeds-the-limit-allowed-and-cannot-be-saved-in-sharepoint-webdav/ <https://www.wintips.org/fix-error-0x800700df-the-file-size-exceeds-the-limit-allowed-and-cannot-be-saved-in-sharepoint-webdav/>`_


