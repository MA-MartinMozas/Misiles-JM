function on_request_success(response) {
    console.debug('response', response);
}

function on_request_error(r, text_status, error_thrown) {
    console.debug('error', text_status + ", " + error_thrown + ":\n" + r.responseText);
}

var request = { ... };
jQuery.ajax({
    url: 'http://host/whatever.cgi',
    type: 'POST',
    cache: false,
    data: JSON.stringify(request),
    contentType: 'application/json',
    processData: false,
    success: on_request_success,
    error: on_request_error
});
//para python
// request = json.load(sys.stdin)
// response = handle_request(request)
// print("Content-Type: application/json", end="\n\n")
// json.dump(response, sys.stdout, indent=2)
