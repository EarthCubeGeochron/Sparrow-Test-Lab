from sparrow.plugins import SparrowPlugin
from sparrow.database import User, on_conflict
from json import load
from os import path

_test_data = path.abspath(
    path.join(path.dirname(__file__), "test-data", "project-1.json")
)


class TestInitPlugin(SparrowPlugin):
    """A plugin to initialize a test dataset"""

    name = "test-init"

    def on_database_ready(self, db):
        # Create a user directly in the database
        with on_conflict("do-nothing"):
            user = User(username="Test")
            user.set_password("Test")
            db.session.add(user)
            db.session.commit()

    def on_load_complete(self):
        ## Todo: running importers on app lifecycle methods is a bad idea,
        # because we might run the method on several workers in production.
        db = self.app.database
        project_count = db.session.query(db.model.project).count()
        if project_count > 0:
            return
        db = self.app.database
        with open(_test_data, "r") as f:
            data = load(f)
        db.load_data("project", data["data"])
