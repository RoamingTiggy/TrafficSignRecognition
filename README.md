# TrafficSignRecognition
Part 1: Raspbian
***The following was executed on a Raspberry Pi, running the Raspbian OS and a usb Camera.***
TrafficSignRecognition Python Code. Using OpenCV for image procesing and Pyttsx as a detection announcer.

Raspbian 

1) Download the required versions and associated libraries.  
    $sudo apt-get install fswebcam   
    $sudo apt-get install python2.7.12  
    $sudo apt-get install python-pip  
    $pip install opencv-python  
    $sudo pip install numpy  
    $sudo pip install pytssx  
    
2) Verify the version of python and openCV with these commands:  
  Python: $ python --version  
  OpenCV: $ python  
        >>> import cv2  
        >>> cv2.__version__  

3) Place the XML files in the same folder(directory) with the .py file

4) Run the .py code

5) Success! Hold "esc" key to terminate the program.

Part 2: Windows10

1) Download the required versions and associated libraries.  
	  Python 2.7.13 https://www.python.org/downloads/release/python-2713/  
    Python pip package installer https://packaging.python.org/tutorials/installing-packages/  
    
2) Run Windows PowerShell terminal.  
    install pip     $python get-pip.py  
    install numpy   $python -m pip install numpy  
    install pyttsx  $python -m pip install pyttsx  
    install pywin32 $python -m pip install pywin32  Python Wrapper for Windows *required*  
   
3) Download, setup and verify OpenCV  

    OpenCV 3.4.2  https://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.4.2/opencv-3.4.2-vc14_vc15.exe/download
    download and extract the contents of the zip file  
    
You must then copy the file from this directory \opencv\build\python\2.7\x64 named “cv2.pyd” and paste it within your python directory        \Python27\Lib\site-packages. This will make python recognize the use of OpenCV. 
Open the Python terminal and type the following codes to verify that OpenCV works.  
        >>> import cv2  
        >>> cv2.__version__   

4)Place the .py along with the XML files in the same folder(directory)  

5)Run PowerShell within that directory and type the $python SignDetection.py  

6)Success!  

    
    
    
