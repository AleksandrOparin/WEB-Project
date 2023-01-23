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


$(".answer-check").change(function (ev) {
    const request = new Request('http://127.0.0.1:8000/correctanswer/',
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
                if (response_json.status) {
                    const new_id = response_json.new_correct_answer_id;
                    const old_id = response_json.old_correct_answer_id;

                    if (response_json.correct) {
                        $('.correct[data-id=' + new_id + ']').append("<i class='fa-solid fa-check fa-2x'></i>");
                    } else {
                        $('.correct[data-id=' + new_id + ']').empty();
                    }

                    if (new_id != old_id) {
                        $('.answer-check[data-id=' + old_id + ']').removeAttr('checked');
                         $('.correct[data-id=' + old_id + ']').empty();
                    }
                }
            }
        )
    );
})
