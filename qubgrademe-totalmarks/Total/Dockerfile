#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Total.csproj", "."]
RUN dotnet restore "./Total.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Total.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Total.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Total.dll"]