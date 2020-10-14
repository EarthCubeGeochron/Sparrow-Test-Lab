from sparrow.plugins import SparrowPlugin
from sparrow.database import User, on_conflict
from json import load
from os import path


class TestInitPlugin(SparrowPlugin):
    name = "test-init"

    def on_database_ready(self, db):
        # Create a user directly in the database
        with on_conflict("do-nothing"):
            user = User(username="Test")
            user.set_password("Test")
            db.session.add(user)
            db.session.commit()

    def on_load_complete(self):
        db = self.app.database
        fn = path.abspath(
            path.join(path.dirname(__file__), "test-data", "project-1.json")
        )
        with open(fn, "r") as f:
            json_data = load(f)
        db.load_data("project", json_data["data"])
