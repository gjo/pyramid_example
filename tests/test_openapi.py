import pytest
import schemathesis


@pytest.fixture(scope="session")
def schema_app(app):
    from example_app.openapi import OAS_PATH

    return schemathesis.from_path(OAS_PATH, app=app)


schema = schemathesis.from_pytest_fixture("schema_app")


@schema.parametrize(method="GET")
def test_get(case):
    response = case.call_wsgi(headers=[])
    case.validate_response(response)
