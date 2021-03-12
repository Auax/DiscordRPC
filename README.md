# Discord Rich Presence
#### By Zelliux

---
This project aims to have an easy and quick configuration, 
so you can change the Discord Status at any time once you have configured it.

With this repository, you can change the Discord status, and set your own!
Here are the detailed steps:

1) First head to https://discord.com/developers/applications and log in with your account, 
and click the "New Application button"

    ![alt button image](https://i.imgur.com/jANJ5US.png)


2) A window will pop-up, choose your application name (you can change it later), and save.
  

- Once you've done that, you'll be redirected to your application dashboard, 
  here you need to copy your **CLIENT ID** (you'll need it later).
  
    <img src="https://i.ibb.co/Y3smwcL/Capture.png" height="70" />


3) Now you need to click the *Rich Presence* setting.
  
    <img src="https://i.ibb.co/xzNGpVN/Capture.png" height="200" />


4) You can add your own image, that'll appear in your profile. Click the ***Add Image(s)*** button
and select your image. (Remember the name you set for the image, you'll need it later).

    <img src="https://i.ibb.co/3rpFZVg/Capture.png" height="40" />

### That's all you need to configure in the Discord Developer Portal

5) Now, head to the ***config.json*** file, located inside the repository folder. 
Configure the file as you want. Don't forget to replace the ***clientID*** value with the 
  one you copied before from the Discord Developer Portal. *(Don't forget to save the changes).*
   

6) Once everything is done, run the ***main.py*** file (with the Discord Launcher opened), 
   and you should see the changes.
  
 ### Config.json arguments

- **clientID:** the ID of your application. *(Mandatory, without the correct ID, the code won't work)*


- **state**: The state Discord will show up in your profile. *(Mandatory, must be 2 characters long)*


- **startTimeStamp**: Epoch seconds for game start. *(Optional. No value = 0)*
  

- **largeImage & smallImage**: **Large/small** image key name for **large/small** profile artwork. 
  *(Optional, if the image key name doesn't exist, or it's Null, no image will appear)*

# Final Example
<img src="https://i.ibb.co/nggSxmK/Capture.png" height="100" />

---
Made with ❤ by <a href="https://github.com/Zelliux">Zelliux<a>
