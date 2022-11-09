## Guide to Use  ScreenCaptureHX.exe

### Setting Quality of  Bandwidth

you can use values starting from zero 
zero for ultra and 1 for  high and 2 for  medium and 3 for low.
```
>screencaptureHX -bandq 2
```
it will set the bandwidth quality to medium.
### Setting Hevc Enabled or Disabled(other)
we can also enable or disable use of hevc by using switch, when you disable it, the
other option H.264 will be selected.
```
> screencaptureHX -hevc 0 
```
zero to disable and 1 to enable the hevc option.

### Setting  the Video Resolution 
video resolution has default (0) , 1440p (1) , 1080p(2) , 720p (3) and 480(4), but there is a known bug with option 480p , it is never selected.

we can set the  video resolution by using similar command as follows:
```
>screencaptureHX -res 2 
```
The above command will set resolution to 1080p.

### Setting FrameRate
You  can use  values  from 0-to-6 to select the desired framerate.
```
>screencaptureHX -fr 2
```
the above command will run the screencapture with framerate as third option  59.94.
### Setting Kvm
we  can also enable or disable use of KVM by using switch
```
> screencaptureHX -kvm 0 
```
zero to disable and 1 to enable the  kvm option.


### Setting mouse check or  not
we can show or hide  mouse by using following switch
```
>screencaptureHX -mouse  0
```
use  zero to disable it and 1  to enable it.

### Audio  Selection
The Audio  Selection  can  be done using  the  -audio switch 
```
>screencaptureHX -audio "Speakers (Realtek High Definition Audio)"
```

##### Note : using  combination of  the above switches is allowed.


## Guide to Use  ScreenCaptureHX.exe

### Setting Quality of  Bandwidth

you can use values starting from zero 
zero for ultra and 1 for  high and 2 for  medium and 3 for low.
```
>screencaptureHX -bandq 2
```
it will set the bandwidth quality to medium.
### Setting Hevc Enabled or Disabled(other)
we can also enable or disable use of hevc by using switch, when you disable it, the
other option H.264 will be selected.
```
> screencaptureHX -hevc 0 
```
zero to disable and 1 to enable the hevc option.

### Setting  the Video Resolution 
video resolution has default (0) , 1440p (1) , 1080p(2) , 720p (3) and 480(4), but there is a known bug with option 480p , it is never selected.

we can set the  video resolution by using similar command as follows:
```
>screencaptureHX -res 2 
```
The above command will set resolution to 1080p.

### Setting FrameRate
You  can use  values  from 0-to-6 to select the desired framerate.
```
>screencaptureHX -fr 2
```
the above command will run the screencapture with framerate as third option  59.94.
### Setting Kvm
we  can also enable or disable use of KVM by using switch
```
> screencaptureHX -kvm 0 
```
zero to disable and 1 to enable the  kvm option.


### Setting mouse check or  not
we can show or hide  mouse by using following switch
```
>screencaptureHX -mouse  0
```
use  zero to disable it and 1  to enable it.

### Audio  Selection
The Audio  Selection  can  be done using  the  -audio switch 
```
>screencaptureHX -audio "Speakers (Realtek High Definition Audio)"
```

##### Note : using  combination of  the above switches is allowed.

###### Enjoy the Tool!!





