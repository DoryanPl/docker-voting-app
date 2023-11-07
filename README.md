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
- [⚙️ Docker Files](#-docker-files)
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

---

## ⚙️ Docker Files

<details closed><summary>Compose File</summary>

[Compose](https://github.com/DoryanPl/docker-voting-app/blob/master/compose.yaml)

```
services:
  vote:
      container_name: vote
      build: ./vote
      restart: always
      ports:
        - "8080:8080"
      depends_on:
      - redis

  redis:
      container_name: redis
      image: "redis:alpine"
      volumes:
        - redis-data:/data
      restart: always
      
  worker:
      container_name: worker
      build: ./worker
      restart: always
      depends_on:
      - redis
      - postgres

  result:
      container_name: result
      build: ./result
      restart: always
      ports:
        - "8081:8081"
      depends_on:
      - postgres

  postgres:
      container_name: postgres
      image: postgres:14-alpine
      ports:
        - 5432:5432
      environment:
        - POSTGRES_PASSWORD=${DB_PASSWORD}
        - POSTGRES_USER=${DB_USERNAME}
        - POSTGRES_DB=${DB_NAME}
      volumes: 
        - postgres-data:/var/lib/postgresql/data
      restart: always

volumes:
  redis-data:
  postgres-data:

```

</details>


<details closed><summary>Vote</summary>

[Dockerfile](https://github.com/DoryanPl/docker-voting-app/blob/main/vote/Dockerfile)

```
FROM python:3.12-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["gunicorn", "app:app", "-c", "gunicorn_config.py"]
```

</details>

<details closed><summary>Result</summary>

[Dockerfile](https://github.com/DoryanPl/docker-voting-app/blob/main/result/Dockerfile)

```
FROM node:20.8-alpine
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY package*.json .
RUN npm ci --omit=dev
USER node
COPY --chown=node:node . .
EXPOSE 8081
CMD ["npm", "start"]
```

</details>

<details closed><summary>Worker</summary>

[Dockerfile](https://github.com/DoryanPl/docker-voting-app/blob/main/worker/Dockerfile) 

```
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
WORKDIR /App

COPY . ./
RUN dotnet restore
RUN dotnet publish -c release --self-contained false --no-restore -o out

FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /App
COPY --from=build-env /App/out .
ENTRYPOINT ["dotnet", "Worker.dll"]

```

</details>

---

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
git clone https://github.com/DoryanPl/docker-voting-app.git
```

```
cd docker-voting-app
```


```
sudo docker compose up
```

[**Return**](#Top)

---

