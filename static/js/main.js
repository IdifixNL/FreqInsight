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
    showSection('backtest');
  });

  $('#hyperopt-btn').click(function() {
    showSection('hyperopt');
  });

  $('#datadownload-btn').click(function() {
    showSection('datadownload');
  });

  $('#configuration-btn').click(function() {
    showSection('configuration');
  });

  $('#help-btn').click(function() {
    showSection('help');
  });

  $('#test-btn').click(function() {
    // Show the "Test" button in the "Test" section
    $('#test-section-button').show();

    // Show the "Test" section
    showSection('test');
  });

  $('#test-section-button').click(function() {
    $.post('/test')
        .done(function(data) {
            $('#test-result').text("Message: " + data.message + "\nName: " + data.name + "\nState: " + data.state);
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            $('#test-result').text('Error: ' + errorThrown);
        });
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

  showSection('configuration');
});
