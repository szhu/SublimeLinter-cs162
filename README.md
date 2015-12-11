SublimeLinter-cs162
=========================

This linter plugin for SublimeLinter provides an interface to any C compiler output served at http://192.168.162.162:16280.

It is intended to be used with the Pintos VM from UC Berkeley's CS 162 course, so that you can see compile-time errors without needing to run make manually. Here's a screenshot:

<img width="376" src="https://cloud.githubusercontent.com/assets/1570168/11751469/84a2160c-9fee-11e5-9028-d79342d34187.png">


To use this, you need to follow these steps:


## Installing

Short version: this plugin has the following dependency tree:

 - **SublimeLinter-cs162**
     - requires **Package Decontrol** to install
     - requires **SublimeLinter3** to run
         - requires **Package Control** to install
         - requires **Sublime Text 3** to run

Long version:

1. Make sure you are on **Sublime Text 3** (for SublimeLinter3 to work).  
   If not, [download it here](<http://www.sublimetext.com/3>).

2. Make sure you have **Package Control** installed (for installing SublimeLinter3).  
   If not, follow [the instructions here](<https://packagecontrol.io/installation>) to install.

3. Make sure you have **SublimeLinter3** installed (for this plugin to work).  
   If not, go to **Tools** > **Command Palette…**, select **Package Control: Install Package**, then select **SublimeLinter**.

4. Make sure you have **Package Decontrol** installed (for installing this plugin).  
   If not, follow [the instructions here](<https://github.com/jfromaniello/Sublime-Package-Decontrol>) to install.

5. Make sure you have this plugin installed!  
   If not, go to **Tools** > **Command Palette…**, select **Package Decontrol: Install from GitHub**, then enter **szhu/SublimeLinter-cs162**.


## Using

This linter repeatedly tries to fetch http://192.168.162.162:16280 and tries to parse it as GCC/Clang error output. To make this work, one last step is required. Inside your VM, you need to enter

```shell
curl -fsL http://git.io/v0Yzx | python
```

and you need to keep this running as long as you want the linter to work. Ctrl-C to stop this.

Alternatives:

- Don't want to use Python? Here's an alternative that works almost perfectly… because it doesn't support concurrent requests, the linter will show your errors only on second save.  
  `bash -c 'while true; do make -j 2>&1 | nc -l 16280 > /dev/null; done'`
- The script at http://git.io/v0Yzx takes command line arguments. The syntax is:  
  `curl -fsL http://git.io/v0Yzx | python - 'COMMAND TO RUN' PORT`  
  where all three arguments are optional but must appear in that order.


## Credit 

Original idea by [@szhu](<http://github.com/szhu>).

Plugin structure and regex from [nirm03/SublimeLinter-clang](<https://github.com/nirm03/SublimeLinter-clang>).
