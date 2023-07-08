# Managed Lightweight File Transfer

[![master](https://github.com/zeeshantariqrafique/Managed-File-Transfer/actions/workflows/managed-file-transfer.yml/badge.svg?event=push)](https://github.com/zeeshantariqrafique/Managed-File-Transfer/actions/workflows/managed-file-transfer.yml)

Managed Lightweight File Transfer is a Python utility that allows you to transfer files through plain old sockets.

## Usage

To quickly test the application from the project directory:

1. Modify the source and destination details in `transfer.yml`.
2. On the destination server, start the socket server by running the command: `sh scripts/start_file_receiver.sh`.
3. On the source server, run the socket client using the command: `sh scripts/send_file.sh ../transfer.yml`.

## Troubleshooting

If the application does not work as expected, please check the following:

1. Ensure that there is a network connection between the source and destination servers. From the source machine, run the command: `telnet <dest_ip_address> 9999`. Before doing this, make sure to run the command `sh scripts/start_file_receiver.sh` on the destination machine.
2. Check if port 9999 is available on the destination server. If it is not free, modify the port in the configuration file (`transfer.yml`) and try again.

## Why use sockets instead of FTP/SFTP?

The use of sockets eliminates the need for user/password authorization, removing the need to manage credentials in your file transfer utilities. Additionally, TCP ports used by sockets are faster than those used by FTP/SFTP, resulting in higher throughput and faster data transfer between servers.

The goal of this project is to enable real-time and platform-independent managed file transfer between servers.

## Planned Features

The following capabilities are yet to be built:

- AES encryption for secure file transfer.
- Multiport transfer to increase transfer speed throughput.

## Goals

The objectives of this project are:

- Achieve file transfer speeds comparable to Apache Kafka but with a much lighter weight for small-scale applications, enabling real-time stream processing.