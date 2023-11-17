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


:doc:`WebDAVS </sections/erda/networkdrive/webdavs/index>`

   
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

SFTP is a secure and efficient file transfer protocol similar to the old FTP protocol, but with proper security built in.
It relies on the security mechanisms of the `OpenSSH <http://www.openssh.com/>`_ suite of applications and it is supported
by a number of clients on all popular platforms. Some platforms even integrate it natively in the general file manager, so that no extra software is required.

If you have a newer Mac with Apple Silicon, then you will need to follow the below subsection. Otherwise, you can proceed to :ref:`erda-networkdrive-msftpsetup` section.


.. _erda-networkdrive-applesilicon:
Macs with Apple Silicon
^^^^^^^^^^^^^^^^^^^^^^^

With the new Apple Silicon, Mac introduced more security and therefore restrictions to their computers. In order to use the program that SSHFS relies on, you will need to allow it to access the kernel extensions. 

You can follow the below guidelines to activate the kernel extensions for 3rd party programs, or contact your local IT department for assistance.

First of all, make sure that this guide is handy, as you will have to restart your computer. Turn off your Mac and wait for it to turn off completely. A mac is completely shut down when the screen is black an all light (including Touch Bar) is turned off.

After that, press the power button and hold it down until the "Loading setup options" text is shown. Click on "Options", then on "Continue". Select your user if you are asked to do so, and click "next". Input your computer's password when prompted.

After getting into the menu, click on the "Utilities" button up on the topor similar button, before clicking on the "Startup Security Utility" button. Select your main system if you have several, and click "Unlock..." if prompted. Then. click on "Security Policy...". In this menu, you have to tick the "Reduced Security" rather than "Full Security", and tick the "Allow user management of kernel extensions from identified developers", click OK afterwards.

You have now enabled kernel extensions, and can proceed with the main guide. Click on the Apple logo in the top-left to restart your computer.


.. _erda-networkdrive-msftpsetup:
Setup SSHFS
-----------

Log onto `ERDA <https://erda.ku.dk/>`_ and click the green icon in the bottom left corner, and click "Setup".

Click on the SFTP tab, and create a password for your SFTP access in the field under "Password". We recommend that you select a separate password than your main one for ERDA. Click on "Save SFTP Settings" once done.

.. TIP::
   The password need to follow the University of Copenhagen's guidelines in terms of passwords, and be at least 12 symbols.


.. _erda-networkdrive-msftpinstall:
Install MacFUSE and SSHFS
^^^^^^^^^^^^^^^^^^^^^^^^^

With SSHFS set up on the ERDA side, you now need to install the SSHFS client, which connects a SFTP-service as a network drive on your computer.

You need to install SSHFS by downloading and running two programs: MacFUSE and SSHFS

You can download the two programs from `this website <https://osxfuse.github.io/>`_.

Open the programs, and follow the installation wizard for each program.

Once you have installed both programs, you can finally connect ERDA as a network drive.

.. IMPORTANT::
   If you have a newer Mac with Apple Silicon, then at the end of the installation you will be prompted to activate the kernel extension. A window will pop up, where you will be asked to open System Settings. Do so and click on the button that has appeared mentioning the program or an extension by "Benjamin Fleischer". After clicking this and being prompted your password, you will need to restart your computer once more to allow the kernel extension to load up as a starting process.


.. _erda-networkdrive-msftpconnectnetwork:
Connect Nerwork Drive
^^^^^^^^^^^^^^^^^^^^^

Open an editor on your computer. (A free and easy tool for mac users is TextEdit, even if it is a rich text editor)

Navigate to the Setup page once more for SFTP, and click on the fold-out menu "SSHFS/SFTP Network Drive", and copy the configuration in the box under "SSHFS Drive on Mac OSX". Insert the text into your editor of choice. If you chose a rich text editor such as TextEdit, then go into "Format" and click ""Make Plain Text". Save this configuration as "config" and make sure that it does not use .txt or similar extension after the file name, and save it as a Unicode file if you are prompted to select which type of file. You can save it on your Desktop for now.

Afterwards, you need to open the terminal on your computer, which you can find via Spotlight search as "Terminal".

.. TIP::
   If a warning message pops up, simply click "OK" to allow "Terminal" to have access to the files.

   
Create the folder ".ssh" in your "~" folder, which should be the one your terminal opened in, and insert the command ``mkdir -p ~/.ssh`` before pressing Enter. Then, you want to insert the command ``touch ~/.ssh/config`` and press Enter to either create or update the timestamp on your config file.

Now you can copy the contents from the file you created earlier into this config file by inserting the command ``cat ~/Desktop/config >> ~/.ssh/config`` into the Terminal before pressing Enter.

After this is done, you need to mount with SSHFS, where one option is to use the following command::
  
  mkdir -p ucph-erda-home && \
    sshfs io.erda.dk: ucph-erda-home -o idmap=user -o reconnect \
      -o iosize=262144

Press Enter after inserting it into your terminal. First time you try to connect ERDA with SFTP / SSHFS, you will be asked to verify the service's fingerprint. Here, you can check if the fingerprint in the terminal corresponds with the one on the ERDA Setup page under "Login Details". Note that the fingerprint can have been updated since this guide was created, and feel free to contact our Support if that is the case.

If it is the same fingerprint, then write ``yes`` and press Enter. You will then be prompted to write a password, and this will be the one you set up in the beginning of this guide. As a security measure, it will not be shown in the terminal, so simply type it and press Enter once done.

ERDA is now connected as a network drive and will be visible on the computer's desktop. You will now have access to all your data in ERDA via your computer and if you are online, then you can work in the files in the same manner as your other local files, and when you save, those changes will be directly transmitted onto the files in ERDA.


.. _erda-networkdrive-msftperror:
Error in the setup
^^^^^^^^^^^^^^^^^^

In case of error in the setup, the SSHFS command will give you the message "remote host has disconnected" in the terminal. If this happens, you can try to test the setup by inserting the command ``sftp io.erda.dk`` and press Enter. If you can log in after that, the setup is correct.

If you still cannot log in, then you need to follow the terminal steps in this guide again, and if you continue to get errors, then you can write to our support at support@erda.dk

Before doing you, please run the command ``sftp -vvv io.erda.dk`` and insert the result in the mail for us to troubleshoot.


.. _erda-networkdrive-msftperror:
Disconnect Network Drive
------------------------

You can disconnect ERDA as a network drive, and we recommend doing this if you share the computer with others.

Right-click on the drive on the Desktop, and click "Push 'macFUSE Volume 0 (sshfs) out".


.. _erda-networkdrive-msftpreconnect:
Reconnect to the Network Drive
------------------------------

When your computer has been turned off, you need to connect the network drive again. You do that by opening the terminal and running the sshfs command::

  mkdir -p ucph-erda-home && \
    sshfs io.erda.dk: ucph-erda-home -o idmap=user -o reconnect \
      -o iosize=262144

If you are experiencing problems in connection the network drive, then it may be because the network drive is connected but not visible. You can try to unmount the network drive by inserting the command ``diskutil unmount force ~/ucph-erda-home`` in the terminal and press Enter. After, you can try to connect the network drive again by running the sshfs command.

