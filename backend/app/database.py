import os

from sqlmodel import Session, SQLModel, create_engine, select, func

DB_PATH = os.environ.get("DB_PATH", "./data/taskvault.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
    """Create all tables defined by SQLModel subclasses."""
    SQLModel.metadata.create_all(engine)
    _seed_if_empty()


def get_session():
    """FastAPI dependency — yields a DB session per request."""
    with Session(engine) as session:
        yield session


def _seed_if_empty():
    """Insert seed data if the tasks table is empty."""
    from app.models import Task
    from app.seed import SEED_TASKS

    with Session(engine) as session:
        count = session.exec(select(func.count()).select_from(Task)).one()
        if count == 0:
            for task in SEED_TASKS:
                session.add(task)
            session.commit()
