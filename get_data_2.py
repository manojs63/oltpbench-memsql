import csv
import sys

with open(sys.argv[1]) as f:
  reader = csv.reader(f)
  next(reader) # skip header
  data = []
  throughput = 0.0
  avg_latency = 0.0
  p90_latency = 0.0
  for row in reader:
    throughput += float(row[1])
    avg_latency += float(row[2])
    p90_latency += float(row[7])
    data.append(row)

  n = len(data)
  if int(sys.argv[2]) == 1:
    print(throughput/n)
  elif int(sys.argv[2]) == 2:
    print(avg_latency/n)
  elif int(sys.argv[2]) == 3:
    print(p90_latency/n)
