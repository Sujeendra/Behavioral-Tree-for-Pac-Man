Installation in Unix
------------
1) Install Dependencies:

`sudo apt-get install build-essential libgl1-mesa-dev python3-tk qtdeclarative5-dev`

2) Download the repository:

`git clone https://github.com/Sujeendra/Behavioral-Tree-for-Pac-Man.git`

3) Build the Software:

Run in a terminal the following commands:
`cd pacman` <br/>
`delete the build folder before building`
`sudo rm -r build` <br/>
`mkdir build` <br/>
`cd build` <br/>
`cmake ..` <br/>
`make`

Run in Unix
------------

Run in a terminal the following commands:
`you should be in the build folder to execute this`
`./behavior_tree_editor`







Verify your installation
------------
-In the BT editor: File->Load  <br/>
-Browse in the folder pacman (the one you retrieved in step 2)  <br/>
-Select the file Custom.xml  <br/>
-A BT should appear in the editor, as in the picture below: <br/>

![alt tag](Screenwindows.png)





-Press the Play <img src="play.png" width="15" height="15"> icon. <br/>










