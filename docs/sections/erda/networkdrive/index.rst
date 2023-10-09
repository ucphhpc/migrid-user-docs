.. _erda-networkdrive-start:

======================================
Connect ERDA as a Network Drive (ERDA)
======================================

If you are an ERDA user, you can work locally on your computer with your ERDA files by connecting ERDA as a network drive.
When you make changes to the files via the network drive, the changes are applied directly to the files in ERDA.

Network drive access uses a secure connection, and the files are available wherever you are, as long as you have internet access.
This means that you do *not* need a VPN to work with the files outside UCPH.

You have two options for connecting ERDA as network drives:

+--------------------+-------------------------------------------------------------------------+
| 1. WebDAVS         | WebDAVS is an abbreviation for Web-based Distributed Authoring and      |
|                    | Versioning. We add an "S" for secure, as it all runs on a secure        |
|                    | connection.                                                             |
|                    |                                                                         |
|                    |   * Can be used from Windows, Mac and Linux/UNIX                        |
|                    |   * Easy to get started                                                 |
|                    |   * Does not require software installation                              |
|                    |   * Limit on file size - 50 MB as a starting point                      |
|                    |   * Sensitive to network outages                                        |
|                    |   * WebDAVS is less efficient at transferring many and/or large files.  |
|                    |                                                                         |
+--------------------+-------------------------------------------------------------------------+
| 2. SSHFS with SFTP | SSHFS is an abbreviation for Secure Shell File System and is the        |
|                    | client that connects an SFTP service as a network drive on your         |
|                    | computer. SFTP is an abbreviation for Secure File Transfer Protocol.    |
|                    |                                                                         |
|                    |   * Can be used from Windows, Mac and Linux/UNIX                        |
|                    |   * Efficient handling of many/large files                              |
|                    |   * Robust regarding network outages                                    |
|                    |   * Unlimited file size                                                 |
|                    |   * You have to install two small programs - once                       |
|                    |                                                                         |
+--------------------+-------------------------------------------------------------------------+


.. TIP::
   **We recommend SSHFS with SFTP, particularly for users who feel comfortable with the technology and/or who work intensively with their data.**
