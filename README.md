# Fair Queueing Algorithm

This repository contains a Python implementation of a fair queueing algorithm that simulates fair bandwidth distribution across multiple users. It processes packet data and calculates metrics such as throughput, latency, and fairness index.

## Features:
- Implements deficit round robin fair queueing algorithm.
- Calculates throughput and latency for each user.
- Computes fairness index to evaluate bandwidth fairness.
- Generates random packet data and processes it using the fair queueing algorithm.

## Files:
- `generate_packets.py`: Generates random packet data for simulation.
- `fair_queue.py`: Implements the fair queueing algorithm and packet processing.
- `plot_results.py`: Plots the throughput, latency, and fairness index results.
- `packets.txt`: Sample input file with packet data for the simulation.

## Installation:
1. Clone the repository:
```bash
git clone https://github.com/username/repository-name.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the simulation:
```
python generate_packets.py
python fair_queue.py
python plot_results.py
```
Usage:
Modify the packets.txt file for custom packet sizes and arrival times. The simulation will output throughput, latency, and fairness index results along with graphical plots.
