# CSCI112-Course-Pack

## Cloning the Repository

We will be using a premade script for this exercise. This script will automaticaly load data that I have generated on my personal workstation. You will use this data to answer the short quiz in Canvas.

To clone the repository from gitlab:

1. Open your AWS Environment.
2. Connect to your Application Server through ssh.
3. Once logged in, you should be in `/home/ubuntu`. You can use `pwd` to check. If you are not in that directory, you can type in `cd /home/ubuntu`.
4. Type in `git clone https://github.com/mrugeria/CSCI112-Course-Pack.git` to clone our repository into `/home/ubuntu`.
5. When you type `ls`, you should see the git repository named `CSCI112-Course-Pack`. You can now `cd` into that to go inside the repo.

## Installing Pymongo

1. Install venv to create a virtual environment

```
sudo apt install python3-venv
```

2. Go to your project path (in this case the repo path where you cloned it), then create the virtual environment.

```
cd <path to repo>/CSCI112-CoursePack

python3 -m venv .venv
```

3. Activate the virtual environment so the OS knows that you are running python commands using your virual environment, not the system level python installation.

```
source .venv/bin/activate
```

4. Install pymongo inside the venv.

```
pip install <package_name>
```

**NOTE: venv needs to be activated (step #3 above) everytime you access your project or work on a different project. You will know if venv is activated if there is a `().venv)` prefix on the terminal.**

## Tools

You should have the following tools open in your workstation:

1. EC2 server already opened through ssh (I recommend the console terminal since it rarely disconnects on its own and there are no firewall limitations when connecting using the univ wifi) - This will be used to pull changes from our remote repository
2. VSCode, with your repo opened locally - This will be used to make changes to our code
3. Local terminal, location should be inside the local repository in your workstation - This will be used to push changes to our remote git repo
4. MongoDB Compass connected to your EC2 server that houses the MongoDB Database - This will be used to validate the changes made when we run our code

## Running Your Code

To run your code, you need to follow these instructions:

1. Make changes to your code in VSCode locally.
2. Go into your MongoDB Server in AWS EC2, then create a new python file.
3. Copy and paste your code from VSCode to the new python file.
4. Run the python file.