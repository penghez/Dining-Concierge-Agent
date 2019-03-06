function sendMessage() {
  var conversation = document.getElementById('conversation');
  var query = document.getElementById('input-query');

  var str = '';
  if (query.value == '') {
    alert('You can not send empty query!');
    return;
  }

  str = '<div class="btalk"><span>' + query.value + '</span></div>';
  conversation.innerHTML = conversation.innerHTML + str;

  getResponse(query.value);
  query.value = '';
}

function getResponse(query) {
  var respmsg;
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {
        respmsg = JSON.parse(JSON.parse(xhr.response).body).botresp;
        showResp(respmsg);
      }
    }
  };
  xhr.open(
    'GET',
    'https://19szjc1ung.execute-api.us-east-1.amazonaws.com/dumbTest/botresp',
    true
  );
  xhr.setRequestHeader('Content-Type', 'application/form-data');
  xhr.send();
}

function showResp(resp) {
  var str = '<div class="atalk"><span>' + resp + '</span></div>';
  conversation.innerHTML = conversation.innerHTML + str;
}
