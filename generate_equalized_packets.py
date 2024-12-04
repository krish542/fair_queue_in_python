import random

def generate_equalized_packets(num_users, num_packets_per_user, min_packet_size, max_packet_size, min_arrival_time, max_arrival_time):
    """
    Generate packets with more evenly distributed characteristics across users.

    Args:
        num_users (int): Number of users.
        num_packets_per_user (int): Number of packets per user.
        min_packet_size (int): Minimum packet size (bytes).
        max_packet_size (int): Maximum packet size (bytes).
        min_arrival_time (int): Minimum packet arrival time.
        max_arrival_time (int): Maximum packet arrival time.
    """
    with open("packets.txt", "w") as file:
        for user_id in range(1, num_users + 1):
            for _ in range(num_packets_per_user):
                packet_size = random.randint(min_packet_size, max_packet_size)
                arrival_time = random.randint(min_arrival_time, max_arrival_time)
                file.write(f"{user_id},{packet_size},{arrival_time}\n")

if __name__ == "__main__":
    num_users = 6
    num_packets_per_user = 5  # Ensures an equal number of packets per user
    min_packet_size = 500     # Minimum packet size in bytes
    max_packet_size = 1500    # Maximum packet size in bytes
    min_arrival_time = 0      # Minimum arrival time in seconds
    max_arrival_time = 20     # Maximum arrival time in seconds

    generate_equalized_packets(num_users, num_packets_per_user, min_packet_size, max_packet_size, min_arrival_time, max_arrival_time)
