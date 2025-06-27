.. _erda-backup-start:

Automatic Backup to ERDA
========================

It is possible to combine Advanced Data Access with the free and open backup program `Duplicati <https://duplicati.com/>`_ to achieve automatic backup of your computer(s) to ERDA.
Duplicati stores backup files in a special container form, which allows it to store e.g. special files and exotic file names, that may otherwise be problem to save directly on ERDA.
It also means that it's easy to encrypt the entire backup, so that no one else can read it, even if they should illegitimately obtain access to the ERDA storage.

Duplicati exists in a user-friendly graphical flavor as well as a command-line flavor better suited for backup of e.g. servers and certain NAS-systems.
On this page, we only cover the graphical flavor.

Setup Duplicati on ERDA
-----------------------

In short setting up Duplicati requires two steps, namely creating the ERDA-specific configuration at your ERDA Duplicati Settings followed by import of the resulting configuration(s) in the Duplicati on your computer.

First you go to your ERDA **Setup** page and choose the Duplicati tab.

.. image:: /images/auto-backup/duplicati-tab.png

Enter one or more names you want to use for your backup(s) in the Backups field.
E.g. the name of the computer or the folders you want to backup.

The remaining fields are optional and can just be left as is.
Please note that you need to have configured password login for SFTP or whichever protocol you choose for Duplicati, however.
Click **Save Duplicati Settings** when done and wait for the automatic page refresh where links to a .json file now appear for each backup name you entered in the Backups field.
In this case where you enter enter *Documents* you'll get *Documents.json* as a result.
You can download the json file(s) by right-clicking on the link(s) and then something like **Save link as** or **Save target as** depending on which web browser you use.


Setting the program up
----------------------

The second half of the setup is to import the resulting json file(s) directly in Duplicati.

Download and install the latest release from the linked website, and finish the install wizard.

When installed Duplicati should automatically start and show the status overview.
However, you can always open Duplciati by right-clicking the status icon in the system tray next to the clock and choose Open there.
Select **Add backup** from the menu in Duplicati, and for Configurataion file, browse to the json you downloaded earlier and click **Import**.

On the next page all ERDA settings are pre-filled from the configuration file - except the password field.
This password is the one you previously configured for the selected protocol on ERDA I.e. with the default choices, it is the SFTP password you set on your ERDA SFTP Setup page, and so on.

At this point you can click **Test connection** to verify that the connection and login is correctly configured before proceeding with Next.

Select which local folders to include in the backup, like e.g. *My Documents* and click Next.
Please note that by default Duplicati runs on behalf of your regular user, so it may not have access to all system files or to shadow copy facilities available on some platforms.
In effect this meanas that you may see warnings or errors if you select folders outside your user space or e.g. folders with application data in active use.
Either leave out any such folders from your backup selection, or follow the Duplicati documentation on running Duplicati as a privileged user.

Optionally further tune the frequency for automatic backup runs and click.
You do not need to touch the **Allowed days**, as no specific days selected has the same effect as ticking them all.

On the last page **Options** you can specify how long backups should be kept and click **Save**.

When set up, you can click **Run now** next to it saying that it has never run.


You need to repeat the procedure in Duplicati for all backup .json files you have created in ERDA Duplicati setup.

After a successful backup run you can always recover selected files or folders from backup with the **Restore** entry in Duplicati or by folding out the backup entry and selecting **Restore files...**.
