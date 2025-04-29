.. _sif-networkdrive-start:

=====================
Efficient Data Access
=====================

As a SIF user, you can work locally on your cmoputer with your SIF files by connecting SIF as a network drive for efficient and transparently integrated file access through different interfaces.


These interfaces allow you to transfer many or big files more efficiently and to map your individual SIF project files and folders on your local PC or workstation.
In that way you can work with them as if they were local files.


Please note that the strict SIF project isolation applies to these interfaces as well, so you can only have one project open at a time.
If you have more than one SIF project you configure efficient access for each of them individually.


All the interfaces use a secure connection to SIF, so they are accessible from anywhere where you have an Internet connection.
Thus, you do not need VPN or anything like that to access them from outside UCPH.
However, they require you to have an active two-factor authentication session from the same computer for added security.


+--------------------+-------------------------------------------------------------------------+
| 1. WebDAVS         | WebDAVS is an abbreviation for Web-based Distributed Authoring          |
|                    |                                                                         |
|                    | and Versioning. A "S" is for secure, as it all runs on a                |
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

⏩️ :doc:`WebDAVS </sections/sif/networkdrive/webdavs/index>`
   WebDAVS is a popular protocol to access remote storage using extensions to the HTTP protocol and is the simpler option.

⏩️ :doc:`SSHFS with SFTP </sections/sif/networkdrive/sshfs/index>`
   SSHFS with SFTP is another popular option to access remote storage that uses the SSH File Transfer Protocol, and is the more robust, but more complex option.

⏩️ :doc:`Workarounds </sections/sif/networkdrive/workarounds/index>`
   Sometimes workarounds are necessary. Those can be found here.
   
.. toctree::
   :maxdepth: 3
   :hidden:

   WebDAVS </sections/sif/networkdrive/webdavs/index>
   SSHFS with SFTP </sections/sif/networkdrive/sshfs/index>
   Workarounds </sections/sif/networkdrive/workarounds/index>
