# stepmaniax.no

## Prerequisites

Make sure you have the following installed:
- Docker
- Docker Compose

## Setup Instructions
1. **Clone the repository**:
```bash
git clone git@github.com:jakobbekken/stepmaniax.no.git
cd stepmaniax.no
```

2. **Create the `.env` file**:
```bash
# And configure them as needed
cp .env.example .env
```

3. **Build images**:
```bash
docker compose build
```

## Running app
```bash
docker compose up
```

If you want to start in the background, run:
```bash
docker compose up -d
```
