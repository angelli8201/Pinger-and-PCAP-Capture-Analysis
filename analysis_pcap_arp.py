import dpkt
import socket
import struct

#if want to test another pcap file then change the name here
f = open('assignment4_my_arp.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)
packets = []


# Look at which packets are ARP. From wireshark : Ethernet frame : ARP(0X0806)
def getARPpackets(packetName):
    for timestamp, buf in pcap:
        ethFrame = buf[:14]
        ethUnpack = struct.unpack("!6s6sH", ethFrame)
        ethType = ethUnpack[2]
        if(ethType == 0x0806):
            packets.append(buf)
    return packets
    #print(len(packets))


def printARPpackets(packet):
    for pkt in packets:
        formatARPpackets(pkt)

#format- parse the bytes and translate
def formatARPpackets(packet):
    (hardwareType ,protocolType,hardwareSize ,protocolSize ,opcode , senderMAC ,senderIP ,destMAC ,destIP ) = struct.unpack('2s2s1s1s2s6s4s6s4s',packet[14:42])

    hardwareTypex= int.from_bytes(hardwareType, byteorder='big')
    protocolTypex = int.from_bytes(protocolType, byteorder='big')
    hardwareSizex = int.from_bytes(hardwareSize, byteorder='big')
    protocolSizex = int.from_bytes(protocolSize, byteorder='big')
    opcodex = int.from_bytes(opcode, byteorder='big')
    senderMACx = senderMAC
    destMACx = destMAC
    senderIPx = socket.inet_ntoa(senderIP)
    destIPx = socket.inet_ntoa(destIP)
    
    if (opcodex == 1):
        print ("ARP Request: ")
    if (opcodex == 2):
        print ("ARP Response: ")

    print("Hardware Type: ",hardwareTypex)
    print("Protocol Type: ",protocolTypex)
    print("Hardware Size ",hardwareSizex)
    print("Protocol Size: ",protocolSizex)
    print("Opcode ",opcodex)
    print("Sender MAC address: ", senderMACx[0:1].hex(), ":",senderMACx[1:2].hex(), ":",senderMACx[2:3].hex(), ":" ,
        senderMACx[3:4].hex(), ":",senderMACx[4:5].hex(),":",senderMACx[5:6].hex())
    print("Sender IP Address: ", senderIPx)
    print("Destination MAC address: ", destMACx[0:1].hex(), ":",destMACx[1:2].hex(), ":",destMACx[2:3].hex(), ":" ,
        destMACx[3:4].hex(), ":",destMACx[4:5].hex(),":",destMACx[5:6].hex())
    print("Destination IP Address: ", destIPx)
    print("")


def main():
    getARPpackets(pcap) #filter out ARP packets in pcap file
    printARPpackets(packets) 

if __name__ == '__main__':
    main()