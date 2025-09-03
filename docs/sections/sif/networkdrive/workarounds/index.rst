===========
Workarounds
===========

Sometimes we need to introduce a workaround either due to limitations in our own systems, or due to how something works at the KU level. Such workarounds are (for now) placed here.


SOCKS5 connection to SIF
=======================

This workaround can sometimes be necessary if you cannot get 2FA to work on your remote KU server.
Based on `https://linuxize.com/post/how-to-setup-ssh-socks-tunnel-for-private-browsing <https://linuxize.com/post/how-to-setup-ssh-socks-tunnel-for-private-browsing>`_.

Prerequisites
-------------

* Server at KU running any flavor of Linux, with SSH access to route your traffic through it.
* A web browser (Google Chrome, Firefox etc.).
* SSH client.


Set up the SSH tunnel
---------------------

Linux and MacOS (tested)
^^^^^^^^^^^^^^^^^^^^^^^^

Run the following command::

  ssh -D 9090 [USER]@[SERVER_IP]

[USER]@[SERVER_IP] - Your remote SSH user and server IP address.

9090 is simply a port number, and can be configured.

Configuring your browser to use proxy
-------------------------------------

Google Chrome (tested)
^^^^^^^^^^^^^^^^^^^^^^

**Linux:**::

  /usr/bin/google-chrome \
    --user-data-dir="$HOME/proxy-profile" \
    --proxy-server="socks5://localhost:9090"

**MacOS:**::

  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --user-data-dir="$HOME/proxy-profile" \
    --proxy-server="socks5://localhost:9090"

**Windows:**::

  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" ^
    --user-data-dir="%USERPROFILE%\proxy-profile" ^
    --proxy-server="socks5://localhost:9090"

 Once open, simply navigate to sif.ku.dk and login. After that, you can use sftp on the machine you SSH'ed to, as you have logged into SIF on that machine through the proxy.

