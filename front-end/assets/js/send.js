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
  conversation.scrollTop = conversation.scrollHeight;
}

function getResponse(query) {
  var respmsg;
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {
        respmsg = JSON.parse(xhr.response).botresp;
        console.log(respmsg);
        showResp(respmsg);
      }
    }
  };
  xhr.open(
    'GET',
    'https://ashou6obvj.execute-api.us-east-1.amazonaws.com/dumbTest/?query=' +
      query,
    true
  );
  xhr.send();
}

function showResp(resp) {
  var conversation = document.getElementById('conversation');
  var str = '<div class="atalk"><span>' + resp + '</span></div>';
  conversation.innerHTML = conversation.innerHTML + str;
  conversation.scrollTop = conversation.scrollHeight;
}

function enterPress(e) {
  var e = e || window.event;
  if (e.keyCode == 13) {
    sendMessage();
  }
}
