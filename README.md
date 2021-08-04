# Discord Rich Presence
#### By Auax

---
This project aims to have an easy and quick configuration, 
so you can change the Discord Status at any time once you have configured it.

With this repository, you can change the Discord status, and set your own!
Here are the detailed steps:

1) First head to https://discord.com/developers/applications and log in with your account, 
and click the `"New Application button"`

    ![alt button image](https://i.imgur.com/jANJ5US.png)


2) A window will pop-up, choose your application name (you can change it later), and save.
  

- Once you've done that, you'll be redirected to your application dashboard, 
  here you need to copy your `CLIENT ID` (you'll need it later).
  
    <img src="https://i.ibb.co/Y3smwcL/Capture.png" height="70" />


3) Now you need to click the *Rich Presence* setting.
  
    <img src="https://i.ibb.co/xzNGpVN/Capture.png" height="200" />


4) You can add your own image, that'll appear in your profile. Click the `Add Image(s)` button
and select your image. (Remember the name you set for the image, you'll need it later).

    <img src="https://i.ibb.co/3rpFZVg/Capture.png" height="40" />

### That's all you need to configure in the Discord Developer Portal

5) Now, head to the `config.json` file, located inside the repository folder. 
Configure the file as you want. Don't forget to replace the `clientID` value with the 
  one you copied before from the Discord Developer Portal. *(Don't forget to save the changes).*
   

6) Once everything is done, run the ***discord_status.py*** file (with the Discord Launcher opened), 
   and you should see the changes.
  
 ### `Config.json` arguments
 
| Argument       | Description                                                      | Mandatory                                     | Notes                                                                                                                         |
| -------------  |-------------                                                     | -----                                         | -----                                                                                                                         |
| ClientID       | The ID of your application.                                      | Yes                                           |This ID never changes, as long as you don't delete the application.                                                            |
| state          | The state Discord will show up in your profile.                  | Only if `stateRndSeq` is not defined.          |Must be at least 2 characters long. Can be left `null` in some cases  .                                                       |
| startTimeStamp | Epoch seconds for game start.                                    | No                                            |Default = `0`                                                                                                                  |
| stateRndSeq    | A list of texts that will be randomly chosen in each update.     | No                                            |Optional. Default=`null`                                                                                                       |
| useTime        | Whether keep track of time or not.                               | Yes                                           |Default = `true`                                                                                                               |
| buttons        | Add a max of two buttons in your profile.                        | No                                            |Syntax: `[{"label":"example", "url":"https://www.youtube.com"}, {...}]`. Default = `null`                                      |
| largeImage     | Large image key name for the large profile artwork.              | No                                            |If the image key name doesn't exist, or it's `null`, no image will appear)                                                     |
| smallImage     | Small image key name for the small profile artwork.              | No                                            |If the image key name doesn't exist, or it's `null`, no image will appear)                                                     |


# Example
<img src="https://i.ibb.co/nggSxmK/Capture.png" height="100" />

---

# Troubleshooting
* **I get thrown an error**
  - Check Discord is running on the same device you are trying to run this app.
  - Make sure the `clientID` info is correct.
  - If this doesn't fix the error. You can create an *issue* on GitHub. I'll fix it as fast as I can.

* **The state doesn't appear on Discord**
  - Make sure the `clientID` info is correct.
  - Check if you have enabled the `Activity Status` on Discord. To find it navigate to *User Setting > Activity Status > Display current activity as a status message*.

# My presets
### Notice that the presets will most probably come with an image. You'll need to upload the asset with the same name as the file. 
I've created some presets that you can download from the `presets` branch.
I will create more presets and upload them to GitHub.
---
Made with ❤ by <a href="https://github.com/auax">Auax<a>
