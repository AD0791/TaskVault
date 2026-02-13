# TaskVault — GitHub Repository & Project Setup Guide

> Step-by-step instructions to create the GitHub repo, configure labels, milestones, and the project board so you can manage TaskVault with GitHub's built-in project management tools.

---

## 1. Create the GitHub Repository

```bash
# Navigate to the TaskVault directory
cd ~/Desktop/PROCODE/TaskVault

# Initialize git (if not already)
git init

# Create the .gitignore
# (we'll create this in the README setup step)

# Initial commit
git add .
git commit -m "chore: initial project structure with docs"

# Create the GitHub repo using the gh CLI
gh repo create TaskVault --public --source=. --remote=origin --push

# Verify
gh repo view --web
```

> **Note**: If you prefer a private repo, replace `--public` with `--private`.

---

## 2. Create Labels

GitHub has default labels, but we want project-specific ones. Run these commands to create them all at once:

```bash
# ========================
# TYPE LABELS
# ========================
gh label create "type:setup"    --color "0E8A16" --description "Project setup and configuration"
gh label create "type:feature"  --color "1D76DB" --description "New feature implementation"
gh label create "type:backend"  --color "D93F0B" --description "Backend / API work"
gh label create "type:frontend" --color "7057FF" --description "React Native / mobile work"
gh label create "type:docs"     --color "0075CA" --description "Documentation"
gh label create "type:devops"   --color "B60205" --description "Docker, CI/CD, deployment"
gh label create "type:test"     --color "FBCA04" --description "Testing"

# ========================
# PRIORITY LABELS
# ========================
gh label create "priority:high"   --color "D93F0B" --description "Must be done first"
gh label create "priority:medium" --color "F9D0C4" --description "Important but not blocking"
gh label create "priority:low"    --color "C5DEF5" --description "Nice to have"

# ========================
# AREA LABELS
# ========================
gh label create "area:navigation" --color "BFD4F2" --description "Navigation related"
gh label create "area:state"      --color "D4C5F9" --description "Redux / state management"
gh label create "area:api"        --color "FEF2C0" --description "API layer / Axios"
gh label create "area:ui"         --color "E6CCB3" --description "UI components and styling"
gh label create "area:forms"      --color "C2E0C6" --description "Form inputs and validation"
```

---

## 3. Create Milestones

```bash
gh api repos/{owner}/{repo}/milestones -f title="M1 — Project Infrastructure"      -f description="Repo init, Docker setup, root config"            -f due_on="2026-02-14T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M2 — Backend API"                  -f description="FastAPI CRUD, SQLModel, seed data"              -f due_on="2026-02-14T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M3 — RN Project Foundation"        -f description="RN init, deps, types, themes"                   -f due_on="2026-02-14T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M4 — Navigation System"            -f description="Stack + Tab navigators, splash screen"          -f due_on="2026-02-15T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M5 — State Management"             -f description="Redux store, slices, async thunks"              -f due_on="2026-02-15T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M6 — API Layer"                    -f description="Axios clients, interceptors, endpoints"         -f due_on="2026-02-15T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M7 — Users Feature"                -f description="Users list, detail, UserCard"                   -f due_on="2026-02-15T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M8 — Tasks Feature"                -f description="Task CRUD list, TaskCard, filters"              -f due_on="2026-02-16T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M9 — Task Form & Validation"       -f description="Create/edit form, validation"                   -f due_on="2026-02-16T00:00:00Z"
gh api repos/{owner}/{repo}/milestones -f title="M10 — Settings, Polish & Docs"     -f description="Settings screen, global UI, final docs"         -f due_on="2026-02-16T00:00:00Z"
```

> **Replace** `{owner}/{repo}` with your actual GitHub username and repo name (e.g., `alexandrod/TaskVault`).

---

## 4. Create GitHub Issues from Task List

Here is a script that creates all 42 issues. **Run this after creating labels and milestones**.

> **Important**: Replace `OWNER/REPO` with your actual values, and update milestone numbers (GitHub assigns them sequentially starting from 1).

```bash
#!/bin/bash
# create-issues.sh
# Run: chmod +x create-issues.sh && ./create-issues.sh

REPO="OWNER/TaskVault"  # ← CHANGE THIS

# ========================
# MILESTONE 1 — Project Infrastructure
# ========================

gh issue create --repo "$REPO" \
  --title "TV-01: Initialize monorepo and Git repository" \
  --label "type:setup,priority:high" \
  --milestone "M1 — Project Infrastructure" \
  --body "$(cat <<'EOF'
## Description
Set up the root TaskVault repository with the monorepo folder structure.

## Acceptance Criteria
- [ ] GitHub repo created: `TaskVault`
- [ ] Root `.gitignore` covers both Python and React Native artifacts
- [ ] Folder structure established: `mobile/`, `backend/`, `docs/`
- [ ] Initial commit pushed to `main`
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-02: Create root docker-compose.yml" \
  --label "type:devops,type:setup,priority:high" \
  --milestone "M1 — Project Infrastructure" \
  --body "$(cat <<'EOF'
## Description
Create the root-level `docker-compose.yml` that orchestrates the FastAPI server and Adminer DB browser.

## Acceptance Criteria
- [ ] `docker-compose.yml` at project root
- [ ] `api` service defined (build from `./backend`, port 8000)
- [ ] `adminer` service defined (port 8080)
- [ ] Volume mounts for SQLite persistence and hot-reload
- [ ] Environment variables for DB path

**Reference**: See project design doc § 4 — Docker Architecture
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-03: Create backend Dockerfile and Python project config" \
  --label "type:devops,type:backend,priority:high" \
  --milestone "M1 — Project Infrastructure" \
  --body "$(cat <<'EOF'
## Description
Create `backend/Dockerfile` using Python 3.12-slim with uv package manager, and `backend/pyproject.toml` with all required dependencies.

## Acceptance Criteria
- [ ] `backend/Dockerfile` created (Python 3.12-slim, uv, uvicorn with --reload)
- [ ] `backend/pyproject.toml` with all dependencies and versions
- [ ] `uv.lock` generated and committed
- [ ] `docker compose build` succeeds without errors
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-04: Write root README.md with launch and deployment instructions" \
  --label "type:docs,priority:medium" \
  --milestone "M1 — Project Infrastructure" \
  --body "$(cat <<'EOF'
## Description
Write a comprehensive README that explains the monorepo structure, prerequisites, how to launch the backend and frontend, and deployment notes.

## Acceptance Criteria
- [ ] Project overview and architecture summary
- [ ] Prerequisites section (Docker, Node, Android SDK, etc.)
- [ ] Step-by-step backend launch instructions
- [ ] Step-by-step frontend launch instructions
- [ ] Port forwarding notes for physical devices
- [ ] Deployment section
EOF
)"

# ========================
# MILESTONE 2 — Backend API
# ========================

gh issue create --repo "$REPO" \
  --title "TV-05: Implement SQLModel database layer" \
  --label "type:backend,priority:high" \
  --milestone "M2 — Backend API" \
  --body "$(cat <<'EOF'
## Description
Create the database module with SQLModel engine, session dependency, and table creation logic. Implement the Task model and request schemas.

## Acceptance Criteria
- [ ] `backend/app/database.py` — engine, `create_db_and_tables()`, `get_session()`
- [ ] `backend/app/models.py` — `Task` table model, `TaskCreate`, `TaskUpdate` schemas
- [ ] `TaskStatus` enum: pending, in_progress, done
- [ ] `TaskPriority` enum: low, medium, high
- [ ] Table auto-creates on startup
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-06: Implement seed data module" \
  --label "type:backend,priority:medium" \
  --milestone "M2 — Backend API" \
  --body "$(cat <<'EOF'
## Description
Create seed data that is inserted on first startup when the tasks table is empty.

## Acceptance Criteria
- [ ] `backend/app/seed.py` with `SEED_TASKS` list (5 tasks)
- [ ] Seed only runs when table is empty (idempotent)
- [ ] Mix of statuses and priorities
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-07: Implement FastAPI app entry point with CORS and lifespan" \
  --label "type:backend,priority:high" \
  --milestone "M2 — Backend API" \
  --body "$(cat <<'EOF'
## Description
Create the FastAPI application entry point with CORS middleware, lifespan handler for DB init, and health check endpoint.

## Acceptance Criteria
- [ ] `backend/app/main.py` with FastAPI app instance
- [ ] CORS middleware allowing all origins
- [ ] Lifespan handler that calls `create_db_and_tables()` on startup
- [ ] `GET /api/health` returns `{"status": "ok", "service": "taskvault-api"}`
- [ ] Swagger UI accessible at `/docs`
- [ ] ReDoc accessible at `/redoc`
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-08: Implement CRUD route handlers for tasks" \
  --label "type:backend,type:feature,priority:high" \
  --milestone "M2 — Backend API" \
  --body "$(cat <<'EOF'
## Description
Create the tasks router with all CRUD endpoints: list (with filters + pagination), get by ID, create, update (partial), and delete.

## Acceptance Criteria
- [ ] `GET /api/tasks` — list all with `{success, data, pagination}`
- [ ] Filter support: `?status=`, `?priority=`, `?search=`
- [ ] Pagination: `?page=1&limit=10`
- [ ] `GET /api/tasks/{id}` — single task (404 if not found)
- [ ] `POST /api/tasks` — create (201 response)
- [ ] `PUT /api/tasks/{id}` — partial update
- [ ] `DELETE /api/tasks/{id}` — delete (404 if not found)
- [ ] All endpoints tested via Swagger UI
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-09: Verify full backend with Docker" \
  --label "type:backend,type:devops,priority:high" \
  --milestone "M2 — Backend API" \
  --body "$(cat <<'EOF'
## Description
Bring up the full Docker environment, verify all endpoints work, and confirm Adminer can browse the database.

## Acceptance Criteria
- [ ] `docker compose up -d` starts both services cleanly
- [ ] Swagger UI at `http://localhost:8000/docs` works
- [ ] Adminer at `http://localhost:8080` can see task table
- [ ] Hot reload works (edit Python → changes reflected)
- [ ] Data persists across restarts
EOF
)"

# ========================
# MILESTONE 3 — RN Project Foundation
# ========================

gh issue create --repo "$REPO" \
  --title "TV-10: Initialize React Native CLI project with TypeScript" \
  --label "type:setup,type:frontend,priority:high" \
  --milestone "M3 — RN Project Foundation" \
  --body "$(cat <<'EOF'
## Description
Create the React Native project inside `mobile/` using the CLI with TypeScript template. Verify it runs on Android.

## Acceptance Criteria
- [ ] RN project initialized in `mobile/` folder
- [ ] TypeScript template used
- [ ] `npx react-native run-android` succeeds
- [ ] Default app renders on emulator/device
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-11: Install all project dependencies" \
  --label "type:setup,type:frontend,priority:high" \
  --milestone "M3 — RN Project Foundation" \
  --body "$(cat <<'EOF'
## Description
Install all required npm packages.

## Packages
- Navigation: @react-navigation/native, stack, bottom-tabs, screens, safe-area-context, gesture-handler
- State: @reduxjs/toolkit, react-redux
- API: axios, @react-native-async-storage/async-storage
- UI: @rneui/themed, @rneui/base, react-native-vector-icons
- Dev: babel-plugin-module-resolver

## Acceptance Criteria
- [ ] All packages installed
- [ ] Android build still succeeds
- [ ] No peer dependency conflicts
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-12: Configure TypeScript path aliases" \
  --label "type:setup,type:frontend,priority:medium" \
  --milestone "M3 — RN Project Foundation" \
  --body "$(cat <<'EOF'
## Description
Set up path aliases in tsconfig.json and babel.config.js.

## Aliases
@screens, @components, @store, @api, @navigation, @themes, @utils, @types

## Acceptance Criteria
- [ ] `tsconfig.json` paths configured
- [ ] `babel.config.js` module-resolver configured
- [ ] Imports using @ aliases resolve correctly
- [ ] TypeScript intellisense works
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-13: Create project folder structure and theme constants" \
  --label "type:setup,type:frontend,priority:medium" \
  --milestone "M3 — RN Project Foundation" \
  --body "$(cat <<'EOF'
## Description
Create the src/ directory structure and implement the theme system.

## Acceptance Criteria
- [ ] All src/ subdirectories created
- [ ] `themes/colors.ts` — complete color palette
- [ ] `themes/typography.ts` — text styles
- [ ] `themes/spacing.ts` — spacing scale
- [ ] `themes/index.ts` — barrel export
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-14: Define TypeScript types for API data" \
  --label "type:frontend,priority:medium" \
  --milestone "M3 — RN Project Foundation" \
  --body "$(cat <<'EOF'
## Description
Create TypeScript interfaces for all data shapes.

## Acceptance Criteria
- [ ] `types/user.ts` — User interface (JSONPlaceholder shape)
- [ ] `types/task.ts` — Task, TaskStatus, TaskPriority
- [ ] `types/api.ts` — ApiResponse<T>, PaginatedResponse<T>, ApiError
EOF
)"

# ========================
# MILESTONE 4 — Navigation System
# ========================

gh issue create --repo "$REPO" \
  --title "TV-15: Implement Tab Navigator with bottom tabs" \
  --label "type:feature,type:frontend,area:navigation,priority:high" \
  --milestone "M4 — Navigation System" \
  --body "$(cat <<'EOF'
## Description
Create the bottom tab navigator with three tabs: Users, Tasks, Settings.

## Acceptance Criteria
- [ ] `TabNavigator.tsx` with three tabs
- [ ] Each tab has an icon
- [ ] Active/inactive styling
- [ ] Tab labels visible
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-16: Implement Stack Navigator with all screens" \
  --label "type:feature,type:frontend,area:navigation,priority:high" \
  --milestone "M4 — Navigation System" \
  --body "$(cat <<'EOF'
## Description
Create the root stack navigator with: Splash, Main (tabs), UserDetail, TaskForm.

## Acceptance Criteria
- [ ] `StackNavigator.tsx` with all screen registrations
- [ ] `AppNavigator.tsx` with NavigationContainer
- [ ] Splash as initial route (no header)
- [ ] UserDetail and TaskForm push on top of tabs
- [ ] Proper transition animations
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-17: Define navigation TypeScript types" \
  --label "type:frontend,area:navigation,priority:medium" \
  --milestone "M4 — Navigation System" \
  --body "$(cat <<'EOF'
## Description
Create typed navigation params for full type safety.

## Acceptance Criteria
- [ ] `RootStackParamList` typed
- [ ] `MainTabParamList` typed
- [ ] Screen prop types exported
- [ ] No `any` types in navigation calls
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-18: Implement Splash Screen with auto-navigation" \
  --label "type:feature,type:frontend,area:navigation,priority:medium" \
  --milestone "M4 — Navigation System" \
  --body "$(cat <<'EOF'
## Description
Create splash screen that auto-navigates to main tabs after a delay.

## Acceptance Criteria
- [ ] Shows "TaskVault" app name with styling
- [ ] Auto-navigates to Main after 2 seconds
- [ ] Uses `navigation.reset()` to prevent back navigation
- [ ] No header visible
EOF
)"

# ========================
# MILESTONE 5 — State Management
# ========================

gh issue create --repo "$REPO" \
  --title "TV-19: Configure Redux store with typed hooks" \
  --label "type:feature,type:frontend,area:state,priority:high" \
  --milestone "M5 — State Management" \
  --body "$(cat <<'EOF'
## Description
Set up Redux store with configureStore and typed hooks.

## Acceptance Criteria
- [ ] `store/index.ts` with all reducers
- [ ] `store/hooks.ts` with useAppSelector and useAppDispatch
- [ ] RootState and AppDispatch types exported
- [ ] Provider wrapping app in root component
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-20: Implement Users slice with async thunks" \
  --label "type:feature,type:frontend,area:state,priority:high" \
  --milestone "M5 — State Management" \
  --body "$(cat <<'EOF'
## Description
Create users slice for fetching data from JSONPlaceholder.

## Acceptance Criteria
- [ ] State: items, selectedUser, loading, error, searchQuery
- [ ] `fetchUsers` thunk — GET /users
- [ ] `fetchUserById` thunk — GET /users/:id
- [ ] extraReducers for pending/fulfilled/rejected
- [ ] setSearchQuery and clearSelectedUser reducers
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-21: Implement Tasks slice with CRUD async thunks" \
  --label "type:feature,type:frontend,area:state,priority:high" \
  --milestone "M5 — State Management" \
  --body "$(cat <<'EOF'
## Description
Create tasks slice for CRUD operations against the local backend.

## Acceptance Criteria
- [ ] State: items, loading, error, filter, pagination
- [ ] fetchTasks thunk with filter/pagination params
- [ ] createTask thunk — POST
- [ ] updateTask thunk — PUT
- [ ] deleteTask thunk — DELETE
- [ ] extraReducers for all async states
- [ ] setFilter reducer
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-22: Implement UI slice for global state" \
  --label "type:feature,type:frontend,area:state,priority:medium" \
  --milestone "M5 — State Management" \
  --body "$(cat <<'EOF'
## Description
Create UI slice for global loading, toast, and theme.

## Acceptance Criteria
- [ ] State: globalLoading, toast, theme
- [ ] Reducers: showLoading, hideLoading, showToast, hideToast, toggleTheme
- [ ] Toast supports: success, error, info, warning types
EOF
)"

# ========================
# MILESTONE 6 — API Layer
# ========================

gh issue create --repo "$REPO" \
  --title "TV-23: Create Axios client instances with interceptors" \
  --label "type:feature,type:frontend,area:api,priority:high" \
  --milestone "M6 — API Layer" \
  --body "$(cat <<'EOF'
## Description
Set up publicApi (JSONPlaceholder) and localApi (Docker backend) Axios instances with interceptors.

## Acceptance Criteria
- [ ] `api/client.ts` with both instances
- [ ] Platform-aware base URL for localApi
- [ ] Request interceptor: logs method + URL
- [ ] Response interceptor: normalizes errors
- [ ] 10s timeout configured
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-24: Create API endpoint constants and service functions" \
  --label "type:feature,type:frontend,area:api,priority:medium" \
  --milestone "M6 — API Layer" \
  --body "$(cat <<'EOF'
## Description
Define endpoint constants and typed service functions.

## Acceptance Criteria
- [ ] `api/endpoints.ts` with URL constants
- [ ] `api/index.ts` barrel export
- [ ] Typed return values
- [ ] Consistent error handling
EOF
)"

# ========================
# MILESTONE 7 — Users Feature
# ========================

gh issue create --repo "$REPO" \
  --title "TV-25: Build UserCard reusable component" \
  --label "type:feature,type:frontend,area:ui,priority:high" \
  --milestone "M7 — Users Feature" \
  --body "$(cat <<'EOF'
## Description
Create UserCard showing name, username, email, company with navigation chevron.

## Acceptance Criteria
- [ ] Typed props interface
- [ ] Displays name, @username, email, company
- [ ] Right chevron arrow
- [ ] Card styling with shadows
- [ ] onPress callback prop
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-26: Implement Users Screen with FlatList" \
  --label "type:feature,type:frontend,priority:high" \
  --milestone "M7 — Users Feature" \
  --body "$(cat <<'EOF'
## Description
Build Users tab with FlatList, pull-to-refresh, loading/error states.

## Acceptance Criteria
- [ ] FlatList of UserCard components
- [ ] Dispatches fetchUsers() on mount
- [ ] Pull-to-refresh
- [ ] Loading spinner on first fetch
- [ ] Error state with retry
- [ ] Empty state component
- [ ] Tap navigates to UserDetail
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-27: Implement User Detail Screen" \
  --label "type:feature,type:frontend,priority:medium" \
  --milestone "M7 — Users Feature" \
  --body "$(cat <<'EOF'
## Description
Show full user profile fetched by ID.

## Acceptance Criteria
- [ ] Receives userId from route params
- [ ] Full profile: name, username, email, phone, website
- [ ] Address section
- [ ] Company section
- [ ] Loading state
- [ ] Back navigation
EOF
)"

# ========================
# MILESTONE 8 — Tasks Feature
# ========================

gh issue create --repo "$REPO" \
  --title "TV-28: Build TaskCard reusable component" \
  --label "type:feature,type:frontend,area:ui,priority:high" \
  --milestone "M8 — Tasks Feature" \
  --body "$(cat <<'EOF'
## Description
Create TaskCard with status/priority badges and edit/delete actions.

## Acceptance Criteria
- [ ] Title, description (truncated), date
- [ ] StatusBadge for status
- [ ] Priority indicator (colored)
- [ ] Edit button → TaskForm with data
- [ ] Delete button → confirmation dialog
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-29: Build StatusBadge reusable component" \
  --label "type:feature,type:frontend,area:ui,priority:medium" \
  --milestone "M8 — Tasks Feature" \
  --body "$(cat <<'EOF'
## Description
Generic colored badge for status and priority display.

## Acceptance Criteria
- [ ] Accepts label and color/variant props
- [ ] Status colors: pending=gray, in_progress=amber, done=green
- [ ] Priority colors: low=green, medium=amber, high=red
- [ ] Rounded pill styling
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-30: Implement Tasks Screen with FlatList and filters" \
  --label "type:feature,type:frontend,priority:high" \
  --milestone "M8 — Tasks Feature" \
  --body "$(cat <<'EOF'
## Description
Tasks tab with filterable FlatList fetching from local API.

## Acceptance Criteria
- [ ] FlatList of TaskCard components
- [ ] Fetches tasks on mount
- [ ] Filter tabs: All | Pending | In Progress | Done
- [ ] Pull-to-refresh
- [ ] "+" button navigates to TaskForm (create)
- [ ] Loading, error, empty states
- [ ] Delete confirmation dialog
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-31: Implement task deletion with confirmation" \
  --label "type:feature,type:frontend,priority:medium" \
  --milestone "M8 — Tasks Feature" \
  --body "$(cat <<'EOF'
## Description
Delete flow: tap delete → confirm → dispatch → toast → refresh.

## Acceptance Criteria
- [ ] Alert.alert confirmation
- [ ] Dispatch deleteTask(id)
- [ ] Success toast
- [ ] Error handling
- [ ] List refresh after delete
EOF
)"

# ========================
# MILESTONE 9 — Task Form
# ========================

gh issue create --repo "$REPO" \
  --title "TV-32: Implement TaskForm Screen (Create mode)" \
  --label "type:feature,type:frontend,area:forms,priority:high" \
  --milestone "M9 — Task Form & Validation" \
  --body "$(cat <<'EOF'
## Description
Task form for creating new tasks with title, description, priority.

## Acceptance Criteria
- [ ] Controlled form inputs
- [ ] Title input (required, max 200)
- [ ] Description input (multiline)
- [ ] Priority selector (segmented)
- [ ] KeyboardAvoidingView
- [ ] Save dispatches createTask(), navigates back
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-33: Extend TaskForm for Edit mode" \
  --label "type:feature,type:frontend,area:forms,priority:high" \
  --milestone "M9 — Task Form & Validation" \
  --body "$(cat <<'EOF'
## Description
Edit mode: detect task in route params, pre-fill form, add status selector.

## Acceptance Criteria
- [ ] Detect edit mode from route.params.task
- [ ] Pre-fill all fields
- [ ] Status selector (only in edit mode)
- [ ] Header: "Edit Task"
- [ ] Save dispatches updateTask()
- [ ] Button label: "Update Task"
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-34: Implement form validation with error messages" \
  --label "type:feature,type:frontend,area:forms,priority:medium" \
  --milestone "M9 — Task Form & Validation" \
  --body "$(cat <<'EOF'
## Description
Client-side validation with inline error messages.

## Acceptance Criteria
- [ ] Title required error
- [ ] Max length enforced
- [ ] Errors shown on submit, not while typing
- [ ] Error clears when user types
- [ ] Submit button disabled during API call
- [ ] Red border on error fields
EOF
)"

# ========================
# MILESTONE 10 — Polish & Docs
# ========================

gh issue create --repo "$REPO" \
  --title "TV-35: Build LoadingOverlay global component" \
  --label "type:feature,type:frontend,area:ui,priority:medium" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Description
Full-screen loading overlay connected to Redux UI slice.

## Acceptance Criteria
- [ ] Full-screen semi-transparent overlay
- [ ] Connected to ui.globalLoading
- [ ] Rendered at root level
- [ ] ActivityIndicator centered
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-36: Build ErrorBanner component" \
  --label "type:feature,type:frontend,area:ui,priority:medium" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Description
Reusable error banner with retry action.

## Acceptance Criteria
- [ ] Displays error message
- [ ] Retry button with onRetry callback
- [ ] Red/error styling
- [ ] Optional dismiss button
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-37: Build EmptyState component" \
  --label "type:feature,type:frontend,area:ui,priority:low" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Description
Reusable empty state with icon, title, subtitle.

## Acceptance Criteria
- [ ] Accepts icon, title, subtitle props
- [ ] Centered layout
- [ ] Used in Users and Tasks screens
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-38: Implement Settings Screen" \
  --label "type:feature,type:frontend,priority:medium" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Description
Settings tab with app info, API health, storage controls, theme toggle.

## Acceptance Criteria
- [ ] App Info section
- [ ] API health check display
- [ ] Clear AsyncStorage button
- [ ] Theme toggle
- [ ] "Clear All Data" with confirmation
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-39: Integrate AsyncStorage for settings persistence" \
  --label "type:feature,type:frontend,priority:medium" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Description
AsyncStorage helpers and theme persistence.

## Acceptance Criteria
- [ ] `utils/storage.ts` helpers
- [ ] Theme saved on toggle
- [ ] Theme loaded on app start
- [ ] Clear All Data works
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-40: Wire up root App.tsx with Provider and Navigation" \
  --label "type:feature,type:frontend,priority:high" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Description
Root App.tsx with Redux Provider, Navigation, and LoadingOverlay.

## Acceptance Criteria
- [ ] Redux Provider wrapping app
- [ ] AppNavigator inside provider
- [ ] LoadingOverlay at root level
- [ ] Clean launch: splash → tabs
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-41: End-to-end manual testing pass" \
  --label "type:test,priority:high" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Test Checklist
- [ ] App launches → splash → main tabs
- [ ] Users tab: list loads, pull-to-refresh, tap → detail
- [ ] User detail: full info, back navigation
- [ ] Tasks tab: list loads, filter tabs work
- [ ] Create task: +, fill form, save → in list
- [ ] Edit task: edit, pre-filled, update → reflected
- [ ] Delete task: confirm → removed
- [ ] Settings: theme toggle, clear data, health check
- [ ] Error states: stop backend → error UI
- [ ] Loading states visible during API calls
EOF
)"

gh issue create --repo "$REPO" \
  --title "TV-42: Final documentation and skills checklist" \
  --label "type:docs,priority:medium" \
  --milestone "M10 — Settings, Polish & Docs" \
  --body "$(cat <<'EOF'
## Description
Final documentation pass and skills verification.

## Acceptance Criteria
- [ ] README.md reflects final state
- [ ] Code commented where non-obvious
- [ ] Skills checklist fully checked off
- [ ] Project presentable as portfolio piece
EOF
)"

echo "✅ All 42 issues created!"
```

---

## 5. Create GitHub Project Board

```bash
# Create a GitHub Project (V2 — new style)
gh project create --owner "@me" --title "TaskVault Development" --format "board"

# The board will be created with default columns: Todo, In Progress, Done
# You can customize columns via the web UI at:
# https://github.com/users/YOUR_USERNAME/projects/N/settings
```

### Recommended Board Columns

| Column         | Description                        |
|----------------|------------------------------------|
| **Backlog**    | All tasks not yet started          |
| **Ready**      | Reviewed and ready to pick up      |
| **In Progress**| Currently being worked on          |
| **In Review**  | Code written, needs self-review    |
| **Done**       | Completed and merged               |

### Adding Issues to the Project

After creating the project, link all issues to it:

```bash
# List your project number
gh project list --owner "@me"

# Add all open issues to the project (replace PROJECT_NUMBER)
gh issue list --repo "OWNER/TaskVault" --state open --json number -q '.[].number' | \
  xargs -I {} gh project item-add PROJECT_NUMBER --owner "@me" --url "https://github.com/OWNER/TaskVault/issues/{}"
```

---

## 6. Git Branch Strategy

For each task, create a branch from `main`:

```bash
# Pattern: feature/TV-XX-short-description
git checkout main
git pull
git checkout -b feature/TV-01-init-monorepo

# Work on the task...
git add .
git commit -m "feat(TV-01): initialize monorepo structure"
git push -u origin feature/TV-01-init-monorepo

# Create PR (auto-links to issue if you reference it)
gh pr create --title "TV-01: Initialize monorepo and Git repository" \
  --body "Closes #1" \
  --base main
```

### Commit Message Convention

```
type(TV-XX): description

Types:
  feat     — New feature
  fix      — Bug fix
  chore    — Setup/config/tooling
  docs     — Documentation
  refactor — Code restructure (no behavior change)
  style    — Formatting, no logic change
  test     — Adding tests
```

---

## Quick Reference

```bash
# View all issues
gh issue list --repo "OWNER/TaskVault"

# View issues by milestone
gh issue list --repo "OWNER/TaskVault" --milestone "M2 — Backend API"

# View project board in browser
gh project view PROJECT_NUMBER --owner "@me" --web

# Close an issue
gh issue close ISSUE_NUMBER --repo "OWNER/TaskVault"
```
