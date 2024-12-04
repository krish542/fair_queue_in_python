import heapq
import matplotlib.pyplot as plt
import random

class User:
    def __init__(self, user_id, quantum):
        self.user_id = user_id
        self.quantum = quantum
        self.packets = []
        self.deficit_counter = 0
        self.total_bytes_sent = 0
        self.total_latency = 0
        self.packets_sent = 0

    def add_packet(self, packet_size, arrival_time):
        self.packets.append((packet_size, arrival_time))

    def send_packet(self, current_time):
        if not self.packets:
            return 0
        
        packet_size, arrival_time = self.packets[0]
        if self.deficit_counter >= packet_size:
            self.packets.pop(0)
            self.deficit_counter -= packet_size  # Deduct only the packet size from the deficit counter
            self.total_bytes_sent += packet_size
            latency_per_packet = (current_time - arrival_time) / packet_size
            self.total_latency += latency_per_packet
            self.packets_sent += 1
            return packet_size
        else:
            self.deficit_counter += self.quantum
            return 0

def fair_queue(packets_file, quantum=1000):
    users = {}
    with open(packets_file, 'r') as file:
        for line in file:
            user_id, packet_size, arrival_time = map(int, line.strip().split(','))
            if user_id not in users:
                users[user_id] = User(user_id, quantum)
            users[user_id].add_packet(packet_size, arrival_time)

    current_time = 0
    while any(user.packets for user in users.values()):
        for user in users.values():
            user.deficit_counter += user.quantum
            if user.packets:
                current_time += user.send_packet(current_time)

    return users

def calculate_throughput(users):
    total_time = sum(user.total_latency for user in users.values())
    throughputs = {user.user_id: user.total_bytes_sent / total_time for user in users.values()}
    return throughputs

def calculate_latency(users):
    latencies = {user.user_id: user.total_latency / user.packets_sent if user.packets_sent > 0 else 0 for user in users.values()}
    return latencies

def calculate_fairness_index(throughputs):
    total_throughput = sum(throughputs.values())
    total_throughput_square = sum(throughput**2 for throughput in throughputs.values())
    n = len(throughputs)
    
    fairness_index = (total_throughput ** 2) / (n * total_throughput_square) if total_throughput_square > 0 else 0
    return fairness_index

if __name__ == "__main__":
    packets_file = "packets.txt"
    
    # Run fair queue algorithm
    users = fair_queue(packets_file)
    
    # Calculate and display throughput information
    throughputs = calculate_throughput(users)
    print("Throughput Information:")
    for user_id, throughput in throughputs.items():
        print(f"User {user_id}: {throughput} bytes/sec")
    
    # Calculate and display latency information
    latencies = calculate_latency(users)
    print("\nLatency Information:")
    for user_id, latency in latencies.items():
        print(f"User {user_id}: {latency} sec")
    
    # Calculate and display fairness index for all users
    fairness_index = calculate_fairness_index(throughputs)
    print(f"\nFairness Index: {fairness_index}")
