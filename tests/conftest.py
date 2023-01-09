import os

import pytest
import sqlalchemy
import webtest
from pyramid.request import Request

if "TESTING_DB_URI" in os.environ:  # pragma: no cover
    TESTING_DB_URI = os.environ["TESTING_DB_URI"]
else:
    TESTING_DB_URI = "mysql+pymysql://test_example_app:test_example_app_pw@127.0.0.1/test_example_app?charset=utf8mb4"  # noqa: E501; black says ok


@pytest.fixture(scope="session")
def db_schema():
    from example_app.db_schemata import Base

    from .factories import make_default_data

    engine = sqlalchemy.create_engine(TESTING_DB_URI)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    make_default_data(engine)
    return engine


@pytest.fixture(scope="session")
def app(db_schema):
    from example_app import app_factory

    testing_settings = {
        "example_app.components..connectors.db_readonly": ".connectors.db_readonly:single_instance",  # noqa: E501; black says ok
        "sqlalchemy.readwrite.url": TESTING_DB_URI,
    }
    return app_factory({}, **testing_settings)


@pytest.fixture(scope="session")
def testapp(app):
    testapp = webtest.TestApp(app)
    testapp.RequestClass = Request
    return testapp
