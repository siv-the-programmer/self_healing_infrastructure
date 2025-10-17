import subprocess
import datetime

container_name = "auto_heal"
image_name = "auto_heal"  # the Docker image

def container_exists(name):
    """Check if a container with this name exists (running or stopped)."""
    result = subprocess.run(
        ["docker", "ps", "-a", "-q", "-f", f"name={name}"],
        capture_output=True, text=True
    )
    return bool(result.stdout.strip())

def is_running(name):
    """Check if a container is currently running."""
    result = subprocess.run(
        ["docker", "ps", "-q", "-f", f"name={name}"],
        capture_output=True, text=True
    )
    return bool(result.stdout.strip())

def start_container(name, image):
    """Start the container if it exists, else run a new one."""
    if container_exists(name):
        print(f"{datetime.datetime.now()}: Container exists but not running, starting it...")
        subprocess.run(["docker", "start", name])
    else:
        print(f"{datetime.datetime.now()}: Container does not exist, creating and starting it...")
        subprocess.run(["docker", "run", "-d", "--name", name, image])

if __name__ == "__main__":
    if is_running(container_name):
        print(f"{datetime.datetime.now()}: Container is running")
    else:
        start_container(container_name, image_name)
