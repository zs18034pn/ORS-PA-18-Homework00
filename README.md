# Homework00


The main objective of this homework is to properly setup development environment for Python 3.x on your personal computer.
In order to successfully complete homework please follow steps given below.

---

#### Step 1. Install Python 3  (Windows Tutorial)

 * Download [Python 3](https://www.python.org/downloads/)

 * Run Installation Wizard

 * Please make sure that you add Python to `PATH` (check option at the bottom).

 ![alt text](https://docs.python.org/3/_images/win_installer.png "Add Python to PATH")

 * Start `Command Prompt` and run `python3` to enter Python interactive console. [1]

 * If Python 3 console appears you have successfully installed Python.

 
 [1] If you receive an error like `'python3' is not recognized as an internal or external command, operable program or batch file. ` or `bash: python3: command not found` you need to add path to Python installation to your system variable PATH.

 If you have already Python installed but forgot to check option `Add to PATH` on install screen, you can uninstall Python and install it again or follow this [tutorial](https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path) in order to fix your issue. Please note that in this tutorial `Python 2.4` is used instead of `Python 3.6` so you need to adjust the paths to match your setup.

 #### Step 2. Install Git  (Windows Tutorial)

  * Download [Git](https://git-scm.com/downloads)

  * Run Installation Wizard

  * If you do not have GitHub account [create one](https://github.com/join) with your student email.

  * Verify your email address once you join GitHub.

  * Login to GitHub.

  * Run `Git Bash`.

  * Generate new [SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#generating-a-new-ssh-key)

  * Run `cat ~/.ssh/id_rsa.pub` in Git Bash in order to get public key (Select and copy your key).

  * [Add SSH](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) key on Github.

  * Run  `git config --global user.name "Your Name"` - please use your own name.

  * Run `git config --global user.email johndoe@example.com` - please use your student email.

 #### Step 3. Install PyCharm Community Version

  * Download [PyCharm Community Version](https://www.jetbrains.com/pycharm/download/)

  * Run Installation Wizard.

  * Create new test project and select Python 3 as interpreter.

 #### Step 4. Fork & Clone this Github project

  * [Fork](https://help.github.com/articles/fork-a-repo/#fork-an-example-repository) this project.

  * Go to [homepage](https://github.com).

  * Open `Homework00` project (right side panel).

  * [Clone repository](https://help.github.com/articles/cloning-a-repository/) on your computer. Remeber the project folder location.

  * Open PyCharm and [create project](https://www.jetbrains.com/help/pycharm/importing-project-from-existing-source-code.html) from existing source code.

  * Open `hello.py` script in PyCharm (left side panel).

  * Run `hello.py` (Right click + choose `Run`).

  

  If you see message `Hello World!` in PyCharm `Run` console you have completed this homework successfully.
  
  ---
  
  If you need help with your homework please contact teaching assistant.
