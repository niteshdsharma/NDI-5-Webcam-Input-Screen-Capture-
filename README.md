# NDI-5-Webcam-Input-Screen-Capture-
Network Device Interface is a royalty-free software specification developed by NewTek to enable video-compatible products to communicate, deliver, and receive high-definition video over a computer.

## User Guide  to WebInput
The binary  file accepts switches , if  you don't provide any switches it will load the program with  default values, it is assumed that you have installed ndi to the default location on your windows system.

```
>webinput 
```
it will  launch the  webinput with  default settings

#### Selecting the Video Source 

To select a Source you need to type the name of  the ndi stream using parenthesis.
```
>webinput -src "type the name of source"
```
example : if you want to select a stream "realtek" , you can write
```
>webinput -src "realtek"
```

if your stream is  nested( as a sub option) , suppose it is  like  desktop2435->myaudio , you simply need to use  parenthesis for child.


```
>webinput -src "desktop2435 (myaudio)"
```
if there  is  further  nesting ,desktop2435->contact->myaudio , you can use following 

```
>webinput -src "desktop2435 ( contact (myaudio))"
```
Must Note : the single space before '(' is compulsory.

#### Adjusting Video Quality
we can use switch '-v' with a value ,as shown in the example.
```
>webinput -v 1
```
it will load all the default values but  video quality will be 1080.
more options:
0 for  automatic video |
1 for  1080|
2 for  720|
3 for  480|
examples :
```
>webinput -v 3
```
the above  will execute webinput with  video quality as 480

#### adjusting audio level
To adjust audio level , use  '-al' switch  
0 - automatic audio level
1 for +20db|
2 for +10db|
3 for +6db(EBU)|
4 for +0db(SMPTE)|
5 for -inf db(mute)|
example:
```
>webinput -al 3
```

#### adjusting audio channels

to adjust the channel use  the '-ac' switch

0 for all channels|
1 for audio channel 1,2|
2 for audio  channel 3,4|
3 for audio channel 5,6|
4 for audio  channel 7,8|

example :
```
> webinput -ac 3
```
it will set the audio channel to  5,6


#### using combination of switches 
 yes, we can use combination of switches  to get the desired settings,
 example 
 ```
 >webinput -v 2 -ac 3 -al 2
 ```
 the above code will set the  video quality to  720 and  audio channel to 5,6 and
 audio level to +10db
 
 
 ## Guide to Use  ScreenCapture.exe
### Setting FrameRate
You  can use  values  from 0-to-6 to select the desired framerate.
```
>screencapture -fr 2
```
the above command will run the screencapture with framerate as third option  59.94(NTSC).
### Setting Kvm
we  can also enable or disable use of KVM by using switch

```
> screencapture -kvm 0 
```
zero to disable and 1 to enable the  kvm option.
### setting  roi option( region of interest )
just like kvm option we can select or  unselect the  option for  roi.
```
>screencapture -roi 1
```
use zero to disable it and 1 to enable it.
### Configure region of Interest
you can specify the region of interest , the region which will be shared. The  -config switch is used for this purpose.
Syntax : >screencapture X on screen,Y on screen,Width,Height , it will display the region with (x,y) coordinate as top left and also with specified width and height.
example :
```
>screencapture -config 500,200,500,100
```
Note: try smaller values for  Y and  height. 

it will select the  screen coordinate (x,y) (500,200) and  width of box as 500 and  height of  box as 100.

### Setting mouse display
we can show or hide  mouse by using following switch
```
>screencapture -mouse  0
```
use  zero to disable it and 1  to enable it.

### Setting webcam video
we can select webcam video by specifiying the name, if  only name is provided the video settings will be auto detect.
```
>screencapture -wvideo "HP Truevision HD"
```


### Providing settings for webcam video
it is recommended to provide videosettings when you have selected a webcam video source, the  following switch can help you
```
>screencapture -wvideo "HP Truevision HD" -wvideosetting "1280x720 30.00Hz"

```


### Setting Webcam Audio
we can also select the  webcam audio as follows
```
>screencapture -waudio "System Audio"
```

### Setting Audio

This is Audio Settings which as not part of webcam , it is available directly on the menu option.
```
>screencapture -as "System Audio"

```

### Note : Combination of  the above Switches is allowed throughout.




 
 
 
 
 
 
 
 
 