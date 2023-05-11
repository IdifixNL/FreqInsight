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

  $('#configuration-btn').click(function() {
    $('.nav-btn').removeClass('active');
    $(this).addClass('active');
    showSection('configuration');

    // Check if the current path matches the configuration path
    if (window.location.pathname === '/config/') {
      // Reload the page to render the configuration form
      window.location.reload();
    }
  });

  $('#download-form').submit(function(e) {
    e.preventDefault();

    // Get the selected number of days
    var daysBack = $('#days-back').val();

    // Make the data download request
    $.post('/download_data', { days: daysBack })
      .done(function(data) {
        alert('Data download command executed successfully. Output: ' + data.message);
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        alert('Error executing data download command: ' + errorThrown);
      });
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
