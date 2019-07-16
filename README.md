
# GetWindowsSpotlight

## Background

If you are a Windows PC user, you may have noticed amazing backgrounds that show when you initial turn on your PC and arrive at the Lock Screen(where you are prompted to enter your username and password). The backgrounds come from a feature called Windows Spotlight. If you don't have that feature enabled, you can turn it on in Settings->Personalization->Lock screen. These backgrounds change often and replace the previous backgrounds. Windows/Microsoft curates these backgrounds from variety of sources and as they refresh the backgrounds the older backgrounds are lost (or removed from your Windows PC).

Have you ever wondered where those backgrounds are stored and how to selct them to for your main desktop background? Well I wondered that and found an article online that described the location where Windows temporarily stores them. It is in an obscure location and the filenames are very long and do not have an image extension (even though they are images).  

You can copy those files to any other location on your PC and rename them to add the extension of .jpg and then those files can be recognized by Windows as an image file and you can see previews of it. In addition to backgrounds, Windows also stores some other images in this location, probably used by some internal apps.

## About the Python script

I wrote this Python program to automatically check the Windows folder location for the Windows Spotlight background images, if it finds new ones, copies them to another location on the PC and changes the extension to add the .jpg. Since the folder can contain other images, before copying the script checks that the image has a width of 1920 pixels (which is the width of most of the Spotlight backgrounds). Interesteingly enough Windows SPotlight stores two files of the same picture. The second image is for mobile backgrounds. The script doesn't handle mobile images but could be easily added.

## Installation

### Prerequisites

*more to be added* here
