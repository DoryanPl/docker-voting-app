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
- [📝 Docker-Compose](#-docker-compose)
- [📝 Code Source](#-code-source)
- [🚀 Getting Started](#-getting-started)
    - [🤖 Running docker-voting-app](#-running-docker-voting-app)

---

## 📍 Overview

For this mini-project, we provide you with the source code of a distributed application that allows an audience to vote between two options.

It's an application that has two web interfaces : 
- The first one allows users to vote for one of the two options.
- The second interface allows users to view the voting results in real-time.

The project is comprised of three distinct modules:

- `Voting`: Implemented as a Python web application, this module enables users to cast their votes for one of two available options.
- `Worker`: Developed in .NET, this service retrieves votes from a Redis instance and persistently stores them in a PostgreSQL database.
- `Result`: A Node.js web application that provides real-time visualization of voting results.

In addition to these primary modules, the application relies on two critical components:

- `PostgreSQL`: This database stores the votes recorded by the Worker service.
- `Redis`: An instance of Redis is employed to facilitate the seamless and secure transmission of votes between different components of the application.

This application was launched with several bash scripts. To make it cleaner and simpler to run, we decided to use Docker.

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

## 📝 Docker-Compose

We used volumes of type "volume" to be able to store database information. We chose this type because we don't need to directly interact with or visualize the data.

## 📝 Code Source

We have updated the configurations in the files '/vote/app.py', '/worker/Progam.cs', and '/result/server.js' by replacing all occurrences of 'localhost' with either 'redis' or 'postgres,' depending on the specific requirements. This change was necessary because within a Docker container, 'localhost' points to the container itself, rather than the host machine.


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

***Configure the .env file***

Change the name of file to `.env` and define connection parameters to the postgres database.

---

### 🤖 Running docker-voting-app

```
git clone https://github.com/DoryanPl/docker-voting-app.git
```

```
cd docker-voting-app
```

```
docker compose up --build --force-recreate
```

[**Return**](#Top)

---

