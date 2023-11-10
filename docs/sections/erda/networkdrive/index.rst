.. _erda-networkdrive-start:

===============================
Connect ERDA as a Network Drive
===============================

If you are an ERDA user, you can work locally on your computer with your ERDA files by connecting ERDA as a network drive.
When you make changes to the files via the network drive, the changes are applied directly to the files in ERDA.

Network drive access uses a secure connection, and the files are available wherever you are, as long as you have internet access.
This means that you do *not* need a VPN to work with the files outside UCPH.

You have two options for connecting ERDA as network drives:

+--------------------+-------------------------------------------------------------------------+
| 1. WebDAVS         | WebDAVS is an abbreviation for Web-based Distributed Authoring          |
|                    |                                                                         |
|                    | and Versioning. We add an "S" for secure, as it all runs on a           |
|                    |                                                                         |
|                    | secure connection.                                                      |
|                    |                                                                         |
|                    |   ☑ Can be used from Windows, Mac and Linux/UNIX                        |
|                    |                                                                         |
|                    |   ☑ Easy to get started                                                 |
|                    |                                                                         |
|                    |   ☑ Does not require software installation                              |
|                    |                                                                         |
|                    |   𐄂 Limit on file size on Windows - 50 MB as a starting point           |
|                    |                                                                         |
|                    |   𐄂 Sensitive to network outages                                        |
|                    |                                                                         |
|                    |   𐄂 WebDAVS is less efficient at transferring many and/or large files.  |
|                    |                                                                         |
+--------------------+-------------------------------------------------------------------------+
| 2. SSHFS with SFTP | SSHFS is an abbreviation for Secure Shell File System and is the        |
|                    | client                                                                  |
|                    |                                                                         |
|                    | that connects an SFTP service as a network drive on your                |
|                    |                                                                         |
|                    |                                                                         |
|                    | computer. SFTP is an abbreviation for Secure File Transfer Protocol.    |
|                    |                                                                         |
|                    |   ☑ Can be used from Windows, Mac and Linux/UNIX                        |
|                    |                                                                         |
|                    |   ☑ Efficient handling of many/large files                              |
|                    |                                                                         |
|                    |   ☑ Robust regarding network outages                                    |
|                    |                                                                         |
|                    |   ☑ Unlimited file size                                                 |
|                    |                                                                         |
|                    |   𐄂 You have to install two small programs - once                       |
|                    |                                                                         |
+--------------------+-------------------------------------------------------------------------+


.. TIP::
   **We recommend SSHFS with SFTP, particularly for users who feel comfortable with the technology and/or who work intensively with their data.**

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

AFter that, click on the fold-out menu on "WebDAVS Network Drive", and copy the URL https://io.erda.dk which you will need shortly.

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

   If you decide to go against our advice, you can find a reference here: `https://www.wintips.org/fix-error-0x800700df-the-file-size-exceeds-the-limit-allowed-and-cannot-be-saved-in-sharepoint-webdav/<https://www.wintips.org/fix-error-0x800700df-the-file-size-exceeds-the-limit-allowed-and-cannot-be-saved-in-sharepoint-webdav/>`_

.. _erda-networkdrive-mdavs:

Setup WebDAVS on macOS
======================

.. _erda-networkdrive-mdavssetup:

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

AFter that, click on the fold-out menu on "WebDAVS Network Drive", and copy the URL https://io.erda.dk which you will need shortly.

.. _erda-networkdrive-mdavsmap:

Map Network Drive
-----------------

Open "Finder" on your computer and navigate to the top to click on "Go", before "Connect to server...".

Insert the URL https://io.erda.dk and click "Connect".


Make sure it is ticked to "Registered User" under "Connect As:" before inserting the information written under "Login Details" on the top of the ERDA Setup page for WebDAVS,
which is your e-mail and the password you chose.
Tick "Remember this password in my keychain" (only do this if you do not share your computer with others) and click "Connect".

.. TIP::
   The password is not necessarily the same password as the one you use when you log onto ERDA's web pages, and we recommend for security reasons that you make these two different.

ERDA is now connected as a network drive, and you have access to all your data in ERDA via your computer!
When you are connected to the internet, you can work in the files in the same way as with your other local files, and any changes
you make are applied directly to the files in ERDA.

.. TIP::
   Your connection will not persist through restarts, so the next time you log onto your computer, you need to click through the "Go" menu again.

.. _erda-networkdrive-mdavsdisc:

Disconnect Network Drive
------------------------

You can disconnect ERDA as a network drive, and we recommend this if you share a computer with others.

Right click on the drive, and click on 'Eject "io.erda.dk"'.

.. _erda-networkdrive-wsftp:

Setup SSHFS with SFTP on Windows
================================

SFTP is a secure and efficient file transfer protocol similar to the old FTP protocol, but with proper security built in.
It relies on the security mechanisms of the `OpenSSH <http://www.openssh.com/>`_ suite of applications and it is supported
by a number of clients on all popular platforms. Some platforms even integrate it natively in the general file manager, so that no extra software is required.


.. _erda-networkdrive-wsftpsetup:

Setup SSHFS
-----------
To setup SSHFS, go onto the ERDA user homepage, and press the avat icon in the bottom left corner, and then on "Setup".

Click on the "SFTP" tab, and either create a new, separate password for your SFTP access in the field under "Password" or add your public key if you prefer that way. If you choose the password route, the password must consist of at least eight characters and contain a combination of lowercase and uppercase letters, numbers, and special characters (at least three out of the four types mentioned).

After you have concluded this step, click on "Save SFTP Settings".

.. image:: /images/networkdrive/networkdrive-loginmethod.png

From here, you click on the fold-out menu called "SSHFS/SFTP Network Drive" and copy the path starting with "\\sshfs\" as you will need it momentarily.


.. _erda-networkdrive-wsftpinstall:
Install WinFsp and SSHFS-Win
----------------------------

On Windows, our recommended way of working with SFTP is through the `SSHFS client <https://github.com/winfsp/sshfs-win#----sshfs-win--sshfs-for-windows>`_.

Thus, you need to go to the linked GitHub page and install the two programs, either by following their installation guide in the GitHub, or by reading on here.

To install without Winget, you first click on the `WinFsp <https://github.com/winfsp/winfsp/releases/tag/v2.0>`_ link, and then click "DOWNLOAD WINFSP". Follow their installation guide, before returning back to the sshfs-win GitHub page.

Click on either of the two buttons under Download, or click the link under the installation section, and pick either the x64 or x86 depending on your computer's architecture.

If you are unsure about your computer's architecture, oyu can find it under Start -> Settings -> System -> About

.. image:: /images/networkdrive/networkdrive-about.png

When you are done installing both programs, you can connect a network drive.


Tips for installing on a UCPH computer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On a standard UCPH computer (B machine), you have access to installing programs by clicking "Request administrator access" in the bottom right corner.

.. image:: /iamges/networkdrive/networkdrive-ucphcomp.png

If you have a spcieal, secure UCPH computer (A machine), you need to contact UCPH IT to install the two programs.


.. _erda-networkdrive-wsftpmapdrive:
Map Network Drive
-----------------

Click on the File Explorer icon on your computer and click on "This PC" on the side. On top, click on the "Computer" tab and click on the "Map network drive" at the top of the screen.

.. image:: /images/networkdrive/networkdrive-mapbutton.png

Next to "Folder", paste the path from ERDA Setup page under "SSHFS/SFTP Network Drive", where it follows the format "\\sshfs\<your-unique-identifier>". Click on "Finish" once you are done.

This will open a login dialogue prompt if you chose password, and you will have to enter your UCPH name, and the password you chose for your SFTP access. Tick "Remember me" if you are using your own personal computer for ease of use, and click "OK".

.. image:: /images/networkdrive/networkdrive-loginprompt.png

ERDA is now connected as a network drive with a chosen drive name, and you now have access to all your data in ERDA via your computer's programs and file management! When you are online, you can work in the files in the same way as with your other local files, and any changes you make will be applied directly to the files in ERDA.

.. TIP::
   Every time you log into your computer, you need to click on the network drive to connect if you have previously ticked "Remember me", and if not, you will need to enter your previously chosen password before it reconnects.


.. _erda-networkdrive-wsftpdisconnect:
Disconnect Network Drive
------------------------

You can disconnect ERDA as a network drive, and we recommend you do this if you share a computer with others.

Right click on the drive and click "Disconnect".

.. _erda-networkdrive-msftp:

Setup SSHFS with SFTP on macOS
==============================

WIP
