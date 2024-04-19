# MinecraftSkinMassDownloader
Mass Downloads as many minecraft skins as you like.

"uuid_list.txt" requires Usernames or UUID's of minecraft players to work, it will have one example in it which will be my username. If you are looking to mass download tons of users minercaft skins there is a link with 6.7million+ minecraft UUID's of players who logged onto hypixel. I will post my file containing the skins I have downloaded from that list in the future.
https://www.mediafire.com/file/d8xsan47gbv4l69/uuid_list.txt/file which I found at https://hypixel.net/threads/minecraft-username-list-6-800-000.5032332/
Both Trimmed and untrimmed uuids work
the uuids must be seperated by lines, as demonstrated in uuid_list.txt
This code was not written by me, I had an AI write and edit it from my promts, I will hand-edit it in the future this was just made for a fun project so I could learn some basic python functions.
You do not need to give Me, MidnightsCrow credit for anything you do with this. However I would appriciate a link found in your project leading to this, so that I may get some recognition for this, as I spent a long time editing it from AI's help. 
You are unable to sell this, but you may sell extensions to this project.

To start run "python3 skingrabber.py", "python skingrabber.py", or "py skingrabber.py" depending on your python setup.
Folder names and file names must be left alone to work properly.

Python is required to run this project.
Pip may be nescesary to install the "requests" import.

FOR THIS PROJECT TO RUN, YOU MUST CREATE A FOLDER TITLED "Skins" INSIDE THE PROJECT FOLDER. IF IT STILL DOESENT WORK TRY RENAMING THE FOLDER TITLES "MinecraftskinsMassDownloader" TO "Skins" SO YOUR FOLDER STRUCTURE SHOULD END UP LOOKING LIKE "Skins/Skins/{downloaded-skins}"

This project runs off of downloading files from https://minotar.net/, so huge shoutout and credits to them!

# Customability!

If you want to change the resolution, add "/{resolution}.png" in the code, like this:
at line 50, "   url = f"https://minotar.net/download/{username}.png"   "
change it to
"   url = f"https://minotar.net/{username}/{resolution}.png"    "

With that in mind, you can also change it to download the players isometric head
by changing it to "https://minotar.net/cube/{username}/{resolution}.png" 
**NOTE: REPLACE {resolution} with the resolution as it is not a variable in the code, and just a placeholder for this.**

If you want a full body frontal view replace it with "https://minotar.net/body/{username}/{resolution}.png"
If you want a full body frontal view with outer layer enabled replace it with "https://minotar.net/armor/body/{username}/{resolution}.png"
If you want just the head frontal view replace it with "https://minotar.net/avatar/{username}/{resolution}.png"
If you want just the head frontal view with outer layer enabled replace it with "https://minotar.net/helm/{username}/{resolution}.png"
If you want the bust of a user replace it with "https://minotar.net/bust/{username}/{resolution}.png"
If you want the bust of a user with outer layer enabled replace it with "https://minotar.net/armor/bust/{username}/{resolution}.png"

# AT THE MOMENT NONE OF THESE WILL WORK. YOU WILL HAVE TO MANUALLY GO TO THESE WEBSITES LISTED. THIS IS BEING WORKED ON.
