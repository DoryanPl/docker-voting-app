FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
WORKDIR /app

RUN useradd -m -s /bin/bash dotnetuser

COPY . ./
RUN dotnet restore
RUN dotnet publish -c release --self-contained false --no-restore -o out

FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app
COPY --from=build-env /etc/passwd /etc/passwd
COPY --from=build-env  /app/out .
USER dotnetuser
ENTRYPOINT ["dotnet", "Worker.dll"]
