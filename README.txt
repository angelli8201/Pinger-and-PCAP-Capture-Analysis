The folder contains 2 PDFs: one PDF for my answers for Part A of the programming assignment and another PDF for my answers for Part B of the programming assignment. 

For the code pertaining to Part A, I worked on the code in Visual Code Studio. The file, sample_pinger.py should be run through command line through the command:

sudo python3 sample_pinger.py < insert website address or an IP address>

The code should proceed to ping the given address. To stop the program, press Control C. After the command, the ping statistics will show up.


For the code pertaining to Part b, I worked on the code in Visual Code Studio. The file, analysis_pcap_arp.py, should be run without taking in any extra arguments: 

python3 analysis_pcap_arp.py

Within the code, a pcap file is read. If you want to test out the program with another pcap file, I made comments in line 5 to show where changes should be made. My approach when doing Part B was to first use the dpkt.pcap.Reader() method to read the provided pcap file. From this, I could filter out which packets within the pcap file were ARP packets. I created a getARPpackets(packetName) method to do this. Looking at Wireshark, I saw that under the Ethernet frame, if the packets were of type ARP, it would show 0x0806. I used Wireshark to see that the ethernet frame part was 14 bytes. I used the struct.unpack() method to extract and see if the packets were ARP packets. From there, I created a list and added the ARP packets to the list. Then, I created two methods: one method was to print each packet and the other method was to format each packet.  Using the source: http://www.tcpipguide.com/free/t_ARPMessageFormat.htm, I found the format of an ARP header element. Wireshark also confirmed the format. Using the struct.unpack() method, I was able to extract and translate bytes to a ARP header element. 