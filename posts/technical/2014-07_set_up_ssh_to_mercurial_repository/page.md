
## Set up SSH to Mercurial repository ##

Generate Key in your PC --> Install Key in your Cloud Account.

If you came to this page because you don't have SSH set up, then you have been using the secure hypertext transfer protocol (HTTPS) to communicate between your local system and Bitbucket Cloud. When you use HTTPS, you authenticate (supply a username and password) each time you take an action that requires a connection with Bitbucket. Who wants to do that? This page shows you how to use secure shell (SSH) to communicate with the Bitbucket server and avoid having to manually type a password all the time.

To use SSH with Bitbucket, you create an SSH identity containing a private key (on your local computer) and a public key (uploaded to Bitbucket) which create a key pair. After setting up SSH between your local system and Bitbucket, your system uses the key pair to authenticate you automatically to anything to which the associated account has access.

There are a few important concepts you need when working with SSH identities and Bitbucket.

- You cannot reuse an identity's public key across accounts. You must create SSH identities for each individual Bitbucket account.

- You can associate multiple identities with a Bitbucket account.

- RSA (R. Rivest, A. Shamir, L. Adleman are the originators) and digital signature algorithm (DSA) are key encryption algorithms. Bitbucket supports both types of algorithms. You should create identities using whichever encryption method is most comfortable and available to you.

The following sections cover how to set up SSH for Mercurial.

## Set up SSH for Linux ##

### Step 1. Ensure you have an SSH client installed ###

SSH is most likely included with your version of Linux. To make sure, do the following to verify your installation:

1.From your terminal window, enter the following command, which identifies the version of SSH you have installed. If SSH is installed, you see something similar to the following:

```
$ ssh -v 
OpenSSH_5.6p1, OpenSSL 0.9.8r 8 Feb 2011
usage: ssh [-1246AaCfgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
           [-D [bind_address:]port] [-e escape_char] [-F configfile]
           [-I pkcs11] [-i identity_file]
           [-L [bind_address:]port:host:hostport]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-R [bind_address:]port:host:hostport] [-S ctl_path]
           [-W host:port] [-w local_tun[:remote_tun]]
           [user@]hostname [command]
```

2.List the contents of your ~/.ssh directory. If you don't have an .ssh directory, don't worry, you'll create it the next section. If you have a .ssh directory or you may see something like this:

```
$ ls -a ~/.ssh 
known_hosts
```

If you have defined a default identity, you'll see the two id_* files:

```
$ ls -a ~/.ssh 
.        ..        id_rsa        id_rsa.pub    known_hosts
```

In this case, the default identity used RSA encryption (id_rsa.pub). If you want to use an existing default identity for your account, skip the next section and go to the ```Step 3. Start the ssh-agent and load your keys```.

### Step 2. Set up your default identity ###

By default, the system adds keys for all identities to the /home/YOURNAME/.ssh directory on Linux. This procedure creates a default identity. If you have a default identity and you want to use it for your account, skip this step and go to ```Step 3.``` Start the ssh-agent and load your keys. If you have an existing default identity but you forgot the passphrase, you can also use this procedure to overwrite your default identity and create a fresh one.

Use the following procedure to create a new default identity:

1.Open a terminal in your local system.

2.Enter ssh-keygen at the command line.

The command prompts you for a file where you want to save the key. If the .ssh directory doesn't exist, the system creates one for you.

```
$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/emmap1/.ssh/id_rsa):
```

3.Press the Enter or Return key to accept the default location.

4.Enter and re-enter a passphrase when prompted.
Unless you need a key for a process such as script, you should always provide a passphrase. The command creates your default identity with its public and private keys. The whole interaction will look similar to the following:

```
$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/emmap1/.ssh/id_rsa):
Created directory '/Users/emmap1/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/emmap1/.ssh/id_rsa.
Your public key has been saved in /Users/emmpa1/.ssh/id_rsa.pub.
The key fingerprint is:
4c:80:61:2c:00:3f:9d:dc:08:41:2e:c0:cf:b9:17:69 emmpa1@myhost.local
The key's randomart image is:
+--[ RSA 2048]----+
|*o+ooo.          |
|.+.=o+ .         |
|. *.* o .        |
| . = E o         |
|    o . S        |
|   . .           |
|    .            |
|                 |
|                 |
+-----------------+
```

5.List the contents of ~/.ssh to view the key files.

```
$ ls -a ~/.ssh
.        ..        id_rsa        id_rsa.pub    known_hosts
```

### Step 3. Start the ssh-agent and load your keys ###

If you are running a Linux operating system, do the following:

1.Open a terminal window and enter the  ps -e | grep [s]sh-agent  command to see if the agent is running.

```
$ ps -e | grep [s]sh-agent 
 9060 ?? 0:00.28 /usr/bin/ssh-agent -l
```

2.If the agent isn't running, start it manually with the following command:

```
$ ssh-agent /bin/bash
```

3.Load your new identity into the ssh-agent  management program using the  ssh-add  command.

```
$ ssh-add ~/.ssh/id_rsa 
Enter passphrase for /Users/emmap1/.ssh/id_rsa:
Identity added: /Users/emmap1/.ssh/id_rsa (/Users/emmpa1/.ssh/id_rsa)
```

4.Use the  ssh-add  command to list the keys that the agent is managing.

```
$ ssh-add -l 
2048 7a:9c:b2:9c:8e:4e:f4:af:de:70:77:b9:52:fd:44:97  /Users/manthony/.ssh/id_rsa (RSA)
```

### Step 4. Enable SSH compression for Mercurial ###

When sending or retrieving data using SSH, Git does compression for you. Mercurial does not automatically do compression. You should enable SSH compression as it can speed up things drastically, in some cases. To enable compression for Mercurial, do the following:

1.Open a terminal window.

2.Edit the Mercurial global configuration file (~/.hgrc). If this file is empty (doesn't exist), fill with the next lines.

```
$ nano ~/.hgrc
```

3.Add the following line to the UI section:

```
ssh = ssh -C
```

When you are done the file should look similar to the following:

```
[ui]
# Name data to appear in commits
username = Emma <emmap1@atlassian.com>
ssh = ssh -C
```

Save and close the file in nano with ctrl+x, yes and enter.

### Step 5. Install the public key on your Bitbucket account ###

1.From Bitbucket Cloud, choose ```avatar > Bitbucket settings``` from the application menu.
The system displays the ```Account settings``` page.

2.Click ```SSH keys```. The ```SSH Keys``` page displays. If you have any existing keys, those appear on this page.

3.Back in your terminal window, copy the contents of your public key file. For example, in Linux you can cat the contents.

```
$ cat ~/.ssh/id_rsa.pub
```

4.Back in your browser, enter a ```Label``` for your new key, for example, Default public key.

5.Paste the copied public key into the SSH ```Key``` field.

6.Press ```Add key```. The system adds the key to your account. Bitbucket sends you an email to confirm addition of the key.

### Step 6. Change your repo from HTTPS to the SSH protocol ###

The URL you use for a repository depends on which protocol you are using, HTTPS and SSH. The repository ```Overview``` page has a quick way for you to see the one for your myquotefork repository. On the repository's ```Overview``` page look for the ```Clone this repository``` line.

Go to your local system and navigate to your myquotefork repository (the only Mercurial repository you've worked with so far). Follow these instructions:	

1.Enter to your current repo and view your current repo configuration. You should see in /.hg/hgrc something similar to the following:

```
[paths]
default = https://bitbucket.org/newuserme/myquotefork
```

2.Change the default value to use the SSH format for that repository. When you are done you should see something similar to the following:

```
[paths]
default = ssh://hg@bitbucket.org/newuserme/myquotefork
```

Save and close the configuration file.

### Step 7. Make a change under the new protocol ###

Now, you can do pull and push without write a password.

Don't worry if appear the next message, write yes and enter to continue:

```
The authenticity of host 'host' can't be established.
RSA key fingerprint is RSAkey.
Are you sure you want to continue connecting (yes/no)?
```

That's all!!.

## Set up SSH for Windows ##

### Step 1. Install TortoiseHg ###

TortoiseHg is the Microsoft Windows version of Mercurial. If you haven't installed Mercurial yet, installing TortoiseHg automatically gives you Mercurial. If you have installed Mercurial, TortoiseHg allows you to set up SSH and give you another option in place of the command line.
After you download the [http://tortoisehg.bitbucket.org/download/index.html](all-in-one installer (MSI version))! and install it, you may need to restart your system for the installation to take effect.


### Step 2. Install PuTTYgen and configure PuTTY ###

PuTTYgen is a free RSA and DSA key generation tool that you also use when setting up SSH.

1.Download the proper version [http://www.putty.org/](http://www.putty.org/)! of the utilities for your system – each one is a single executable file.

2.Start Putty. The ```PuTTy Configuration``` dialog displays. Use this dialog to configure your PuTTy sessions.

3.Under the ```Session``` node, select ```Default Settings``` and press ```Load```. This allows you to edit the Default Settings session configuration.

4.Under the ```Connection``` node, click ```SSH```. The ```Options controlling SSH connections``` display.

5.Check ```Enable compression```. This option can improve performance of a low-band connection.

6.Click the ```Session``` node, select ```Default Settings``` and press ```Save```.

7.Click the Close button (red x).

### Step 3. Create your default identity ###

The following procedure creates a default identity with PuttyGen. If you have an existing private key, you can skip this step and go onto  Enable SSH compression for Mercurial.

1.Locate the puttygen.exe executable in your system and double click the icon to start it. If you are following along with this tutorial, you installed PuTTYgen in C:\Program Files\TortoiseHG. The system opens the ```PuTTY Key Generator dialog```.

2.Complete

3.Press Generate. Following the instructions to generate some randomness. When the generation completes, the system displays the public key and a number of other fields.

4.Enter and confirm a key passphrase.

5.Press Save private key. The system prompts you for a location to save the file and a file name. By convention, store your key files in a folder called C:\Users\yourname\ .ssh\ and give it a .ppk extension. (create .ssh folder typing in cmd: ```cd C:\Users\yourname\``` and ```mkdir .ssh```)

6.Go ahead and close PuTTYgen.

### Step 4. Enable SSH compression for Mercurial ###

When sending or retrieving data using SSH, Git does compression for you. Mercurial does not automatically do compression.  If you are using Mercurial, you should enable SSH compression as it can speed up things drastically, in some cases. To enable compression for Mercurial, do the following:

1.Start the TortoiseHg Workbench.

2.Select ```File > Settings```.

3.Make sure you have the global settings tab selected.

4.Press ```Edit File```.

5.Add the following line to the UI section:

```
ssh = "TortoisePlink.exe" -ssh -2 -batch -C
```

When you are done the file should look similar to the following:

```
[ui] 
# Name data to appear in commits
username = Emma Paris <emmap1@atlassian.com>
ssh = "C:\Program Files\TortoiseHg\TortoisePlink.exe" -ssh -2 -batch -C
```

6.Press ```Save``` to store your settings and close the file.

7.Press ```OK``` to close the settings dialog.

### Step 5. Start Pageant and install your private key ###

TortoiseHG comes with Pageant which is an SSH authentication agent. You load your keys into Pageant and it automatically authenticates you so you don't need to enter your passphrase. Do the following to load your keys:

1.Start Pageant by double clicking its icon. By default, TortoiseHG installs the Pageant in the C:\Program Files\TortoiseHG folder. When it is running, Pageant appears in your system tray (the icon is a computer with a hat).

2.Double-click the Pageant icon to launch the ```Pageant Key List``` dialog.

3.Click the ```Add Key``` button. The system displays the ```Select Private Key File``` dialog.

4.Navigate to and open the default key you created previously.

5.Enter the passphrase when prompted:

6.Press ```OK```. Pageant shows your key in the running list.

7.Press ```Close``` to close the dialog. Pageant continues to run on your system.

Additional:

With the last steps Pageant close every time you shutdown your PC. So, you should to open Pageant and add the key each time you want to use your Key.

To start Pageant with a shortcut that include your Key, do: Close pageant of your System Tray. Then create a shortcut of pagent.exe and save it in the Desktop. Make sure the shortcut’s target contains the path to your key as well: Right click in the shorcut and into Properties under Target:  "C:\Program Files (x86)\PuTTY\pageant.exe" "C:\Users\Dennis\.ssh\ssh-key.ppk". Run Pagent and it should go to your System Tray.

To start Pageant automatically each time yu start your PC (but each time you restart you PC you should to type your Passphrase), do: Close pageant of your System Tray. Then create a shortcut of pagent.exe and save it in the Startup folder (Click the Start button of the Start button , click All Programs, right-click the Startup folder, and then click Open). Make sure the shortcut’s target contains the path to your key as well: Right click in the shorcut and into Properties under Target:  "C:\Program Files (x86)\PuTTY\pageant.exe" "C:\Users\Dennis\.ssh\ssh-key.ppk". Run Pagent and it should go to your System Tray.

### Step 6. Install the public key on your Bitbucket account ###

1.Open a browser and log in to Bitbucket.

2.Choose ```avatar > Account``` from the menu bar. The system displays the ```Account settings``` page.

3.Click ```SSH keys```. The ```SSH Keys``` page displays. It shows a list of any existing keys. Then, below that, a dialog for labeling and entering a new key.

4.Switch to your local desktop and start the PuTTYgen program.

5.Press ```Load```.

6.Navigate to and open your default private key.

7.Enter your passphrase when prompted and press OK. The system displays your public key.

8.Select and copy the contents of the ```Public key for pasting into OpenSSH authorized_keys file``` field.

9.Back in your browser, enter a ```Label``` for your new key, for example, Default public key.

10.Paste the copied public key into the ```SSH Key``` field.

11.Press ```Add key```. The system adds the key and it appears in the ```SSH Keys``` listing.

12.Close PuTTYgen.


### Step 7. Configure your local repository to use the SSH protocol ###

The URL you use for a repository depends on which protocol you are using, HTTPS and SSH. The Bitbucket repository ```Overview``` page has a quick way for you to see the one for your myquotefork repository. On the repository's ```Overview``` page look for the ```Clone this repository``` line.

Go to your local system and navigate to your myquotefork repository (the only Mercurial repository you've worked with so far). These instructions assume you have added the repository to the TortoiseHG Workbench.	

1.Enter to your current repo and view your current repo configuration. You should see in /.hg/hgrc something similar to the following:

```
[paths]
default = https://bitbucket.org/newuserme/myquotefork
```

2.Change the default value to use the SSH format for that repository. When you are done you should see something similar to the following:

```
[paths]
default = ssh://hg@bitbucket.org/newuserme/myquotefork
```

Save and close the configuration file.

### Step 8. Make a change under the new protocol ###

Now, you can do pull and push without write a password.

### Basics Git Comands ###

Pull -> Addremove -> Commit -> Push.

Enter the terminal to Linux or Windows console.

Before all we must place ourselves in the local repository folder with ```cd``` command. Example:

```
$ cd /home/dennis/Documents/Repositories/documentation
```

Be careful that all file names do not have spaces, otherwise you will have problems to add or delete files to the repository.

#### Pull ####

It’s an easy way to synchronize your local repository with upstream changes.

```
$ hg pull
```

Then:

```
$ hg update
```

#### Addremove ####

To add deleted, modified new ones files to the index:

```
$ hg addremove
```

Warning: A file can be added to the folder in the local repository but does not belong to the local repository.

Warning: A file can be deleted from the folder on the local repository but not removed from the local repository.

#### Commit ####

Store the current contents of the index in a new commit along in the remote repository with a log message from the user describing the changes.

```
$ hg commit -m "first commit"
```

#### Push ####

Pushing is how you transfer commits from your local repository to a remote repository.

```
$ hg push
```

### Resources ###

- [https://confluence.atlassian.com/bitbucket/set-up-ssh-for-mercurial-728138122.html](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-mercurial-728138122.html)!.


