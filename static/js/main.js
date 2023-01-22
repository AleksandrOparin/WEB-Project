$(".like-question-btn-up").on('click', function (ev) {
    const request = new Request('http://127.0.0.1:8000/likequestion/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body: 'question_id=' + $(this).data('id'),
        }
    )

    fetch(request).then(
        response_raw => response_raw.json().then(
            response_json => {
                $('.like-count[data-id=' + response_json.question_id + ']').text(response_json.likes_count);

                $(this).addClass("active");
                $('.like-question-btn-down[data-id=' + response_json.question_id + ']').removeClass("active");
            }
        )
    );
})


$(".like-question-btn-down").on('click', function (ev) {
    const request = new Request('http://127.0.0.1:8000/dislikequestion/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body: 'question_id=' + $(this).data('id'),
        }
    )

    fetch(request).then(
        response_raw => response_raw.json().then(
            response_json => {
                $('.like-count[data-id=' + response_json.question_id + ']').text(response_json.likes_count);

                $(this).addClass("active");
                $('.like-question-btn-up[data-id=' + response_json.question_id + ']').removeClass("active");
            }
        )
    );
})


$(".like-answer-btn-up").on('click', function (ev) {
    const request = new Request('http://127.0.0.1:8000/likeanswer/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body: 'answer_id=' + $(this).data('id'),
        }
    )

    fetch(request).then(
        response_raw => response_raw.json().then(
            response_json => {
                $('.like-count[data-id=' + response_json.answer_id + ']').text(response_json.likes_count);

                $(this).addClass("active");
                $('.like-answer-btn-down[data-id=' + response_json.answer_id + ']').removeClass("active");
            }
        )
    );
})


$(".like-answer-btn-down").on('click', function (ev) {
    const request = new Request('http://127.0.0.1:8000/dislikeanswer/',
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body: 'answer_id=' + $(this).data('id'),
        }
    )

    fetch(request).then(
        response_raw => response_raw.json().then(
            response_json => {
                $('.like-count[data-id=' + response_json.answer_id + ']').text(response_json.likes_count);

                $(this).addClass("active");
                $('.like-answer-btn-up[data-id=' + response_json.answer_id + ']').removeClass("active");
            }
        )
    );
})
