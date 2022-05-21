# Managed Light Weight File Transfer
A python utility to transfer files through plain old socket . 

## Usage 

To quickly start test the application from the project directory 
1 : Alter the source and destination details in transfer.yml 
2 : At the Destination Server , Start the socker server through command : sh scripts/start_file_reciever.sh
3 : At the Source Server , Run the socket client through the command , sh scripts/send_file.sh ../transfer.yml 

## Did not work ?
If your source and destination servers are seperate machines (Ideally , It should be to make sense of this project)
Then check the following 

1 : Network connection between both machines , from the source machine run the command : 
telnet <dest_ip_address> <port> 
(Before this please ensure to run the command on destination machine : sh scripts/start_file_reciever.sh )

2 : Check if destination port 9999 is free , else please checge the port in the config (transfer.xml) and try again

## Question : Why socket when we have ftp/sftp ?

Answer : Socket will not need user/pass for authorization which will remove credential maintainence from your file transfer utilities 
PLus , TCP ports are faster than FTP/SFTP ports so you can get your data to move swiftly between servers with much higher throughput.

The intention of this project is to enable real time and platform independant managed file transfer between servers .



Capabilities that are yet to be built :
- AES encryption
- Multiport transfer to increase transfer speed throughput 

Goal :
- Match the file transfer speed of Apache Kafka at much lighter weight for small scale applications and provide real time stream processing. 
- 20x faster than ftp and sftp protocol.
- Avoid username/password authentication like stfp , Plug and Play peer to peer security feature on initial setup .
