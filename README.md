<div align="center">
<h1 align="center">
<img src="https://i.imgur.com/6ZeiCD9.png" width="100" />
<br>DOCKER-VOTING-APP</h1>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat-square&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=flat-square&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=flat-square&logo=Gunicorn&logoColor=white" alt="Gunicorn" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />

<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Socket.io-010101.svg?style=flat-square&logo=socketdotio&logoColor=white" alt="Socket.io" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=flat-square&logo=Express&logoColor=white" alt="Express" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat-square&logo=Flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📖 Table of Contents
- [📍 Overview](#-overview)
- [📂 Repository Structure](#-repository-structure)
- [📂 Folder Descriptions](#-folder-descriptions)
- [🚀 Getting Started](#-getting-started)
    - [🤖 Running docker-voting-app](#-running-docker-voting-app)

---

## 📍 Overview

For this mini-project, we provide you with the source code of a distributed application that allows an audience to vote between two options.

This application consists of two web interfaces:

The first one allows users to vote for one of the two options. Each web browser can only vote once, but it is always possible to change the vote.

The second interface allows users to view the voting results. The page is automatically updated whenever a new vote is counted.

---

## 📂 Repository Structure

```
└── docker-voting-app/
    │ 
    ├── compose.yaml
    │ 
    ├── result/
    │   ├── Dockerfile
    │   ├── server.js
    │   ├── package.json
    │   ├── package-lock.json
    │   └── views/
    │       ├── index.html
    │       ├── app.js
    │       ├── angular.min.js
    │       ├── socket.io.js
    │       └── stylesheets/
    │           └── style.css
    ├── vote/
    │   ├── Dockerfile
    │   ├── app.py
    │   ├── gunicorn_config.py
    │   ├── requirements.txt
    │   └── templates/
    │       └── index.html
    └── worker/
        ├── Dockerfile
        ├── Program.cs
        └── Worker.csproj
        
```
---

## 📂 Folder Descriptions

The `vote` folder

```
This folder contains the voting page in Python. 
It performs a POST request to the redis database for each vote.
```

The `result` folder

```
This folder contains the results page in javascript. 
It retrieves votes in real time.   
```

The `worker` folder

```
This folder links the redis database to postgres in the C# language. 
It retrieves votes from the redis database and inserts them into postgres.
```

## 🚀 Getting Started

***Install Docker***

On Windows :  [Download DockerDesktop](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)

On Macbook : [Download DockerDesktop](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64)

On Debian : 
```
sudo apt-get update
```

```
sudo apt-get install ca-certificates curl gnupg
```

```
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

```
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

You can verify that the installation is successful by running `hello-world` image : 

```
sudo docker run hello-world
```

---

### 🤖 Running docker-voting-app

```
docker compose up
```

[**Return**](#Top)

---

