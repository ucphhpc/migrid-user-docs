.. _erda-networkdrive-msftp:

Setup SSHFS with SFTP on macOS
==============================

.. _erda-networkdrive-applesilicon:

Macs with Apple Silicon
^^^^^^^^^^^^^^^^^^^^^^^

With the new Apple Silicon, Mac introduced more security and therefore restrictions to their computers. In order to use the program that SSHFS relies on, you will need to allow it to access the kernel extensions. 

You can follow the below guidelines to activate the kernel extensions for 3rd party programs, or contact your local IT department for assistance.

First of all, make sure that this guide is handy, as you will have to restart your computer. Turn off your Mac and wait for it to turn off completely. A mac is completely shut down when the screen is black an all light (including Touch Bar) is turned off.

After that, press the power button and hold it down until the "Loading setup options" text is shown. Click on "Options", then on "Continue". Select your user if you are asked to do so, and click "next". Input your computer's password when prompted.

After getting into the menu, click on the "Utilities" button up on the top or similar button, before clicking on the "Startup Security Utility" button. Select your main system if you have several, and click "Unlock..." if prompted. Then. click on "Security Policy...". In this menu, you have to tick the "Reduced Security" rather than "Full Security", and tick the "Allow user management of kernel extensions from identified developers", click OK afterwards.

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


.. _erda-networkdrive-msftpdisconnect:

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

