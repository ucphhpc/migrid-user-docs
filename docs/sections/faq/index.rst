Frequently Asked Questions (FAQ)
================================

How much storage space do I have on ERDA?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There's no space quota as such on the general ERDA storage, but the huge data sets known from high energy physics and bioinformatic databases are examples of data contents not considered suitable for ERDA. Anything within a few tens of terabytes should be fine, and we suggest that you just have a word with us if you want to store more than that.
ERDA also includes a file synchronization service called Seafile, and that particular part may not be so suitable for big data sets, so it comes with a quota of 100 GB per user. 


Is my ERDA data replicated and backed up?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All data on ERDA is automatically replicated over multiple disks with RAID technology. Additionally we frequently make local file system snapshots and transfer the latest one to a remote location on about a monthly basis for disaster recovery situations. Thus, while we do have a number of extra data safety measures, we do not currently guarantee automatic and complete backup of data in your ERDA home folder or in the Workgroup shares. That would simply not be feasible for the biggest data sets there. Only files explicitly duplicated with the Archive feature are guaranteed to be backed up - first to local disk and later also a copy to remote tape for extra data safety. We are working on ways to increase the remote transfer frequency, and perhaps implement instant mirroring or high-availability distribution of a select subset of the storage space.
We recommend our Seafile file synchronization service for any small to medium sized data sets, for which you want automatic file versioning. With that solution you generally have the ability to recover deleted files or 'roll back' files to earlier versions.
Please note that the local storage at the DAG and MODI Jupyter instances is scratch space. Thus, any important data from your analysis there should always explicitly be saved to ERDA for permanent storage. You can conveniently use the work and erda_mount network drives there respectively to do so.


How do I Transfer Entire Folders to/from ERDA?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the ERDA web interface you can only upload/download individual files, so if you e.g. want to upload an entire folder structure there, first pack the folder(s) in a zip or tar file, upload it as usual and then use unpack from the right-click menu on the uploaded file.
Likewise you can use pack on a folder in ERDA, download and unpack it locally.
Alternatively you can use the efficient file/folder handling described in the Network Drive Intro and the User Guide. That makes ERDA appear like just another disk drive, so that you can use your local file manager to copy entire folders to ERDA or otherwise work with your data like they were local.


Can I Share, Exchange and Publish Data in e.g. a Read-only Fashion on ERDA?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, depending on the audience and dynamics of the data to share you can use one of three overall methods.
For permanent read-only publishing just create a new archive from your Archives page and make sure to mark it for public availability.
For more dynamic data you can either share in a read-write manner using the Workgroup shares or make them read-only in the Workgroup administration. Similarly you can do read-only sharing and publishing through the Workgroup web pages. Both are built into the Workgroups and the web pages come in a public and in a group-wide flavor, where the publishing is done by Workgroup owners storing data in the ``public_base`` and ``private_base`` workgroup subdirectories respectively on ERDA. Your Workgroups page includes links to those and to the resulting web pages.
For quick data exchange with anyone and particularly people not on ERDA, we recommend the Share Link feature. From your Files page you can create a share link for a file or folder and choose what kind of read and write access share link recipients should be granted. A similar feature applies for any data you may store in our optional Seafile data synchronization service. Just use the share by email feature to similarly create upload or download shares with optional password and time limit. Both share link methods include the option to send out an invitation with the link directly on email, but they can of course also be manually distributed by other means. Share links can also be accessed with SFTP, FTPS and WebDAVS as described in the user guide.


Is it possible to get a DOI for my ERDA archive?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, since June 2018 we integrate DOI registration.
A number of users have asked about the possibility of assigning a Digital Object Identifier (DOI) to their published ERDA archives. It is getting more common to use such DOIs in research papers in line with the open-access and `Open science <https://en.wikipedia.org/wiki/Open_science>` spirit. UCPH has a license to mint DOIs through `DataCite <https://www.datacite.org/>` and University IT has developed a service to help do that, which we've integrated with ERDA. In practice you create your ERDA freeze archive as usual and select yes for Make Dataset Publicly Available. When satisfied with the archive contents you click **Finalize archive** to permanently freeze it. Afterwards you can use the **Request archive DOI** button on the View archive details page to proceed with the UCPH DOI registration form. At KUNet you can find a `more elaborate DOI introduction <https://kunet.ku.dk/work-areas/research/data/data-sharing/data-doi/Pages/default.aspx>` including a complete visual walk-through of the process to create an archive and assign a DOI. We guarantee the availability of ERDA archives for at least(!) 10 years and the same applies for the UCPH-minted DOIs. 


How are Workgroups managed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Workgroups can be created by academic staff (VIP) as well as technical/administrative staff (TAP) and the creator of a workgroup automatically becomes owner. All user management is left to the owner(s) without interaction from the ERDA system administrators. Co-owners and members can be added either directly using the *Swedish numberplate* or email alias of the user, or indirectly if the user requests owner-/membership on the Workgroups page, and the owner(s) follow the instructions then sent on email about adding the user with the full user ID format. We recommend the intro guide on Workgroups for further details.


Can I have a shared or separate account for our project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, we **cannot** allow such accounts or account aliasing, mainly due to rules and regulations. In case of suspected or alleged abuse we need to be able to uniquely identify who did what and when, and all kinds of anonymous or shared accounts would prevent that. Please refer to the `UCPH information security policy <https://informationssikkerhed.ku.dk/english/is-policy/>` for further details about identity and traceability requirements.
So basically you need to use your own personal and clearly identifiable account for all logins. What you **can** do is to use Workgroups to store data in a shared group folder. In that way the data is not bound to your account specifically and you and your project group can easily manage all account access yourselves through the Workgroup admin page.
Similarly share links can be used for access to particular subfolders if you need to e.g. automate data upload from lab machines without storing your personal login there. Please refer to the user guide for more details. 


Why can I not use certain characters in file names?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ERDA prevents certain characters like "\< \> \{ \| \} \* \? \[ \]" in file names. You may already have run into similar limitations when naming files on your own PC or devices. In order to provide a secure and consistent experience across different platforms, web and advanced interfaces ERDA prohibits those and some more that are known to cause problems. Either because they are so-called control characters with a special potentially dangerous meaning on the storage systems or because they are known to interfere with the web interfacing and presentation. We are continuously evaluating the need for allowing more exotic characters but always with focus on not breaking existing interfaces and backends. Feel free to contact us about the possibility of allowing any additional characters that you may miss.


How do I install and run software XYZ in Jupyter?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We\'ve added Jupyter integration in ERDA, so that you can run interactive data analysis sessions e.g. in a Python or R environment with direct access to all your ERDA data. The built-in Jupyter Terminal extends the options with a multitude of command line tools.
A number of software packages are already available in the different Jupyter instances, but sometimes you may still want to run additional software there. Please refer to the section about Jupyter Notebook Customization in the user guide for details.
We are working on a solution whith greater DIY customization of the notebook images, but for now please contact us at our support email if you have additional permanent software wishes. Then we will see if they can be fulfilled - but we can\'t give any promises.


Can I run MATLAB, FIJI/ImageJ, Java or similar on ERDA?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes and no. Typically a number of license and technical limitations prevent similar integration of MATLAB, etc. to what we do with Jupyter. However, you can use ERDA as a network drive, in line with the corresponding intro, and in that way run whatever software installed at your computer on your ERDA data. Combined with a fast network connection that can work well.
For non-graphical MATLAB scripts in particular there is also the option to compile the code into a simple binary, that can run in the Jupyter Terminal using just the MATLAB Compiler Runtime (MCR) - without the strict license restrictions.
Unfortunately we can't offer detailed support on that part, but point to the official vendor documentation and a `simple example <https://support.opensciencegrid.org/support/solutions/articles/5000660751-basics-of-compiled-matlab-applications-hello-world-example>`.


I forgot my password, can I recover or change it?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WIP


Web login suddenly says "No such user (xyz123\@ku.dk)"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WIP


Why do I get "Account disabled or expired" emails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WIP


What is the cause of "read: connection reset by peer" errors e.g. for SFTP/SSHFS?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WIP


Can I get an ERDA account without a UCPH account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WIP


Can I keep my ERDA account after my UCPH employment/studies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WIP
