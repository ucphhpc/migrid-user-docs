WebDAVS
=======

WebDAV is a popular protocol to access remote storage using extensions to the HHTP protocol, and it can be secured with TLS/SSL in the same way.

We refer to this secured version as WebDAVS, and recent versions of Microsoft Windows, MacOS and Linux support this protocol out-of-the-box, so it is possible to access remote content as if it was in a local folder.
There is no need to install additional software and you can access your files in a secure fashion, and you can get relatively easily started with working on your data through WebDAVS.
However, it should be noted that WebDAVS was built for simple web page publishing, so it is neither particularly efficient for bigger data transfers nor robust against network glitches.
Thus, we generally recommend looking at one of the SFTP-based solutions, where `SSHFS with SFTP </sections/erda/networkdrive/sshfs/index>`_ is a popular option if performance and stability is a concern.

With that being said, you can find our guide for Windows and MacOS linked below. If you are interested in a file synchronization service resembling Dropbox, but which you are permitted to use as a KU/UCPH Employee, then you can also check out Seafile, also linked below.

⏩️ :doc:`Setup WebDAVS on Windows </sections/erda/networkdrive/webdavs/windows>`

⏩️ :doc:`Setup WebDAVS on MacOS </sections/erda/networkdrive/webdavs/macos>`

⏩️ :doc:`ERDA Seafile </sections/erda/seafile/index>`


.. toctree::
   :maxdepth: 1
   :hidden:

   Windows </sections/erda/networkdrive/webdavs/windows>
   MacOS </sections/erda/networkdrive/webdavs/macos>
