
.. _erda-twofactor:

=========================
Two-factor Authentication
=========================

.. Security::
   To increase security, we recommend that you use two-factor authentication for all ERDA access.

   
With two-factor authentication, you can add an extra verification step to the login process which authenticates you. In addition to asking about something you know (in this case your username and password), an account protected by two-factor authentication will also request a token from an app you have on either your phone, tablet or desktop.


Setup
-----

When setting up two-factor authentication, you must complete a one-time wizard.

Click the green avatar in the bottom left corner. Click "Setup".

.. image:: /images/authenticator/authenticator-wizard.png

Click on the button "Okay, let's go!"

.. image:: /images/authenticator/authenticator-go.png

A wizard will now appear in ERDA which you must follow, either via its text in the wizard or by following along here.


Download App
^^^^^^^^^^^^

You need to install a TOTP Authenticator client on either a phone or tablet, like `Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator>`_, `FreeOTP <https://freeotp.github.io/>`_, `Yubico Authenticator <https://www.yubico.com/products/yubico-authenticator/#h-download-yubico-authenticator>`_, `Bitwarden <https://bitwarden.com/download/>`_ or `NetIQ Advanced Authentication <https://www.microfocus.com/en-us/cyberres/identity-access-management/advanced-authentication>`_. Find any of these where you normally download apps, and click "I've got it installed!".

.. Note::
   If you only have a private mobile phone/tablet and you do not want to use it, you may request a small device that you can use instead. Contact support@erda.dk for further information.


Import personal Two-Factor Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Import your personal two-factor code with "Scan your Personal QR code" or type your personal key code.

.. image:: /images/authenticator/authenticator-import.png


**Example with Scan your personal QR code:**

After clicking the button, a QR code pops up in ERDA.

Open your downloaded app and find the option to scan a QR code. The screenshot below is from the *Google Authenticator* app.

.. image:: /images/authenticator/authenticator-scanqrcode.png

Now scan the QR code you have just opened in the wizard on ERDA. Point your device's camera at the QR code (The app may ask for permission to use your camera. Allow this). Now the app scans the QR code and you may click "Done importing" on ERDA.

Your application should now have a profile which generates a six-digit token, which changes every 30 seconds.


Verify that it works
^^^^^^^^^^^^^^^^^^^^

After downloading and importing your personal two-factor code, you can verify that it works properly by clicking the *Verify* button. A pop-up window automatically appears, and you must enter the token which shows up in your app. Please note that the token changes after 30 seconds, and will not work after that. Click the **Verify** button in the pop-up and it will confirm whether your two-factor is set up correct.

.. image:: /images/authenticator/authenticator-verify.png


Enable Two-Factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tap the slider button under *Enable 2-FA for KU/UCPH OpenID web login* to switch it from grey/off to green/on.

.. image:: /images/authenticator/authenticator-toggle.png

Additional two-factor authentication options for WebDAVS, SFTP and FTPS are now shown. These are protocols which you primarily need if you want to use ERDA as a network drive on your own computer.

If you are not sure whether you are going to use ERDA as a network drive, we recommend that you activate all three slider buttons by switching them to green/on.

Click *Save 2-Factor Auth Settings*.

Your ERDA account is now protected with two-factor authentication.
