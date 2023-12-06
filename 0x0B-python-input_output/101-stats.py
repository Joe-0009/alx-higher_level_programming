#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys


"""init metrics"""

total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_processed = 0


def print_metrics():
    """pritns the metrics"""

    print(f"Total file size: {total_size}")
    for code in sorted(status_count):
        print(f"{code}: {status_code_count[code]}")


try:
    for line in sys.stdin:
        parts = line.split()
        status = int(parts[-2])
        size = int(parts[-1])

        status_count[status] += 1
        lines_processed += 1
        total_size += size

        if lines_processed % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
