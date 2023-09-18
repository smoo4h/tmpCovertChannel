# Covert Channel Communication Using Python

This project provides a simple example of covert channel communication between a sender and a receiver using Python. The sender and receiver communicate by creating and deleting folders in the `/tmp` directory.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Sender Code](#sender-code)
  - [Functions](#sender-functions)
  - [Flow](#sender-flow)
- [Receiver Code](#receiver-code)
  - [Functions](#receiver-functions)
  - [Flow](#receiver-flow)
- [Disclaimer](#disclaimer)

## Setup

1. Make sure Python is installed on your system.
2. Save the sender and receiver codes in separate Python files.
3. Ensure you have write and delete permissions for the `/tmp` directory.

## Usage

Run the sender and receiver codes in separate Python processes.

```bash
python sender.py
python receiver.py

##Sender Code
#Functions
string_to_binary(message): Converts a string into its binary ASCII representation.
send_bit(bit): Creates a folder in /tmp named either first or second based on the bit value (1 or 0).
#Flow
Takes a message as input from the user.
Converts the message to its binary ASCII representation.
Creates a folder named data1 in /tmp to signal the receiver to start reading.
Sends each bit of the message one at a time.
Waits for an acknowledgment (data2 folder) from the receiver.
Deletes the folders first or second and data1 after acknowledgment.
Repeats steps 4-6 for each bit in the message.
Deletes all created folders upon completion.

##Receiver Code
#Functions
read_bit(): Checks for folders named first or second in /tmp and returns the corresponding bit.
binary_to_string(binary_message): Converts a binary string back into ASCII text.
#Flow
Runs in a loop, waiting for a data1 folder to appear in /tmp.
Upon detecting data1, it starts reading the sent bits.
Acknowledges each read bit by creating a data2 folder.
Deletes the data2 folder after 2 seconds and waits for the next bit.
Converts the received bits back to the original message using ASCII encoding.
