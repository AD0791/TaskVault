# TaskVault — Project Task List

> **Purpose**: This document defines every task needed to build TaskVault from scratch. Each task is designed to be created as a **GitHub Issue** and organized using **GitHub Projects** (kanban board), **Milestones**, and **Labels**.

---

## How to Use This Document with GitHub

### Monorepo Structure

TaskVault lives in a **single GitHub repository** with this layout:

```
TaskVault/
├── mobile/                ← React Native CLI project
├── backend/               ← FastAPI + Docker backend
├── docker-compose.yml     ← Root-level orchestration
├── docs/                  ← Project documentation
│   ├── TASKS.md           ← This file
│   └── GITHUB_SETUP.md   ← GitHub setup instructions
├── README.md              ← Launch & deployment guide
└── .gitignore
```

### GitHub Project Management Mapping

| GitHub Feature  | How We Use It                                              |
|-----------------|------------------------------------------------------------|
| **Issues**      | Each task below becomes one GitHub Issue                    |
| **Milestones**  | Group issues by phase (M1, M2, M3...)                      |
| **Labels**      | Categorize by type, priority, and area                     |
| **Projects**    | Kanban board with columns: Backlog → In Progress → Done    |
| **Branches**    | One branch per issue: `feature/TV-XX-short-description`    |

### Labels to Create

| Label              | Color     | Description                        |
|--------------------|-----------|------------------------------------|
| `type:setup`       | `#0E8A16` | Project setup and configuration    |
| `type:feature`     | `#1D76DB` | New feature implementation         |
| `type:backend`     | `#D93F0B` | Backend / API work                 |
| `type:frontend`    | `#7057FF` | React Native / mobile work         |
| `type:docs`        | `#0075CA` | Documentation                      |
| `type:devops`      | `#B60205` | Docker, CI/CD, deployment          |
| `type:test`        | `#FBCA04` | Testing                            |
| `priority:high`    | `#D93F0B` | Must be done first                 |
| `priority:medium`  | `#F9D0C4` | Important but not blocking         |
| `priority:low`     | `#C5DEF5` | Nice to have                       |
| `area:navigation`  | `#BFD4F2` | Navigation related                 |
| `area:state`       | `#D4C5F9` | Redux / state management           |
| `area:api`         | `#FEF2C0` | API layer / Axios                  |
| `area:ui`          | `#E6CCB3` | UI components and styling          |
| `area:forms`       | `#C2E0C6` | Form inputs and validation         |

### Milestones

| Milestone | Title                          | Target     |
|-----------|--------------------------------|------------|
| M1        | Project Infrastructure         | Day 1 AM   |
| M2        | Backend API                    | Day 1 PM   |
| M3        | RN Project Foundation          | Day 1 PM   |
| M4        | Navigation System              | Day 2 AM   |
| M5        | State Management (Redux)       | Day 2 AM   |
| M6        | API Layer (Axios)              | Day 2 PM   |
| M7        | Users Feature (Remote)         | Day 2 PM   |
| M8        | Tasks Feature (CRUD)           | Day 3 AM   |
| M9        | Task Form & Validation         | Day 3 AM   |
| M10       | Settings, Polish & Docs        | Day 3 PM   |

---

## Task List

> Each task includes: title, description (for the issue body), labels, milestone, and acceptance criteria. Tasks are numbered `TV-XX` for easy reference.

---

### Milestone 1 — Project Infrastructure

#### TV-01: Initialize monorepo and Git repository

**Labels**: `type:setup`, `priority:high`
**Milestone**: M1

**Description**:
Set up the root TaskVault repository with the monorepo folder structure.

**Acceptance Criteria**:
- [x] GitHub repo created: `TaskVault`
- [x] Root `.gitignore` covers both Python and React Native artifacts
- [x] Folder structure established: `mobile/`, `backend/`, `docs/`
- [x] Initial commit pushed to `main`

---

#### TV-02: Create root docker-compose.yml

**Labels**: `type:devops`, `type:setup`, `priority:high`
**Milestone**: M1

**Description**:
Create the root-level `docker-compose.yml` that orchestrates the FastAPI server and Adminer DB browser. The compose file should reference the `backend/` directory for the build context.

**Acceptance Criteria**:
- [x] `docker-compose.yml` at project root
- [x] `api` service defined (build from `./backend`, port 8000)
- [x] `adminer` service defined (port 8080)
- [x] Volume mounts for SQLite persistence and hot-reload
- [x] Environment variables for DB path

**Reference**: See project design doc § 4 — Docker Architecture

---

#### TV-03: Create backend Dockerfile and Python project config

**Labels**: `type:devops`, `type:backend`, `priority:high`
**Milestone**: M1

**Description**:
Create `backend/Dockerfile` using Python 3.12-slim with uv package manager, and `backend/pyproject.toml` with all required dependencies (FastAPI, SQLModel, Uvicorn, aiosqlite).

**Acceptance Criteria**:
- [x] `backend/Dockerfile` created (Python 3.12-slim, uv, uvicorn with --reload)
- [x] `backend/pyproject.toml` with all dependencies and versions
- [x] `uv.lock` generated and committed
- [x] `docker compose build` succeeds without errors

---

#### TV-04: Write root README.md with launch and deployment instructions

**Labels**: `type:docs`, `priority:medium`
**Milestone**: M1

**Description**:
Write a comprehensive README that explains the monorepo structure, prerequisites, how to launch the backend and frontend, and deployment notes.

**Acceptance Criteria**:
- [x] Project overview and architecture summary
- [x] Prerequisites section (Docker, Node, Android SDK, etc.)
- [x] Step-by-step backend launch instructions
- [x] Step-by-step frontend launch instructions
- [x] Port forwarding notes for physical devices
- [x] Deployment section

---

### Milestone 2 — Backend API

#### TV-05: Implement SQLModel database layer

**Labels**: `type:backend`, `priority:high`
**Milestone**: M2

**Description**:
Create the database module with SQLModel engine, session dependency, and table creation logic. Implement the Task model with all fields (id, title, description, status, priority, created_at, updated_at) and the request schemas (TaskCreate, TaskUpdate).

**Acceptance Criteria**:
- [ ] `backend/app/database.py` — engine, `create_db_and_tables()`, `get_session()`
- [ ] `backend/app/models.py` — `Task` table model, `TaskCreate`, `TaskUpdate` schemas
- [ ] `TaskStatus` enum: pending, in_progress, done
- [ ] `TaskPriority` enum: low, medium, high
- [ ] Table auto-creates on startup

---

#### TV-06: Implement seed data module

**Labels**: `type:backend`, `priority:medium`
**Milestone**: M2

**Description**:
Create seed data that is inserted on first startup when the tasks table is empty. Include 5 sample tasks with varying statuses and priorities.

**Acceptance Criteria**:
- [ ] `backend/app/seed.py` with `SEED_TASKS` list (5 tasks)
- [ ] Seed only runs when table is empty (idempotent)
- [ ] Mix of statuses (pending, in_progress, done) and priorities (low, medium, high)

---

#### TV-07: Implement FastAPI app entry point with CORS and lifespan

**Labels**: `type:backend`, `priority:high`
**Milestone**: M2

**Description**:
Create the FastAPI application entry point with CORS middleware (allow all origins for mobile dev), lifespan handler for DB initialization, and health check endpoint.

**Acceptance Criteria**:
- [ ] `backend/app/main.py` with FastAPI app instance
- [ ] CORS middleware allowing all origins
- [ ] Lifespan handler that calls `create_db_and_tables()` on startup
- [ ] `GET /api/health` returns `{"status": "ok", "service": "taskvault-api"}`
- [ ] Swagger UI accessible at `/docs`
- [ ] ReDoc accessible at `/redoc`

---

#### TV-08: Implement CRUD route handlers for tasks

**Labels**: `type:backend`, `type:feature`, `priority:high`
**Milestone**: M2

**Description**:
Create the tasks router with all CRUD endpoints: list (with filters + pagination), get by ID, create, update (partial), and delete.

**Acceptance Criteria**:
- [ ] `GET /api/tasks` — list all tasks with response wrapper `{success, data, pagination}`
- [ ] `GET /api/tasks?status=pending` — filter by status
- [ ] `GET /api/tasks?priority=high` — filter by priority
- [ ] `GET /api/tasks?search=react` — search by title (contains)
- [ ] `GET /api/tasks?page=1&limit=10` — pagination support
- [ ] `GET /api/tasks/{id}` — get single task (404 if not found)
- [ ] `POST /api/tasks` — create new task (201 response)
- [ ] `PUT /api/tasks/{id}` — partial update (updates `updated_at`)
- [ ] `DELETE /api/tasks/{id}` — delete task (404 if not found)
- [ ] All endpoints tested via Swagger UI

---

#### TV-09: Verify full backend with Docker

**Labels**: `type:backend`, `type:devops`, `priority:high`
**Milestone**: M2

**Description**:
Bring up the full Docker environment, verify all endpoints work via Swagger UI, and confirm Adminer can browse the SQLite database.

**Acceptance Criteria**:
- [ ] `docker compose up -d` starts both services cleanly
- [ ] Swagger UI at `http://localhost:8000/docs` — all endpoints visible and testable
- [ ] Adminer at `http://localhost:8080` — can see `task` table and seed data
- [ ] Hot reload works (edit Python code → changes reflected without rebuild)
- [ ] `docker compose down && docker compose up -d` preserves data (volume persistence)

---

### Milestone 3 — React Native Project Foundation

#### TV-10: Initialize React Native CLI project with TypeScript

**Labels**: `type:setup`, `type:frontend`, `priority:high`
**Milestone**: M3

**Description**:
Create the React Native project inside the `mobile/` directory using the CLI with TypeScript template. Verify it builds and runs on Android emulator.

**Acceptance Criteria**:
- [ ] RN project initialized in `mobile/` folder
- [ ] TypeScript template used
- [ ] `npx react-native run-android` succeeds
- [ ] Default app renders on emulator/device

---

#### TV-11: Install all project dependencies

**Labels**: `type:setup`, `type:frontend`, `priority:high`
**Milestone**: M3

**Description**:
Install all required npm packages for navigation, state management, API, storage, and UI.

**Packages**:
- Navigation: `@react-navigation/native`, `@react-navigation/stack`, `@react-navigation/bottom-tabs`, `react-native-screens`, `react-native-safe-area-context`, `react-native-gesture-handler`
- State: `@reduxjs/toolkit`, `react-redux`
- API: `axios`, `@react-native-async-storage/async-storage`
- UI: `@rneui/themed`, `@rneui/base`, `react-native-vector-icons`
- Dev: `babel-plugin-module-resolver`

**Acceptance Criteria**:
- [ ] All packages installed
- [ ] Android build still succeeds after installation
- [ ] No peer dependency conflicts

---

#### TV-12: Configure TypeScript path aliases

**Labels**: `type:setup`, `type:frontend`, `priority:medium`
**Milestone**: M3

**Description**:
Set up path aliases (`@screens`, `@components`, `@store`, `@api`, `@navigation`, `@themes`, `@utils`, `@types`) in both `tsconfig.json` and `babel.config.js`.

**Acceptance Criteria**:
- [ ] `tsconfig.json` — `baseUrl` and `paths` configured
- [ ] `babel.config.js` — `module-resolver` plugin with matching aliases
- [ ] Imports using `@` aliases resolve correctly
- [ ] TypeScript intellisense works with aliases

---

#### TV-13: Create project folder structure and theme constants

**Labels**: `type:setup`, `type:frontend`, `priority:medium`
**Milestone**: M3

**Description**:
Create the `src/` directory structure and implement the theme system (colors, typography, spacing).

**Acceptance Criteria**:
- [ ] Directories created: `api/`, `store/`, `navigation/`, `screens/`, `components/`, `themes/`, `types/`, `utils/`
- [ ] `themes/colors.ts` — complete color palette (primary, status, neutral, priority)
- [ ] `themes/typography.ts` — text style definitions (h1, h2, h3, body, caption, button)
- [ ] `themes/spacing.ts` — consistent spacing scale
- [ ] `themes/index.ts` — barrel export

---

#### TV-14: Define TypeScript types for API data

**Labels**: `type:frontend`, `priority:medium`
**Milestone**: M3

**Description**:
Create TypeScript interfaces for all data shapes used in the app.

**Acceptance Criteria**:
- [ ] `types/user.ts` — `User` interface (matching JSONPlaceholder response)
- [ ] `types/task.ts` — `Task`, `TaskStatus`, `TaskPriority` types (matching backend)
- [ ] `types/api.ts` — `ApiResponse<T>`, `PaginatedResponse<T>`, `ApiError` types

---

### Milestone 4 — Navigation System

#### TV-15: Implement Tab Navigator with bottom tabs

**Labels**: `type:feature`, `type:frontend`, `area:navigation`, `priority:high`
**Milestone**: M4

**Description**:
Create the bottom tab navigator with three tabs: Users, Tasks, and Settings. Include icons from react-native-vector-icons.

**Acceptance Criteria**:
- [ ] `TabNavigator.tsx` with three tabs
- [ ] Each tab has an icon (using vector icons)
- [ ] Active/inactive tab styling (color change)
- [ ] Tab labels visible below icons

---

#### TV-16: Implement Stack Navigator with all screens

**Labels**: `type:feature`, `type:frontend`, `area:navigation`, `priority:high`
**Milestone**: M4

**Description**:
Create the root stack navigator containing: SplashScreen, Main (TabNavigator), UserDetail, and TaskForm screens.

**Acceptance Criteria**:
- [ ] `StackNavigator.tsx` with all screen registrations
- [ ] `AppNavigator.tsx` wrapping everything in `NavigationContainer`
- [ ] Splash screen as initial route (header hidden)
- [ ] Main tab navigator as second route (header hidden)
- [ ] UserDetail and TaskForm push on top of tabs
- [ ] Proper transition animations

---

#### TV-17: Define navigation TypeScript types

**Labels**: `type:frontend`, `area:navigation`, `priority:medium`
**Milestone**: M4

**Description**:
Create strongly typed navigation params so that `navigation.navigate()` and `route.params` are fully typed.

**Acceptance Criteria**:
- [ ] `RootStackParamList` — typed params for all stack screens
- [ ] `MainTabParamList` — typed params for all tab screens
- [ ] Screen prop types exported (`UserDetailProps`, `TaskFormProps`, etc.)
- [ ] No `any` types in navigation calls

---

#### TV-18: Implement Splash Screen with navigation to main

**Labels**: `type:feature`, `type:frontend`, `area:navigation`, `priority:medium`
**Milestone**: M4

**Description**:
Create a splash screen that displays the app logo/name and auto-navigates to the main tab screen after a brief delay.

**Acceptance Criteria**:
- [ ] Splash screen renders app name "TaskVault" with styling
- [ ] Auto-navigates to `Main` after 2 seconds
- [ ] Uses `navigation.reset()` to prevent back navigation to splash
- [ ] No header visible on splash screen

---

### Milestone 5 — State Management (Redux)

#### TV-19: Configure Redux store with typed hooks

**Labels**: `type:feature`, `type:frontend`, `area:state`, `priority:high`
**Milestone**: M5

**Description**:
Set up the Redux store using `configureStore` and create typed hooks (`useAppSelector`, `useAppDispatch`).

**Acceptance Criteria**:
- [ ] `store/index.ts` — store configured with all three reducers
- [ ] `store/hooks.ts` — typed `useAppSelector` and `useAppDispatch`
- [ ] `RootState` and `AppDispatch` types exported
- [ ] `<Provider store={store}>` wrapping app in root component

---

#### TV-20: Implement Users slice with async thunks

**Labels**: `type:feature`, `type:frontend`, `area:state`, `priority:high`
**Milestone**: M5

**Description**:
Create the users slice for fetching data from JSONPlaceholder. Include `fetchUsers` and `fetchUserById` async thunks.

**Acceptance Criteria**:
- [ ] `usersSlice.ts` with initial state: `items`, `selectedUser`, `loading`, `error`, `searchQuery`
- [ ] `fetchUsers` thunk — `GET /users` from JSONPlaceholder
- [ ] `fetchUserById` thunk — `GET /users/:id` from JSONPlaceholder
- [ ] `extraReducers` handling pending/fulfilled/rejected for both thunks
- [ ] `setSearchQuery` and `clearSelectedUser` reducers

---

#### TV-21: Implement Tasks slice with CRUD async thunks

**Labels**: `type:feature`, `type:frontend`, `area:state`, `priority:high`
**Milestone**: M5

**Description**:
Create the tasks slice for full CRUD operations against the local FastAPI backend.

**Acceptance Criteria**:
- [ ] `tasksSlice.ts` with initial state: `items`, `loading`, `error`, `filter`, `pagination`
- [ ] `fetchTasks` thunk — `GET /api/tasks` with filter/pagination params
- [ ] `createTask` thunk — `POST /api/tasks`
- [ ] `updateTask` thunk — `PUT /api/tasks/{id}`
- [ ] `deleteTask` thunk — `DELETE /api/tasks/{id}`
- [ ] `extraReducers` handling all async states
- [ ] `setFilter` reducer

---

#### TV-22: Implement UI slice for global state

**Labels**: `type:feature`, `type:frontend`, `area:state`, `priority:medium`
**Milestone**: M5

**Description**:
Create the UI slice for managing global loading overlay, toast notifications, and theme preference.

**Acceptance Criteria**:
- [ ] `uiSlice.ts` with state: `globalLoading`, `toast`, `theme`
- [ ] Reducers: `showLoading`, `hideLoading`, `showToast`, `hideToast`, `toggleTheme`
- [ ] Toast type supports `success`, `error`, `info`, `warning`

---

### Milestone 6 — API Layer (Axios)

#### TV-23: Create Axios client instances with interceptors

**Labels**: `type:feature`, `type:frontend`, `area:api`, `priority:high`
**Milestone**: M6

**Description**:
Set up two Axios instances: `publicApi` (JSONPlaceholder) and `localApi` (your Docker backend). Add request/response interceptors for logging and error normalization.

**Acceptance Criteria**:
- [ ] `api/client.ts` with `publicApi` and `localApi` instances
- [ ] `publicApi` base URL: `https://jsonplaceholder.typicode.com`
- [ ] `localApi` base URL: platform-aware (10.0.2.2 for Android emulator, localhost for iOS)
- [ ] Request interceptor: logs method + URL
- [ ] Response interceptor: normalizes error messages
- [ ] Timeout configured (10s)

---

#### TV-24: Create API endpoint constants and service functions

**Labels**: `type:feature`, `type:frontend`, `area:api`, `priority:medium`
**Milestone**: M6

**Description**:
Define endpoint constants and create typed service functions that the Redux thunks will call.

**Acceptance Criteria**:
- [ ] `api/endpoints.ts` — all endpoint URL constants
- [ ] `api/index.ts` — barrel export
- [ ] Service functions return properly typed responses
- [ ] Error handling consistent across all functions

---

### Milestone 7 — Users Feature (Remote API)

#### TV-25: Build UserCard reusable component

**Labels**: `type:feature`, `type:frontend`, `area:ui`, `priority:high`
**Milestone**: M7

**Description**:
Create a reusable `UserCard` component that displays user name, username, email, and company. It should be pressable to navigate to detail.

**Acceptance Criteria**:
- [ ] `components/UserCard.tsx` with typed props
- [ ] Displays: name, @username, email, company name
- [ ] Right chevron arrow indicating navigation
- [ ] Proper spacing, typography, and card styling
- [ ] `onPress` callback prop

---

#### TV-26: Implement Users Screen with FlatList

**Labels**: `type:feature`, `type:frontend`, `priority:high`
**Milestone**: M7

**Description**:
Build the Users tab screen that fetches and displays users from JSONPlaceholder in a FlatList with pull-to-refresh.

**Acceptance Criteria**:
- [ ] `screens/UsersScreen.tsx` renders a FlatList of `UserCard` components
- [ ] Dispatches `fetchUsers()` on mount
- [ ] Pull-to-refresh with `RefreshControl`
- [ ] Loading spinner during initial fetch
- [ ] Error state with retry button
- [ ] Empty state component when no results
- [ ] Tapping a card navigates to `UserDetail` with `userId` param

---

#### TV-27: Implement User Detail Screen

**Labels**: `type:feature`, `type:frontend`, `priority:medium`
**Milestone**: M7

**Description**:
Build the user detail screen that shows full user information fetched by ID.

**Acceptance Criteria**:
- [ ] `screens/UserDetailScreen.tsx` receives `userId` from route params
- [ ] Dispatches `fetchUserById(userId)` on mount
- [ ] Displays full user profile: name, username, email, phone, website
- [ ] Displays address section (street, city, zipcode)
- [ ] Displays company section (name, catchPhrase, bs)
- [ ] Loading state while fetching
- [ ] Back button in header

---

### Milestone 8 — Tasks Feature (CRUD)

#### TV-28: Build TaskCard reusable component

**Labels**: `type:feature`, `type:frontend`, `area:ui`, `priority:high`
**Milestone**: M8

**Description**:
Create a `TaskCard` component that displays task info with status/priority badges and edit/delete action buttons.

**Acceptance Criteria**:
- [ ] `components/TaskCard.tsx` with typed props
- [ ] Displays: title, description (truncated), created date
- [ ] `StatusBadge` — colored badge showing status (pending/in_progress/done)
- [ ] Priority indicator (colored dot or badge: red=high, amber=medium, green=low)
- [ ] Edit button (navigates to TaskForm with task data)
- [ ] Delete button (triggers confirmation dialog, then dispatches `deleteTask`)

---

#### TV-29: Build StatusBadge reusable component

**Labels**: `type:feature`, `type:frontend`, `area:ui`, `priority:medium`
**Milestone**: M8

**Description**:
Create a generic badge component for displaying task status and priority with appropriate colors.

**Acceptance Criteria**:
- [ ] `components/StatusBadge.tsx` — accepts `label` and `color`/`variant` props
- [ ] Status colors: pending=gray, in_progress=amber, done=green
- [ ] Priority colors: low=green, medium=amber, high=red
- [ ] Rounded pill styling with colored background

---

#### TV-30: Implement Tasks Screen with FlatList and filters

**Labels**: `type:feature`, `type:frontend`, `priority:high`
**Milestone**: M8

**Description**:
Build the Tasks tab screen with a filterable FlatList of tasks fetched from the local API.

**Acceptance Criteria**:
- [ ] `screens/TasksScreen.tsx` renders FlatList of `TaskCard` components
- [ ] Dispatches `fetchTasks()` on mount
- [ ] Filter tabs at the top: All | Pending | In Progress | Done
- [ ] Tapping a filter dispatches `setFilter()` and re-fetches tasks
- [ ] Pull-to-refresh support
- [ ] "+" button in header navigates to TaskForm (create mode)
- [ ] Loading and error states
- [ ] Empty state when no tasks match the filter
- [ ] Confirmation dialog before deleting a task

---

#### TV-31: Implement task deletion with confirmation

**Labels**: `type:feature`, `type:frontend`, `priority:medium`
**Milestone**: M8

**Description**:
When the user taps delete on a TaskCard, show a native Alert confirmation. On confirm, dispatch `deleteTask()`, show a success toast, and refresh the list.

**Acceptance Criteria**:
- [ ] `Alert.alert()` confirmation dialog: "Delete Task?" / "This action cannot be undone."
- [ ] On confirm: dispatch `deleteTask(id)`, handle loading state
- [ ] On success: show toast "Task deleted", refresh task list
- [ ] On error: show error toast

---

### Milestone 9 — Task Form & Validation

#### TV-32: Implement TaskForm Screen (Create mode)

**Labels**: `type:feature`, `type:frontend`, `area:forms`, `priority:high`
**Milestone**: M9

**Description**:
Build the task form screen for creating new tasks. Includes text inputs for title and description, and segmented controls for priority.

**Acceptance Criteria**:
- [ ] `screens/TaskFormScreen.tsx` — form with controlled inputs
- [ ] Title input (required, min 1 char, max 200)
- [ ] Description input (multiline, optional)
- [ ] Priority selector (Low / Medium / High) — segmented control or button group
- [ ] "Save Task" button at the bottom
- [ ] Header title: "New Task"
- [ ] `KeyboardAvoidingView` wrapping the form
- [ ] On save: dispatch `createTask()`, navigate back on success

---

#### TV-33: Extend TaskForm for Edit mode

**Labels**: `type:feature`, `type:frontend`, `area:forms`, `priority:high`
**Milestone**: M9

**Description**:
Extend the TaskForm screen to support editing an existing task. When a `task` object is passed via route params, pre-fill the form and show the status selector.

**Acceptance Criteria**:
- [ ] Detect edit mode from `route.params.task`
- [ ] Pre-fill all form fields with existing task data
- [ ] Show Status selector (Pending / In Progress / Done) — only in edit mode
- [ ] Header title: "Edit Task" when editing
- [ ] On save: dispatch `updateTask({id, data})`, navigate back on success
- [ ] "Save" button label changes to "Update Task" in edit mode

---

#### TV-34: Implement form validation with error messages

**Labels**: `type:feature`, `type:frontend`, `area:forms`, `priority:medium`
**Milestone**: M9

**Description**:
Add client-side validation to the task form with inline error messages.

**Acceptance Criteria**:
- [ ] Title is required — show "Title is required" error below input
- [ ] Title max length enforced (200 chars)
- [ ] Error messages appear on submit attempt, not while typing
- [ ] Error clears when user starts typing in that field
- [ ] Submit button disabled during API call (prevent double-submit)
- [ ] Form inputs styled with error state (red border)

---

### Milestone 10 — Settings, Polish & Documentation

#### TV-35: Build LoadingOverlay global component

**Labels**: `type:feature`, `type:frontend`, `area:ui`, `priority:medium`
**Milestone**: M10

**Description**:
Create a full-screen semi-transparent loading overlay that can be triggered globally from the UI slice.

**Acceptance Criteria**:
- [ ] `components/LoadingOverlay.tsx` — full-screen overlay with spinner
- [ ] Connected to `ui.globalLoading` from Redux
- [ ] Rendered at the root level of the app (always on top)
- [ ] Semi-transparent dark background
- [ ] `ActivityIndicator` centered

---

#### TV-36: Build ErrorBanner component

**Labels**: `type:feature`, `type:frontend`, `area:ui`, `priority:medium`
**Milestone**: M10

**Description**:
Create a reusable error banner that displays error messages with a retry action.

**Acceptance Criteria**:
- [ ] `components/ErrorBanner.tsx` — displays error message
- [ ] "Retry" button that calls the provided `onRetry` callback
- [ ] Red/error-themed styling
- [ ] Dismissible (optional close button)

---

#### TV-37: Build EmptyState component

**Labels**: `type:feature`, `type:frontend`, `area:ui`, `priority:low`
**Milestone**: M10

**Description**:
Create a reusable empty state component for when lists have no data.

**Acceptance Criteria**:
- [ ] `components/EmptyState.tsx` — icon + title + subtitle
- [ ] Accepts `icon`, `title`, `subtitle` props
- [ ] Centered layout with appropriate spacing
- [ ] Used in UsersScreen and TasksScreen empty states

---

#### TV-38: Implement Settings Screen

**Labels**: `type:feature`, `type:frontend`, `priority:medium`
**Milestone**: M10

**Description**:
Build the Settings tab screen with app info and utility actions.

**Acceptance Criteria**:
- [ ] `screens/SettingsScreen.tsx` with sections:
  - App Info: version, author
  - API: current backend URL, health check status
  - Storage: clear AsyncStorage button
  - Theme: light/dark toggle (dispatches `toggleTheme`)
- [ ] Settings stored in AsyncStorage (persist theme preference)
- [ ] "Clear All Data" with confirmation dialog

---

#### TV-39: Integrate AsyncStorage for settings persistence

**Labels**: `type:feature`, `type:frontend`, `priority:medium`
**Milestone**: M10

**Description**:
Create AsyncStorage utility helpers and use them to persist the user's theme preference across app restarts.

**Acceptance Criteria**:
- [ ] `utils/storage.ts` — helper functions: `getItem`, `setItem`, `removeItem`, `clear`
- [ ] Theme preference saved on toggle
- [ ] Theme loaded from storage on app start (in splash screen)
- [ ] Settings screen "Clear All Data" uses `storage.clear()`

---

#### TV-40: Wire up root App.tsx with Provider and Navigation

**Labels**: `type:feature`, `type:frontend`, `priority:high`
**Milestone**: M10

**Description**:
Ensure the root `App.tsx` properly wraps the app with Redux Provider, Navigation Container, and LoadingOverlay.

**Acceptance Criteria**:
- [ ] Redux `<Provider>` wrapping the app
- [ ] `<AppNavigator>` inside the provider
- [ ] `<LoadingOverlay>` rendered at root level
- [ ] App launches cleanly from splash → tabs

---

#### TV-41: End-to-end manual testing pass

**Labels**: `type:test`, `priority:high`
**Milestone**: M10

**Description**:
Perform a complete manual test of all features to ensure everything works together.

**Test Checklist**:
- [ ] App launches → splash → main tabs
- [ ] Users tab: list loads, pull-to-refresh works, tap navigates to detail
- [ ] User detail: full info displayed, back navigation works
- [ ] Tasks tab: list loads from backend, filter tabs work
- [ ] Create task: tap +, fill form, save → appears in list
- [ ] Edit task: tap edit, form pre-filled, update → reflected in list
- [ ] Delete task: tap delete, confirm → removed from list
- [ ] Settings: theme toggle, clear data, health check
- [ ] Error states: stop backend, verify error UI shows
- [ ] Loading states: visible during API calls

---

#### TV-42: Final documentation and skills checklist

**Labels**: `type:docs`, `priority:medium`
**Milestone**: M10

**Description**:
Update all documentation, verify README is accurate, and complete the skills checklist.

**Acceptance Criteria**:
- [ ] README.md reflects final project state
- [ ] All code is commented where non-obvious
- [ ] Skills checklist in design doc is fully checked off
- [ ] Project is presentable as a portfolio piece

---

## Task Dependency Graph

```
TV-01 (repo init)
  ├── TV-02 (docker-compose)
  │     └── TV-03 (Dockerfile + pyproject)
  │           └── TV-05 (database layer)
  │                 ├── TV-06 (seed data)
  │                 └── TV-07 (FastAPI entry)
  │                       └── TV-08 (CRUD routes)
  │                             └── TV-09 (verify backend)
  │
  ├── TV-04 (README)
  │
  └── TV-10 (RN init)
        └── TV-11 (install deps)
              ├── TV-12 (path aliases)
              ├── TV-13 (folder structure + themes)
              │     └── TV-14 (TypeScript types)
              │
              ├── TV-15 (Tab Navigator)
              │     └── TV-16 (Stack Navigator)
              │           ├── TV-17 (nav types)
              │           └── TV-18 (Splash Screen)
              │
              ├── TV-19 (Redux store)
              │     ├── TV-20 (Users slice)
              │     ├── TV-21 (Tasks slice)
              │     └── TV-22 (UI slice)
              │
              └── TV-23 (Axios clients)
                    └── TV-24 (API endpoints)
                          │
                          ├── TV-25 (UserCard)
                          │     └── TV-26 (Users Screen)
                          │           └── TV-27 (User Detail)
                          │
                          ├── TV-28 (TaskCard)
                          │     ├── TV-29 (StatusBadge)
                          │     └── TV-30 (Tasks Screen)
                          │           └── TV-31 (Delete task)
                          │
                          ├── TV-32 (TaskForm create)
                          │     ├── TV-33 (TaskForm edit)
                          │     └── TV-34 (Form validation)
                          │
                          ├── TV-35 (LoadingOverlay)
                          ├── TV-36 (ErrorBanner)
                          ├── TV-37 (EmptyState)
                          │
                          ├── TV-38 (Settings Screen)
                          │     └── TV-39 (AsyncStorage)
                          │
                          └── TV-40 (Wire App.tsx)
                                └── TV-41 (E2E testing)
                                      └── TV-42 (Final docs)
```

---

## Summary

| Milestone | Tasks       | Estimated Time |
|-----------|-------------|----------------|
| M1        | TV-01 → 04  | 2–3 hours      |
| M2        | TV-05 → 09  | 3–4 hours      |
| M3        | TV-10 → 14  | 2–3 hours      |
| M4        | TV-15 → 18  | 2–3 hours      |
| M5        | TV-19 → 22  | 3–4 hours      |
| M6        | TV-23 → 24  | 1–2 hours      |
| M7        | TV-25 → 27  | 3–4 hours      |
| M8        | TV-28 → 31  | 3–4 hours      |
| M9        | TV-32 → 34  | 3–4 hours      |
| M10       | TV-35 → 42  | 4–5 hours      |
| **Total** | **42 tasks**| **~3 days**    |
