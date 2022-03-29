Feature: Validation of get-candlestick endpoint

  Scenario Outline: Retrieve candlestick data using get-candlestick endpoint
    Given Request is sent to get-candlestick data with <instrument_name> and <timeframe>
    Then response is received with HTTP status code 200
    And the response body should return expected details
    Examples:
      | instrument_name | timeframe |
      | BTC_USDT        | 1m        |
      | BTC_USDT        | 5m        |
      | BTC_USDT        | 15m       |
      | BTC_USDT        | 30m       |
      | BTC_USDT        | 1h        |
      | BTC_USDT        | 6h        |
      | BTC_USDT        | 12h       |
      | BTC_USDT        | 1D        |
      | BTC_USDT        | 7D        |
      | BTC_USDT        | 14D       |
      | BTC_USDT        | 1M        |


  Scenario: Validate response when empty instrument_name is passed
    When Request is sent to get-candlestick data without instrument_name
    Then response is received with HTTP status code 200
    And response should contain an error message as "Invalid input"

  Scenario: Validate response when empty timeframe is passed
    When Request is sent to get-candlestick data without timeframe
    Then response is received with HTTP status code 200
    And response should contain an error message as "Timeframe  is not supported"


  Scenario: Validate response when request is sent without mandatory query parameter
    When Request is sent to get-candlestick data without query parameter
    Then response is received with HTTP status code 400
    And response should contain an error message as "Bad Request"






