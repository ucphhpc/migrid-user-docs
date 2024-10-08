.. _erda-networkdrive-start:

Connect ERDA as a Network Drive
===============================

As a ERDA user, you can work locally on your computer with your ERDA files by connecting ERDA as a network drive for efficient and transparently integrated file access through different interfaces. These interfaces allow you to transfer  files more efficiently and to map your ERDA files and folders on your local PC or workstation. This means that when you make changes to the files via the network drive, the changes directly applies to the files in ERDA.


Network drive access uses a secure connection, making the files available everywhere, as long as you have internet access.
This means that you do *not* need a VPN to work with the files outside UCPH.


You have several options for connecting ERDA as a network drive, but below is a comparison of the two most popular choices:

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


⏩️ :doc:`WebDAVS </sections/erda/networkdrive/webdavs/index>`
   WebDAVS is a popular protocol to access remote storage using extensions to the HTTP protocol and is the simpler option.

⏩️ :doc:`SSHFS with SFTP </sections/erda/networkdrive/sshfs/index>`
   SSHFS with SFTP is another popular option to access remote storage that uses the SSH File Transfer Protocol, and is the more robust, but more complex option.

⏩️ :doc:`FTPS </sections/erda/networkdrive/ftps/index>`
   FTPS is another secure and efficient file transfer protocol built on top of the old FTP protocol, but with proper security added.

.. toctree::
   :maxdepth: 3
   :hidden:

   WebDAVS </sections/erda/networkdrive/webdavs/index>
   SSHFS with SFTP </sections/erda/networkdrive/sshfs/index>
   FTPS </sections/erda/networkdrive/ftps/index>
