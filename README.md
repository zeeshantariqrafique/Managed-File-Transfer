# PyFiTransfer
A python utility to transfer files through socket . 

## Question : Why socket when we have ftp/sftp ?

Answer : Socket will not need user/pass for authorization which will remove credential maintainence from your file transfer utilities 
PLus , TCP ports are faster than FTP/SFTP ports so you can get your data to move swiftly between servers with much higher throughput.

The intention of this project is to enable real time and platform independant managed file transfer between servers .

Capabilities that are to be built :
- AES encryption
- Multiport transfer to increase transfer speed throughput 

Goal :
- Match the file transfer speed of Apache Kafka at much lighter weight for small scale applications and provide real time stream processing. 
- 20x faster than ftp and sftp protocol.
- Avoid username/password authentication like stfp , Plug and Play peer to peer security feature on initial setup .
