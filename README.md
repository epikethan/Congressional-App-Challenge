MEW, More Efficient Work

This is basically a website blocker

There are several steps to setting up this website blocker.

The first step is to open Visual Studio Code as an administrator.                  
To do this, you can press type into the search bar in your task bar, and type Visual Studio.                   
Then right click on the option and press, “Run as Administrator” Then click, “Yes”.                  

The second step is to find your public IPv4.                   
To do this, go to your web browser search up, “What is my public IPV4?” and you can click the first website that shows up.                   
Once on the website, it will state your IPV4, which you will need to copy into the code.                   
Then, paste the IP address into the line, “ ip_address = ‘’ “.                   
Make sure to paste the IP address between the two quotation marks.                  

The third step is to download this sound file and paste the file path into your code.                  
To download the sound file go to this link and click download on the right hand side.                                  

https://pixabay.com/sound-effects/alarm-beep-clock-165474/                  

Then go to files, downloads, and then right click the sound file.                  
Then click, "Copy as Path" and paste it into line 12 between the quotation marks.

Finally, go back to line 8.                  
Put the websites you would like to block by typing their address into the list.
For example, if I wanted to block Youtube and Facebook, I would type into the list "youtube.com" and "facebook.com", making line 12 look like:               

website_list = ["youtube.com, facebook.com"]

Once you have set these up, you can now run the program.

Then input time into the text boxes, in the format " hours minutes seconds " and you are then able to start your timer.                  
Make sure to have your browser closed when you start the timer as if it currently open, this app will not work.                  
And once the timer ends, click ok on the popup window, close your browser and reopen it.


