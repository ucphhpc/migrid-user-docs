FTPS
====

FTPS is another secure and efficient file transfer protocol built on top of the old FTP protocol, but with proper security added.
It relies on the security mechanisms of TLS/SSL and it is supported by a number of clients on all popular platforms.
As far as we know none of the major platforms integrate it natively in the general file manager, so you probably need to install a dedicated client to use it.

You generally need to first open the *FTPS* tab on your Setup page at ERDA and configure how you want to authenticate to our FTPS server.
Enter a password that you want to login with and click *Save FTPS Settings*.
Please also note the login details including the automatic username shown there.

.. info::
   Our SFTP server is more thoroughly tested and allows the stronger public key authentication, but our FTPS server may deliver higher throughput, so feel free to use either in accordance with your needs.

⏩️ :doc:`Setup FileZilla up (Windows/MacOS/Linux) </sections/erda/networkdrive/ftps/filezilla>`
