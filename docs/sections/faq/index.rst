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
A number of users have asked about the possibility of assigning a Digital Object Identifier (DOI) to their published ERDA archives. It is getting more common to use such DOIs in research papers in line with the open-access and `Open science <https://en.wikipedia.org/wiki/Open_science>` spirit. UCPH has a license to mint DOIs through `DataCite <https://www.datacite.org/>`_ and University IT has developed a service to help do that, which we've integrated with ERDA. In practice you create your ERDA freeze archive as usual and select yes for Make Dataset Publicly Available. When satisfied with the archive contents you click **Finalize archive** to permanently freeze it. Afterwards you can use the **Request archive DOI** button on the View archive details page to proceed with the UCPH DOI registration form. At KUNet you can find a `more elaborate DOI introduction <https://kunet.ku.dk/work-areas/research/data/data-sharing/data-doi/Pages/default.aspx>`_ including a complete visual walk-through of the process to create an archive and assign a DOI. We guarantee the availability of ERDA archives for at least(!) 10 years and the same applies for the UCPH-minted DOIs. 


How are Workgroups managed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Workgroups can be created by academic staff (VIP) as well as technical/administrative staff (TAP) and the creator of a workgroup automatically becomes owner. All user management is left to the owner(s) without interaction from the ERDA system administrators. Co-owners and members can be added either directly using the *Swedish numberplate* or email alias of the user, or indirectly if the user requests owner-/membership on the Workgroups page, and the owner(s) follow the instructions then sent on email about adding the user with the full user ID format. We recommend the intro guide on Workgroups for further details.


Can I have a shared or separate account for our project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, we **cannot** allow such accounts or account aliasing, mainly due to rules and regulations. In case of suspected or alleged abuse we need to be able to uniquely identify who did what and when, and all kinds of anonymous or shared accounts would prevent that. Please refer to the `UCPH information security policy <https://informationssikkerhed.ku.dk/english/is-policy/>`_ for further details about identity and traceability requirements.
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
Unfortunately we can't offer detailed support on that part, but point to the official vendor documentation and a `simple example <https://support.opensciencegrid.org/support/solutions/articles/5000660751-basics-of-compiled-matlab-applications-hello-world-example>`_.


I forgot my password, can I recover or change it?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For security reasons we generally avoid storing passwords in our systems and only save a one-way derived hash value. Therefore we **cannot** recover passwords, but we do allow you to change it.
If you are an employee or student at KU/UCPH you typically log in to ERDA web through the UCPH OpenID authentication service. It is linked to the central UCPH user database and therefore employs your usual UCPH credentials from e.g. KU Mail and KU Net (usernames are on the form *abc123*). If you forgot your KU/UCPH password or e.g. it expired you need to go through UCPH password change procedures or get in touch with `UCPH IT Support <https://it.ku.dk/english/contact/>`_.
If you are an external user on ERDA you can always use the External user *sign up* button again to renew access and/or change your main ERDA password. Just fill the sign up form as usual including your particular ID fields, the mandatory name and email of your UCPH contact and perhaps a note that you want to change password in the Comment field.
For password changes we recommend the *Forgot your password?* link on the login page. Just enter your registered ERDA account email address there to receive a reset password link on email and use it to pick a new password.
The other ERDA services like SFTP, WebDAVS, FTPS and Seafile rely on local login credentials and you can change them yourself on your ERDA Setup page and on ERDA Seafile respectively. 


Web login suddenly says "No such user (xyz123\@ku.dk)"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already signed up to ERDA and had access but you begin receiving such errors it is likely that you hit an occasional problem we experience when UCPH IT changes primary email address of users in their central user database. This typically only happens in relation to significant employment status changes. ERDA just relies on the UCPH OpenID service for sign up and log in, so the change means that your existing account with e.g. xyz123\@alumni.ku.dk is no longer recognized to belong to the ID, which UCPH OpenID tells us you now have. Rest assured that your ERDA account remains intact, and usually we can fix the problem by assigning the new primary email alias to it. We just need you to contact us as described below to do so. 


Why do I get "Account disabled or expired" emails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since December 2020 we have enforced automatic WebDAVS/SFTP/FTPS access expiry for all users in order to reduce the risk of no longer active accounts being abused/hacked that way. We have enforced automatic ERDA account expiry for longer for web access. However, UCPH users automatically get their account renewed when successfully logging into the web pages through the UCPH OpenID service, while external users must explicitly renew their account access annually using the sign up form on the front page. With account expiry extended to cover the efficient I/O services any configured access to our WebDAVS, SFTP or FTPS services will also automatically expire when accounts do. Attempts to log in on those services after general account expiry will fail and trigger an email warning that the account is expired. In practice it has limited consequences for external users, who already go through the annual renewal process. UCPH users solely or mainly using ERDA as network drive or through a WebDAVS/SFTP/FTPS client, will have to get used to regularly renew account access to keep using said I/O services. This can either be done for a whole year at a time by repeating 'sign up' on the front page or for 30 days by a simple web log in. Thus, users solely or regularly using the web access don't need to worry or do anything new. Those who enabled 2-Factor authentication for all ERDA account access can also just continue with their usual web login before their I/O service logins. 


What is the cause of "read: connection reset by peer" errors e.g. for SFTP/SSHFS?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

That error message is a common symptom of a firewall ban at ERDA. We experience regular password guessing attacks and rely on a self-defense system to monitor login attempts and act on apparent cracking or abuse attempts. In practice it automatically bans IP addresses temporarily when we receive too many failed login attempts over a certain period of time. The ban period depends on the login pattern and simple repeated password failures usually only result in a 15 minute ban. More aggressive scans and failures on the other hand may trigger a 24 hour ban, while the most blatant cracking attempts result in a 24 day ban. For multi-user systems and computers behind a shared gateway these bans unfortunately may result in not only the offender but also several other users or computers getting affected by the ban. In the sense that they are no longer able to reach ERDA until the ban expires or gets manually lifted by the site administrators. Thus, please contact us on ERDA support if you hit this issue and it remains so even after 15 minutes without further login attempts. If you include the public IP address that you connect from (`ip.me <https://ip.me/>`_) it's a significant help to investigate and getting any unnecessary bans lifted without further delay. 


Can I get an ERDA account without a UCPH account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, as long as you need an ERDA account for a course, workshop or project collaboration with one or more employees at UCPH it is possible to get one in line with the Sign Up Intro - even if you don't have a general UCPH account.
Just use the tabs at the top to switch between the different sign up and log in methods. After the ERDA admins receive your account request and your UCPH employed contact has confirmed you as Peer, your account will be created with your non-UCPH login. You will automatically receive a brief intro email explaining how to log in, either with your registered email and chosen password or with your x509 user certificate installed.

.. IMPORTANT::
   Please note that UCPH management requires ALL such users not employed at UCPH to explicitly register their ERDA account with their affiliation to a current employee at UCPH. So please ALWAYS include a reference (name + email) to your contact employed at UCPH in the comment field, when you fill in the OpenID or certificate account request form. 


Can I keep my ERDA account after my UCPH employment/studies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, if you keep collaborating with one or more UCPH employees you can do so in line with the answer above.
Our general username+password access described in the user guide relies on the OpenID login from University IT and they strictly use the main UCPH user database. So only users with an active UCPH account can use that login.
However, we provide two alternative access methods, namely a similar username+password login using our own stand-alone OpenID login service, and another one relying on our x509 `user certificates <https://dk-sid.migrid.org/cgi-sid/reqcert.py>`_ for added security.
You can sign up for a non-UCPH log in method to your ERDA account by opening one of the other tabs above, clicking the sign up button and filling the web form. You just need to make sure to enter values matching your current account in the form, as well as explicitly reference with whom at UCPH you will keep collaborating. Please ask us if in doubt. 
