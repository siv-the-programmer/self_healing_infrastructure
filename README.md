# Self-Healing_Infrastructure Docker Container

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)

A lightweight Python-based project demonstrating self-healing Docker containers.  
`monitor.py` ensures your container is always running, restarting it automatically if it stops or creating it if it doesn’t exist. Perfect for DevOps automation and learning resilient container workflows.

---

## Features

- **Self-Healing Containers:** Automatically start or restart Docker containers if they stop.
- **Python Automation:** Simple Python scripts manage container monitoring and recovery.
- **Containerized Workflow:** Runs inside Docker, keeping the system alive continuously.
- **Lightweight & Modular:** Easy to extend for multiple containers or more complex checks.

---

## Technologies Used

- Python 3.11
- Docker
- Bash (used internally via Python’s `subprocess`)

---

## Getting Started

### Clone the Repository
```
git clone https://github.com/yourusername/aws_projects.git
cd aws_projects
```
# Build the Docker Image

```
docker build -t auto_heal .
```
# Run the Container
```
docker run -d --name auto_heal auto_heal
```
# Start the Monitor
```
python monitor.py
```
The monitor script will check if the container is running every time it is executed and start it if needed. Run it in the background or as a service for continuous monitoring.

⚙️ How It Works
-
```
[ app.py running inside container ]
           ^
           |
           | (container heartbeat)
           |
[ monitor.py ] ---> checks container status ---> starts or restarts container if needed
app.py prints a heartbeat every 5 seconds to keep the container alive.

monitor.py ensures the container exists and is running, automatically starting or creating it as necessary.

This creates a simple self-healing Docker setup.
```
Project Structure
-
```
self_healing_docker/
├─ app.py          # Container heartbeat script
├─ monitor.py      # Monitor & self-healing script
├─ Dockerfile      # Docker container setup
├─ .gitignore      # Ignored files (env, cache, logs)
├─ README.md       # Project documentation
```
-
Still To Be Done / Roadmap
-
 Full Automation: Schedule monitor.py to run continuously (e.g., system service, cron job).

 Multiple Containers: Extend monitoring to handle multiple containers simultaneously.

 Logging & Alerts: Add logging and notifications (Slack, Email) on container failure/restart.

 Advanced Health Checks: Integrate health-check scripts beyond just “is it running?”

 -

# The project demonstrates the basics of container resilience and is ready for further automation and scaling.


Security
-
No sensitive data is stored, but avoid committing local configuration files unnecessarily.

.gitignore is configured to skip logs or temporary files.

📖 License
-
Open-source. Modify, extend, and experiment responsibly.
