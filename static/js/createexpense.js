let RECURRING_CHECKBOX = '#recurring-checkbox';

$('#id_start_date').change(function(event) {
    if ($(RECURRING_CHECKBOX).is(":checked")) {
        let date = new Date($(this).val());
        console.log(date.getDate());
    }
});

$(RECURRING_CHECKBOX).click(function() {
    let recurrenceWrapper = $('#recurrences-wrapper');
    if (recurrenceWrapper.css("display") == "none") {
        recurrenceWrapper.css("display", "");
        $('#id_recurrences').val(1);
    } else {
        recurrenceWrapper.css("display", "none");
        $('#id_recurrences').val(0);
    }
});

$('#id_recurrences').change(function(event) {
    if ($('#recurrences-wrapper').css("display)") != "none") {
        if ($(this).val() < 1) {
            $(this).val(1)
        }
    }
});