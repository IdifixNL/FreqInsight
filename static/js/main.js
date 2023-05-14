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

    // Get all selected time frames
    var timeFrames = [];
    $("input:checkbox[name='time_frames']:checked").each(function() {
      timeFrames.push($(this).val());
    });

    // Make the data download request
    $.ajax({
      url: '/download_data',
      type: 'POST',
      contentType: 'application/json', // Specify that we're sending JSON
      data: JSON.stringify({ days: daysBack, time_frames: timeFrames }), // Convert the data to a JSON string
      dataType: 'json', // Expect a JSON response
      success: function(data) {
        alert('Data download command executed successfully. Output: ' + JSON.stringify(data));
      },
      error: function(jqXHR, textStatus, errorThrown) {
        alert('Error executing data download command: ' + errorThrown);
      }
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



  $.get('/backtest')
  .done(function(data) {
    var strategyFiles = data.strategy_files;
    var strategySelect = $('#strategy-select');
    strategySelect.empty();
    for (var i = 0; i < strategyFiles.length; i++) {
      strategySelect.append($('<option>', {
        value: strategyFiles[i],
        text: strategyFiles[i]
      }));
    }
  })
  .fail(function(jqXHR, textStatus, errorThrown) {
    console.error('Error retrieving strategies:', errorThrown);
  });


  $('#backtest-form').submit(function(e) {
    e.preventDefault();

    var selectedStrategy = $('#strategy-select').val();

    $.post('/run_backtest', { 'strategy-select': selectedStrategy })
      .done(function(data) {
        alert('Backtest command executed successfully. Result: ' + data.result);
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        alert('Error executing backtest command: ' + errorThrown);
      });
    return false; // Prevent default form submission behavior
  });
});