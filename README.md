# stepmaniax.no

StepManiaX.no is an unofficial community page dedicated to StepManiaX players in Norway.

## Disclaimer

This website is **not affiliated with StepRevolution or the official StepManiaX brand**. It is a fan-run community page created to enhance the interest and connection between Norwegian StepManiaX players.

For official information, updates, and details about StepManiaX, please visit the official website: https://stepmaniax.com/.

## Prerequisites

Make sure you have the following installed:
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/jakobbekken/stepmaniax.no.git
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
