import random

def generate_packets(num_users, num_packets, max_packet_size, max_arrival_time):
    with open("packets.txt", "w") as file:
        for _ in range(num_packets):
            user_id = random.randint(1, num_users)
            packet_size = random.randint(100, max_packet_size)
            arrival_time = random.randint(0, max_arrival_time)
            file.write(f"{user_id},{packet_size},{arrival_time}\n")

if __name__ == "__main__":
    num_users = 6
    num_packets = 60
    max_packet_size = 2000
    max_arrival_time = 5
    generate_packets(num_users, num_packets, max_packet_size, max_arrival_time)