import psutil

print("Collecting basic system resource snapshot...")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()

print("CPU Usage (%):", cpu)
print("Memory Usage (%):", memory.percent)
print("Available Memory (MB):", round(memory.available / (1024 * 1024), 2))