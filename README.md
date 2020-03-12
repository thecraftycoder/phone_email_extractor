# The Extractor

![Sarah Connor](https://cdn.vox-cdn.com/thumbor/80cX0s7Y6ID0iHU0KvH_pPrEE3k=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/16294722/phx03489r.jpg "Sarah Connor")

Phone and email extractor using regex &amp; python.

## Without Regex

The [isPhoneNumber()](wo_regex/isPhoneNumber.py) function works but is limited; it can only find one pattern of phone numbers.

Edge cases:
- 415.555.4242
- (415) 555-4242
- 415-555-4242 x 99

Function isPhoneNumber() would fail to validate the above edge cases. You can add more code but there is an easier way.
