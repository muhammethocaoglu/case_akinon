from datetime import datetime

from pytest import raises

from src.core.model.search_exchange_input_model import SearchExchangeInputModel
from src.infra.exception.bad_request_exception import BadRequestException


class TestExchangeService:
    def test_should_raise_bad_request_error_when_search_if_input_is_invalid(
        self, exchange_service
    ):
        # given
        search_exchange_input_model: SearchExchangeInputModel = (
            SearchExchangeInputModel(
                id=1, start_date=datetime.utcnow().date()
            )
        )
        # when
        with raises(BadRequestException) as bad_request_exc:
            exchange_service.search(
                search_exchange_input_model
            )
        # then
        assert bad_request_exc.value.error_code == 2001
