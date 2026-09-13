# CSCI112-Course-Pack

## Cloning the Repository

We will be using a premade script for this exercise. This script will automaticaly load data that I have generated on my personal workstation. You will use this data to answer the short quiz in Canvas.

To clone the repository from gitlab:

1. Open your AWS Environment.
2. Connect to your Application Server through ssh.
3. Once logged in, you should be in `/home/ubuntu`. You can use `pwd` to check. If you are not in that directory, you can type in `cd /home/ubuntu`.
4. Type in `git clone https://github.com/mrugeria/CSCI112-Course-Pack.git` to clone our repository into `/home/ubuntu`.
5. When you type `ls`, you should see the git repository named `CSCI112-Course-Pack`. You can now `cd` into that to go inside the repo.

## Tools

You should have the following tools open in your workstation:

1. EC2 server already opened through ssh (I recommend the console terminal since it rarely disconnects on its own and there are no firewall limitations when connecting using the univ wifi) - This will be used to pull changes from our remote repository
2. VSCode, with your repo opened locally - This will be used to make changes to our code
3. MongoDB Compass connected to your EC2 server that houses the MongoDB Database - This will be used to validate the changes made when we run our code

> [!NOTE]
> For instructions on setting up your tools and environment, go to lecture_supplements > 00-mongodb-server-setup and read the instructions in the README.md file.