import time
from behave import *
from behave.formatter import null
from utilities.AddResources import *
from utilities.BaseClass import BaseClass
from utilities.configurations import get_endpoint

baseclass = BaseClass()
url = get_endpoint()['API']['get_candle_stick'] + addresourcse.get_candle_stick_path


@given('Request is sent to get-candlestick data with {instrument_name} and {timeframe}')
def step_impl(context, instrument_name, timeframe):
    querystring = {"instrument_name": instrument_name, "timeframe": timeframe}
    context.response = baseclass.getRequest(url, querystring)
    context.candlestick_details = context.response.json()
    context.expected_instrument_name = instrument_name
    context.expected_timeframe = timeframe


@then('response is received with HTTP status code {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode


@then('the response body should return expected details')
def step_impl(context):
    actual_instrument_name = context.candlestick_details['result']['instrument_name']
    actual_timeframe = context.candlestick_details['result']['interval']
    assert actual_instrument_name == context.expected_instrument_name
    assert actual_timeframe == context.expected_timeframe
    candle_stick_data = context.candlestick_details['result']['data']
    for data in candle_stick_data:
        for key, value in data.items():
            assert value is not null


@when('Request is sent to get-candlestick data without instrument_name')
def step_impl(context):
    querystring = {"instrument_name": '', "timeframe": '5m'}
    context.response = baseclass.getRequest(url, querystring)
    context.candlestick_details = context.response.json()


@then('response should contain an error message as "Invalid input"')
def step_impl(context):
    assert context.candlestick_details['message'] == "Invalid input"


@when('Request is sent to get-candlestick data without timeframe')
def step_impl(context):
    querystring = {"instrument_name": 'BTC_USDT', "timeframe": ''}
    context.response = baseclass.getRequest(url, querystring)
    context.candlestick_details = context.response.json()


@then('response should contain an error message as "Timeframe  is not supported"')
def step_impl(context):
    assert context.candlestick_details['message'] == "Timeframe  is not supported."


@when('Request is sent to get-candlestick data without query parameter')
def step_impl(context):
    querystring = {}
    context.response = baseclass.getRequest(url, querystring)
    context.candlestick_details = context.response.json()


@then('response should contain an error message as "Bad Request"')
def step_impl(context):
    assert context.candlestick_details['error'] == "Bad Request"
