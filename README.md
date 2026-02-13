# TaskVault

A personal task management app built with **React Native CLI** (TypeScript) and a **FastAPI** backend, all in a single monorepo. This project exercises fetching data from a REST API, performing CRUD operations against a SQLite database (running in Docker), managing state with Redux Toolkit, and navigating between screens.

---

## Architecture

```
┌──────────────────────────────┐     ┌──────────────────────────────┐
│     REACT NATIVE APP         │     │      DOCKER BACKEND          │
│     (mobile/)                │     │      (backend/)              │
│                              │     │                              │
│  Redux Toolkit ←→ Axios ─────────→│  FastAPI + SQLite            │
│  React Navigation            │     │  Port 8000 (API)            │
│  RNEUI Components            │     │  Port 8080 (Adminer)        │
│                              │     │                              │
│  Also fetches from:          │     │  Swagger UI: /docs           │
│  JSONPlaceholder (public)    │     │  ReDoc: /redoc               │
└──────────────────────────────┘     └──────────────────────────────┘
```

---

## Repository Structure

```
TaskVault/
├── mobile/                    ← React Native CLI project (TypeScript)
│   ├── src/
│   │   ├── api/               ← Axios clients & interceptors
│   │   ├── store/             ← Redux Toolkit (slices, hooks)
│   │   ├── navigation/        ← React Navigation (Stack + Tabs)
│   │   ├── screens/           ← Screen components
│   │   ├── components/        ← Reusable UI components
│   │   ├── themes/            ← Colors, typography, spacing
│   │   ├── types/             ← TypeScript type definitions
│   │   ├── utils/             ← Helpers (AsyncStorage, validation)
│   │   └── App.tsx            ← Root component
│   ├── android/
│   ├── ios/
│   ├── package.json
│   └── tsconfig.json
│
├── backend/                   ← FastAPI + SQLite backend
│   ├── app/
│   │   ├── main.py            ← FastAPI entry point + CORS
│   │   ├── database.py        ← SQLModel engine + sessions
│   │   ├── models.py          ← Task model + schemas
│   │   ├── seed.py            ← Initial seed data
│   │   └── routers/
│   │       └── tasks.py       ← CRUD route handlers
│   ├── Dockerfile
│   ├── pyproject.toml         ← Python dependencies (uv)
│   └── uv.lock
│
├── docker-compose.yml         ← Orchestrates API + Adminer
├── docs/                      ← Project documentation
│   ├── TASKS.md               ← Full task list (42 issues)
│   └── GITHUB_SETUP.md        ← GitHub project setup guide
├── README.md                  ← This file
└── .gitignore
```

---

## Prerequisites

Before starting, ensure you have the following installed:

| Tool               | Version   | Check Command                |
|--------------------|-----------|------------------------------|
| Node.js            | 18+       | `node --version`             |
| Yarn               | 1.22+     | `yarn --version`             |
| Docker & Compose   | 24+       | `docker --version`           |
| Android Studio     | Latest    | SDK Manager → API 34+        |
| Java JDK           | 17        | `java --version`             |
| Python (optional)  | 3.12+     | `python3 --version`          |
| uv (optional)      | Latest    | `uv --version`               |
| GitHub CLI         | Latest    | `gh --version`               |

> Python and uv are optional — they run inside Docker. Only needed if you want to develop the backend outside Docker.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TaskVault.git
cd TaskVault
```

### 2. Start the Backend

```bash
# Start FastAPI server + Adminer in background
docker compose up -d

# Verify services are running
docker compose ps

# Watch API logs (optional)
docker compose logs -f api
```

**Backend is now available at:**

| Service     | URL                              | Purpose                    |
|-------------|----------------------------------|----------------------------|
| API         | http://localhost:8000            | REST API base              |
| Swagger UI  | http://localhost:8000/docs       | Interactive API explorer   |
| ReDoc       | http://localhost:8000/redoc      | API documentation          |
| Health      | http://localhost:8000/api/health | Health check endpoint      |
| Adminer     | http://localhost:8080            | Database browser (SQLite)  |

> **First run**: The database is auto-created with seed data (5 sample tasks).

### 3. Start the React Native App

```bash
# Navigate to the mobile project
cd mobile

# Install dependencies
yarn install

# Start Metro bundler (Terminal 1)
npx react-native start

# In a new terminal, build and run on Android (Terminal 2)
npx react-native run-android
```

### 4. Connect Physical Device to Backend (Optional)

If running on a physical Android device instead of the emulator:

```bash
# Forward the backend port from device to your machine
adb reverse tcp:8000 tcp:8000

# Forward Metro bundler port
adb reverse tcp:8081 tcp:8081
```

> **Android Emulator**: No extra steps needed — the app uses `10.0.2.2` to reach the host machine's `localhost`.

---

## Daily Development Workflow

Open **3 terminals**:

```
Terminal 1 (Backend):
$ docker compose up -d
✓ FastAPI on http://localhost:8000
✓ Adminer on http://localhost:8080

Terminal 2 (Metro Bundler):
$ cd mobile && npx react-native start
✓ Metro on http://localhost:8081

Terminal 3 (Build & Run):
$ cd mobile && npx react-native run-android
✓ App installed on device/emulator
```

**Hot reload is automatic:**
- Edit `mobile/src/` files → Metro reloads the app instantly
- Edit `backend/app/` files → Uvicorn reloads the server automatically (via `--reload` flag + volume mount)
- View database → Open http://localhost:8080

---

## Backend Commands

```bash
# Start services
docker compose up -d

# Stop services
docker compose down

# Rebuild after Dockerfile/dependency changes
docker compose up -d --build

# View logs
docker compose logs -f api

# Reset database (delete + recreate with seed data)
rm -f backend/data/taskvault.db
docker compose restart api

# Stop and remove everything (including volumes)
docker compose down -v
```

## Frontend Commands

```bash
cd mobile

# Start Metro bundler
npx react-native start
npx react-native start --reset-cache    # with cache cleared

# Build and run
npx react-native run-android
npx react-native run-android --device   # physical device only

# Type checking
npx tsc --noEmit
npx tsc --noEmit --watch

# Clean build (when things break)
cd android && ./gradlew clean && cd ..
rm -rf node_modules && yarn install
npx react-native start --reset-cache

# Environment check
npx react-native doctor
```

---

## API Endpoints

| Method   | Endpoint           | Description                    |
|----------|--------------------|--------------------------------|
| `GET`    | `/api/tasks`       | List tasks (filters, pagination)|
| `GET`    | `/api/tasks/{id}`  | Get single task                |
| `POST`   | `/api/tasks`       | Create new task                |
| `PUT`    | `/api/tasks/{id}`  | Update task (partial)          |
| `DELETE` | `/api/tasks/{id}`  | Delete task                    |
| `GET`    | `/api/health`      | Health check                   |

**Query Parameters** (for `GET /api/tasks`):

| Param      | Example            | Description          |
|------------|--------------------|----------------------|
| `status`   | `?status=pending`  | Filter by status     |
| `priority` | `?priority=high`   | Filter by priority   |
| `search`   | `?search=react`    | Search by title      |
| `page`     | `?page=1`          | Page number          |
| `limit`    | `?limit=10`        | Items per page       |

---

## Deployment

### Backend Deployment (Production)

For production deployment, the backend can be hosted on any Docker-compatible platform:

**Option A — Railway / Render / Fly.io** (recommended for simplicity):

```bash
# These platforms auto-detect Dockerfile and deploy
# 1. Connect your GitHub repo
# 2. Set the root directory to `backend/`
# 3. Set environment variable: DB_PATH=/data/taskvault.db
# 4. Deploy
```

**Option B — VPS with Docker Compose**:

```bash
# On your server
git clone https://github.com/YOUR_USERNAME/TaskVault.git
cd TaskVault

# Production compose (remove Adminer, add HTTPS proxy)
docker compose -f docker-compose.prod.yml up -d
```

**Production considerations:**
- Remove `--reload` flag from Uvicorn CMD in Dockerfile
- Remove Adminer service (or restrict access)
- Add HTTPS reverse proxy (Caddy, Nginx, or Traefik)
- Set `allow_origins` in CORS to your specific domains
- Consider switching from SQLite to PostgreSQL for concurrent access

### Mobile Deployment

**Android APK (Debug)**:
```bash
cd mobile/android
./gradlew assembleDebug
# APK at: app/build/outputs/apk/debug/app-debug.apk
```

**Android AAB (Release — for Play Store)**:
```bash
cd mobile/android

# 1. Generate a signing key (one-time)
keytool -genkeypair -v -storetype PKCS12 -keystore taskvault-release.keystore \
  -alias taskvault -keyalg RSA -keysize 2048 -validity 10000

# 2. Configure signing in android/app/build.gradle

# 3. Build release bundle
./gradlew bundleRelease
# AAB at: app/build/outputs/bundle/release/app-release.aab
```

**Update API base URL for production:**
- In `mobile/src/api/client.ts`, update `LOCAL_BASE` to point to your deployed backend URL

---

## Tech Stack

### Frontend (mobile/)

| Library                    | Purpose                        |
|----------------------------|--------------------------------|
| React Native CLI 0.76+    | Mobile framework               |
| TypeScript 5.x            | Type safety                    |
| React Navigation v7       | Stack + Tab navigation         |
| Redux Toolkit              | State management               |
| Axios                      | HTTP client                    |
| AsyncStorage               | Local persistence              |
| RNEUI v4                   | UI component library           |
| React Native Vector Icons  | Icon library                   |

### Backend (backend/)

| Library          | Purpose                        |
|------------------|--------------------------------|
| Python 3.12      | Runtime                        |
| FastAPI          | REST API framework             |
| SQLModel         | ORM + validation (SQLAlchemy + Pydantic) |
| Uvicorn          | ASGI server                    |
| Docker Compose   | Container orchestration        |
| Adminer          | Database browser               |

---

## Project Management

This project uses **GitHub Issues**, **Milestones**, and **Projects** for task tracking.

- **42 tasks** organized into **10 milestones**
- See [`docs/TASKS.md`](docs/TASKS.md) for the full task list
- See [`docs/GITHUB_SETUP.md`](docs/GITHUB_SETUP.md) for setup instructions

---

## License

This project is for educational/practice purposes.
