import os
import time

def read_bit():
    if os.path.exists("/tmp/first"):
        return '1'
    if os.path.exists("/tmp/second"):
        return '0'
    return None

def binary_to_string(binary_message):
    return ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

def main():
    received_bits = []
    
    while True:
        if os.path.exists("/tmp/data1"):
            bit = read_bit()
            if bit is not None:
                received_bits.append(bit)
                os.mkdir("/tmp/data2")  # Acknowledgment
                time.sleep(2)
                os.rmdir("/tmp/data2")  # Remove acknowledgment
            if not os.path.exists("/tmp/data1"):
                break

    binary_message = ''.join(received_bits)
    received_message = binary_to_string(binary_message)
    print(f"Received message: {received_message}")

if __name__ == "__main__":
    main()
