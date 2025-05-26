.. _erda-dataimpexp-start:

Data Import/Export
==================

We offer the ability to import and export data from ERDA in an efficient way.
Typical scenarios include fetching big data sets from dedicated Linux/UNIX servers or from imaging sites, where data are recorded on-site with remote access afterwards.
This is probably mostly relevant for users with a certain experience in handling big data sets.

ERDA comes with low-level background import and export of data through different efficient transfer protocols like SFTP/FTPS/RSYNC/HTTPS and WebDAVS.

From the **Files** page you can right-click in the file manager and in the menu under *Data Transfers* you can find *Import* and *Export*.

There is also the dedicated page. The corresponding navigation menu entry is not shown by default to keep it simple,  but you can **Add** it to your home page, which you can read more about on <erda-homepage-start>`_.

On the **Data Transfers** page you can create an external data transfer and either import or export data via a handy form.


.. _erda-dataimpexp-transfer:

External Data Transfer
----------------------

Select whether you want to import or export data via **Action**, and (optionally) give it a transfer ID / name to recognize it by.

Select **Protocol**, and specify **Host and port**.

Choose your **Login method** and specify the **Source path(s)**, clicking on the button *Add another source field* in case you have several **source paths**.

Add **Destination path** and **Exclude path(s)**.

If you transfer from a slow site, you should set **Enable compression**, and otherwise make sure it is unset.

You can specify your mail for a notification on completion, and then click **Request transfer**.

