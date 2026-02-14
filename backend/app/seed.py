from app.models import Task, TaskPriority, TaskStatus

SEED_TASKS = [
    Task(
        title="Learn React Native Core",
        description="Study View, Text, FlatList, StyleSheet",
        status=TaskStatus.in_progress,
        priority=TaskPriority.high,
    ),
    Task(
        title="Set up Redux Toolkit",
        description="Configure store, create slices",
        status=TaskStatus.pending,
        priority=TaskPriority.high,
    ),
    Task(
        title="Build API layer with Axios",
        description="Create instance, add interceptors",
        status=TaskStatus.pending,
        priority=TaskPriority.medium,
    ),
    Task(
        title="Practice navigation",
        description="Stack + Tab navigation patterns",
        status=TaskStatus.pending,
        priority=TaskPriority.medium,
    ),
    Task(
        title="Study Firebase docs",
        description="FCM setup and notification handling",
        status=TaskStatus.done,
        priority=TaskPriority.low,
    ),
]
