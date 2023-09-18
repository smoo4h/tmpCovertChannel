import os
import time

def string_to_binary(message):
    return ''.join(format(ord(ch), '08b') for ch in message)

def send_bit(bit):
    folder_name = 'first' if bit == '1' else 'second'
    os.mkdir(f"/tmp/{folder_name}")

def main():
    message = input("Enter the message to send: ")
    binary_message = string_to_binary(message)
    print(f"Sending message: {message} as binary: {binary_message}")
    
    os.mkdir("/tmp/data1")  # Signal to start reading

    for bit in binary_message:
        while os.path.exists("/tmp/data2"):
            os.rmdir("/tmp/data2")  # Remove acknowledgment
        send_bit(bit)
        while not os.path.exists("/tmp/data2"):  # Wait for acknowledgment
            time.sleep(1)
        os.rmdir(f"/tmp/first") if bit == '1' else os.rmdir("/tmp/second")  # Delete sent folder
        os.rmdir("/tmp/data1")  # Signal for next bit

    os.rmdir("/tmp/data1")  # Cleanup

if __name__ == "__main__":
    main()
