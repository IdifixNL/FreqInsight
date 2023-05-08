$(document).ready(function() {
  // Hide all sections except the first one
  $(".section:not(:first)").hide();

  // Function to show the section with the given id and hide others
  function showSection(id) {
    $(".section").hide();
    $("#" + id).show();
  }

  // Event listeners for menu buttons
  $('#backtest-btn').click(function() {
    $('.nav-btn').removeClass('active');
    $(this).addClass('active');
    showSection('backtest');
  });

  $('#hyperopt-btn').click(function() {
    $('.nav-btn').removeClass('active');
    $(this).addClass('active');
    showSection('hyperopt');
  });

  $('#datadownload-btn').click(function() {
    $('.nav-btn').removeClass('active');
    $(this).addClass('active');
    showSection('datadownload');
  });

  $('#test-btn').click(function() {
    $('.nav-btn').removeClass('active');
    $(this).addClass('active');
    showSection('test');
  });

  $('#test-section-button').click(function() {
    $.post('/test')
      .done(function(data) {
        var output = JSON.parse(data.raw_output);
        var status = output[0].Status;
        var state = output[0].State;
        $('#test-result').text("Status: " + status + "\nState: " + state);
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        $('#test-result').text('Error: ' + errorThrown);
      });
  });

  $('#configuration-btn').click(function() {
    $('.nav-btn').removeClass('active');
    $(this).addClass('active');
    showSection('configuration');
  });

  $('#help-btn').click(function() {
    $('.nav-btn').removeClass('active');
    $(this).addClass('active');
    showSection('help');
  });

  $('#logs-btn').click(function() {
    $.get('/logs')
        .done(function(data) {
            $('#logs-content').html(data);
            showSection('logs');
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            $('#logs-content').text('Error: ' + errorThrown);
            showSection('logs');
        });
  });

  // Add event listener for help section button
  $('#help-section-button').click(function() {
    alert('You clicked the button in the help section!');
  });

  // Show the configuration section when the link is clicked
  $('#configuration-link').click(function() {
    showSection('configuration');
  });

  // Submit the configuration form
  $('#profile-form').submit(function(event) {
    event.preventDefault();

    // Collect form data
    var formData = {
      'servername': $('#servername').val(),
      'freqtrade_config_path': $('#freqtrade_config_path').val(),
      'user_data_path': $('#user_data_path').val(),
      'strategies_path': $('#strategies_path').val()
    };

    // Send form data as JSON to the server
    $.ajax({
      type: 'POST',
      url: '/profile',
      data: JSON.stringify(formData),
      contentType: 'application/json',
      success: function(data) {
        console.log('Form submitted successfully:', data);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error submitting form:', errorThrown);
      }
    });
  });

  showSection('configuration');
});
