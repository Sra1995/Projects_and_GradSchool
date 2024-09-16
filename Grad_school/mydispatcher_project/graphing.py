# need to change so that it shows multiple algorithms in one graph 
# at least 3 graphs based on something of my choice like comparing by quantum size, number of processes, etc


import matplotlib.pyplot as plt
import numpy as np

def read_output_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    return lines

def parse_output_data(output_data):
    data = {'process': [], 'start_time': [], 'waiting_time': [], 'turnaround_time': []}

    for line in output_data:
        parts = line.split(':')
        process_info = parts[0].split()
        time_info = parts[1].strip().split(', ')

        data['process'].append(int(process_info[0]))
        data['start_time'].append(list(map(int, time_info[0][2:].split('-')))[0])  # Use the start time of the range
        data['waiting_time'].append(int(time_info[2][2:]))
        data['turnaround_time'].append(int(time_info[4][2:]))

    return data

def plot_percentiles(data, title, y_label, x_label):
    percentiles = np.percentile(data[x_label], np.arange(0, 101, 10))

    plt.plot(percentiles, np.percentile(data[y_label], np.arange(0, 101, 10)), marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(x_label.capitalize())
    plt.ylabel(y_label.capitalize())
    plt.grid(True)
    plt.show()

def main():
    output_data = read_output_file('output.dat')
    parsed_data = parse_output_data(output_data)

    plot_percentiles(parsed_data, 'Waiting Time vs Percentile of Time Required', 'waiting_time', 'start_time')
    plot_percentiles(parsed_data, 'Normalized Turnaround Time vs Percentile of Time Required', 'turnaround_time', 'start_time')
    plot_percentiles(parsed_data, 'Normalized Response Time vs Utilization', 'start_time', 'waiting_time')

if __name__ == "__main__":
    main()
