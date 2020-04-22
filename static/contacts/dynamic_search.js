const search_input = $('#search_input')
const search_content = $('#all_search_content')

const endpoint = ''
const delay_by_in_ms = 300
const fade_delay = 50

let scheduled_function = false
let prev_val = ''

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            search_content.fadeTo(fade_delay, 0).promise().then(() => {
                search_content.html(response['html_from_view'])
                search_content.fadeTo(fade_delay, 1)
            })
        })
}

search_input.on('keyup', function () {

    if ($(this).val() != prev_val)
    {
        prev_val = $(this).val()

        const request_parameters = {
            search: $(this).val()
        }
    
        if (scheduled_function) {
            clearTimeout(scheduled_function)
        }   
        scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
    }
})
