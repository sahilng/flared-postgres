# flared-postgres (FLAsk+REDis <- POSTGRES)

A sample flask api that serves data from redis which acts as a cache for postgres

Example use case: A data API for a frontend charting tool, where data can be a little stale but must be returned quickly to prevent slow loading for the user

Can be run with docker compose, or in a VS Code Dev Container / GitHub Codespace

```sh
docker compose up -d
```

Runs on port 3000 by default
