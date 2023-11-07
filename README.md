# UAV-rental

docker pull postgres
docker run --name postgres-test -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=uav -p 5433:5432 -d postgres
docker exec -it postgres-test bash
