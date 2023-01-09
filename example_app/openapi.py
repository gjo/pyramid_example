from pathlib import Path

from openapi_core.validation.request.datatypes import RequestValidationResult
from pyramid.config import Configurator
from pyramid.request import Request

OAS_PATH = Path(__file__).absolute().parent / "openapi.yaml"


def validated_params(request: Request) -> RequestValidationResult:
    return request.openapi_validated


def includeme(config: Configurator) -> None:
    config.pyramid_openapi3_spec(str(OAS_PATH))
