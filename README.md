# 🚀 Flask + Redis Dockerised App

**A modern containerized Flask web application integrated with Redis, built using Docker and orchestrated with Docker Compose.**  

This project demonstrates a real-world **multi-container Python setup**, showcasing how web services and in-memory databases can communicate seamlessly inside containers.

---

### 🧩 Tech Stack

| Component         | Description                                        |
|------------------|----------------------------------------------------|
| **Flask**         | Lightweight Python web framework for APIs and web apps |
| **Redis**         | In-memory data store for caching and fast data access |
| **Docker**        | Ensures consistent app environments across systems |
| **Docker Compose**| Orchestrates multiple containers and manages networking |

---

### 📁 Project Structure

flask-redis-docker/  
├── app.py                 # Flask application entry point  
├── Dockerfile             # Instructions to build the Flask image  
├── docker-compose.yml     # Defines Flask & Redis services and networking  
└── README.md              # Project documentation  

---

### ⚙️ Installation & Setup

1️⃣ **Clone the repository**  

```bash
git clone https://github.com/your-username/flask-redis-docker.git
cd flask-redis-docker
```

2️⃣ **Build and start the containers**  

```bash
docker-compose up --build
```

3️⃣ **Access the app**  

Open your browser and go to:  
http://localhost:5001

---

### 💡 Usage

The Flask app automatically connects to the Redis container over Docker’s internal network.  

You can extend `app.py` to:  

- ✅ Store data in Redis (`SET key value`)  
- ✅ Retrieve data from Redis (`GET key`)  
- ✅ Implement caching or session management  

To stop containers:  

```bash
docker-compose down
```

---

### 🐳 Docker Details

**Flask Service**  

- Base image: `python:3.8-slim`  
- Installs Flask + Redis Python client  
- Exposes port 5001  

**Redis Service**  

- Base image: official `redis` image  
- Runs Redis server on port 6379  

**Networking**  

Docker Compose automatically creates a network allowing the Flask container to connect to Redis:

```python
host = "redis"
port = 6379
```

---

### 🔧 Environment Variables

You can customize configurations in a `.env` file or directly in `docker-compose.yml`:

| Variable      | Default      | Description                  |
|---------------|-------------|------------------------------|
| `FLASK_ENV`   | development | Flask environment mode       |
| `REDIS_HOST`  | redis       | Redis hostname (service name)|
| `REDIS_PORT`  | 6379        | Redis port                   |

---

### 🧠 Example Output

```
Hello from Flask! Connected to Redis successfully 🎯
```

---

### ✨ Author

**Adnaan Mohamoud**  
📍 London

---

### 📜 License

This project is open-source and free to use under the **MIT License**.
=======
I am going to display a page that would keep count on the amount of visitors
