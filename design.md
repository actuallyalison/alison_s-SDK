# Design

This SDK uses a helper function get_api to shorten all other methods and to allow direct API 
access to endpoints not already included in the SDK

The main API endpoints are grouped into a single function per entity type with optional parameters,
for example book() takes optional arguments for book_id and get_chapters to cover all /book API calls.

The tests are just pass/fail using a custom helper function rather than a full test library. 
Tests take in the response to an SDK call, a lambda to transform the response, and an expected value.

Not yet implemented due to short available time: sorting, paging and filtering.
This would be handled similarly by simply adding additional optional arguments to the existing methods.


