# Visual-Packet-Tracer

The main purpose of this project is to map the IP addresses from a Wireshark packet capture from the users computer. 
By inputing the public IP addresses and Wireshark packet capture, we are able to map in Google Maps where our traffic is coming from. 

For the Project:

Don't forget to add your own Wireshark packet capture to the folder/IDE you are using for this project. You need this for the program to read the different IP addresses to map. 

At the beginning, my program would output the header and footer but did not give me any feedback on my IP or my packet capture. 
I did a few differnt things to troubleshoot this. 
One; I added a few more checks to the main code to be able to better read where I needed to focu my efforts and where the code was not working. 
From here I was able to create a few different pieces of code to check if the GeoLiteCity file was readable, if my IP was in that file to be read, if the file was locked or not, and the destination source. 

To be able to run this project, the only code we need is the Main.py. The other .py files are for troubleshooting only. I put them here for other people's benefit if they are getting stuck. 

