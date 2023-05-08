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

  showSection('configuration');
});
