import matplotlib.pyplot as plt
from fair_queue import calculate_throughput, calculate_latency, calculate_fairness_index, fair_queue

def plot_results(users):
    throughputs = calculate_throughput(users)
    latencies = calculate_latency(users)
    fairness_index = calculate_fairness_index(throughputs)

    user_ids = list(throughputs.keys())
    throughput_values = list(throughputs.values())
    latency_values = [latencies.get(user_id, 0) for user_id in user_ids]  # Ensure all user IDs have a value

    # Plot throughput
    plt.figure(figsize=(18, 6))
    plt.subplot(1, 3, 1)
    plt.bar(user_ids, throughput_values, color='blue')
    plt.xlabel('User ID')
    plt.ylabel('Throughput (bytes/sec)')
    plt.title('Throughput Information')

    # Plot latency
    plt.subplot(1, 3, 2)
    plt.bar(user_ids, latency_values, color='green')
    plt.xlabel('User ID')
    plt.ylabel('Latency (sec)')
    plt.title('Latency Information')

    # Plot fairness index
    plt.subplot(1, 3, 3)
    plt.bar(['Fairness Index'], [fairness_index], color='red')
    plt.ylabel('Fairness Index')
    plt.title('Fairness Index for All Users')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    packets_file = "packets.txt"
    users = fair_queue(packets_file)
    plot_results(users)