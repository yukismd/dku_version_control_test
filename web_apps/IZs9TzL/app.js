$.getJSON(getWebAppBackendUrl('/get_datasets'), function(data) {
    console.log('Received data from backend', data)
    formattedJson = JSON.stringify(data,undefined,4)
    const output = $('<pre />').text(formattedJson);
    $('body').append(output)
});