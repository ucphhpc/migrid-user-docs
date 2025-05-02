WebDAVS
=======

WebDAV is a popular protocol to access remote storage using extensions to the HTTP protocol, and it can be secured with TLS/SSL in the same way.


We refer to this secured version as WebDAVS, and recent versions of Microsoft Windows, MacOS and Linux support this protocol out of the box, so that it is possible to access remote content as if it was in a local folder on your computer.
There is no need to install additional software and you can access your files in a secure fashion.
It should be noted that WebDAVS was built for simple web page publishing, so it is neither particularly efficient for bigger data transfers nor robust against network glitches.
Thus, we genereally recommend looking at one of the SFTP-based solutions, where `SSHFS with SFTP </sections/sif/networkdrive/sshfs/index>`_ is a popular option if performance and stability is a concern.

Firstly, you need to go to your **Setup** page at SIF and configure a strong password to enable WebDAVS, and click **Save WebDAVS Settings**. Please note that your Login Details including your automatic login username is shown on that page.


Once you have set it up, you can find our guide for Windows, MacOS and Linux linked below.

⏩️ :doc:`Setup WebDAVS on Windows </sections/sif/networkdrive/webdavs/windows>`

⏩️ :doc:`Setup WebDAVS on MacOS </sections/sif/networkdrive/webdavs/macos>`

⏩️ :doc:`Setup WebDAVS on MacOS </sections/sif/networkdrive/webdavs/macos>`

.. toctree::
   :maxdepth: 1
   :hidden:

   Windows </sections/sif/networkdrive/webdavs/windows>
   MacOS </sections/sif/networkdrive/webdavs/macos>
   Linux </sections/sif/networkdrive/webdavs/linux>
