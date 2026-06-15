import numpy as np

traffic = np.array([
    [100, 120, 110],
    [90, 95, 100],
    [500, 550, 600]
])

overall_avg = np.mean(traffic)

server_averages = np.mean(traffic, axis=1)

anomaly_servers = np.where(server_averages > 2 * overall_avg)[0]

print("Servers with above average traffic:", anomaly_servers)
