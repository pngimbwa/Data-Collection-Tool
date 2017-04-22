$(document).ready(function(){
                  $('.timepicker').timepicker({
                      timeFormat: 'HH:mm',
                      //timeFormat: 'H:mm p',
                      interval: 60,
                      minTime: '0',
                      //maxTime: '6:00pm',
                      //defaultTime: '11',
                      //startTime: '10:00',
                      dynamic: false,
                      dropdown: true,
                      scrollbar: true
                  });
              });


$(document).ready(function () {
    $('#addfarmer_form').bootstrapValidator({
        feedbackIcons: {
            //valid: 'glyphicon glyphicon-ok',
            //invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            country: {
                validators: {
                    notEmpty: {
                        message: 'Please select country' }
                        }
                    },
                    
            region: {
                validators: {
                    notEmpty: {
                        message: 'Please select region' }
                        }
                    },
            
            district: {
                validators: {
                    notEmpty: {
                        message: 'Please select district' }
                        }
                    },
            
            village: {
                validators: {
                    notEmpty: {
                        message: 'Please select village' }
                        }
                    },
            group: {
                validators: {
                    notEmpty: {
                        message: 'Please select that a farmer belong' }
                        }
                    },
            farmid: {
                validators: {
                    stringLength: { min: 2 },
                    notEmpty: { message: 'Please supply farm id' }
                }
            },
            farmsize: {
                validators: {
                    //stringLength: { min: 2 },
                    notEmpty: { message: 'Please supply farm size' }
                }
            },
//            cropcategory: {
//                validators: {
//                    //stringLength: { min: 2 },
//                    notEmpty: { message: 'Please supply crop' }
//                }
//            },
            crosp: {
                validators: {
                    //stringLength: { min: 2 },
                    notEmpty: { message: 'Please supply crop' }
                }
            },
            firstname: {
                validators: {
                    stringLength: { min: 2 },
                    notEmpty: { message: 'Please supply first name' }
                }
            },
            lastname: {
                validators: {
                    stringLength: { min: 2 },
                    notEmpty: { message: 'Please supply last name' }
                }
            },
            phone: {
                validators: {
                    notEmpty: { message: 'Please supply your phone number' },
                    phone: {
                        country: 'TZ',
                        message: 'Please supply a vaild phone number with area code'
                    }
                }
            },
            
        pumptype: {
                validators: {
                    notEmpty: {
                        message: 'Please select pump type' }
                        }
                    },
        pipesize: {
                validators: {
                    notEmpty: {
                        message: 'Please select pipe size' }
                        }
                    },
        }
    }).on('success.form.bv', function (e) {
        $('#success_message').slideDown({ opacity: 'show' }, 'slow');
        $('#addfarmer_form').data('bootstrapValidator').resetForm();
        e.preventDefault();
        var $form = $(e.target);
        var bv = $form.data('bootstrapValidator');
        $.post($form.attr('action'), $form.serialize(), function (result) {
            console.log(result);
        }, 'json');
    });
});
      //# sourceURL=pen.js
