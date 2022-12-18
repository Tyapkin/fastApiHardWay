# import all the models, so that Base has before being
# imported by Alembic
from backend.db.base_class import Base  # noqa
# from backend.models.jobs import Job  # noqa
from backend.models.users import User  # noqa
