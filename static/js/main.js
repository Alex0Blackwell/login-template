$("form[name=signup_form]").submit(function(e) {
  var $form = $(this);
  var $error = $form.find(".error");

  // Get all the fields of the form to send them to the backend
  var data = $form.serialize();

  // send to the backend (/user/signup) with ajax
  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "Json",

    success: function(resp) {
      console.log(resp);
    },

    error: function(resp) {
      console.log(resp);
    }
  });

  e.preventDefault();
});
