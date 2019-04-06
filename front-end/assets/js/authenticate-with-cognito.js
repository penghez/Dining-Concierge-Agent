$(document).ready(function() {
  if (window.location.href.indexOf('id_token') >= 0) {
    var urlParams = new URLSearchParams(window.location.href.split('#')[1]);
    id_token = urlParams.get('id_token');
    // Set the region where your identity pool exists (us-east-1, eu-west-1)
    AWS.config.region = 'us-east-1';

    // Configure the credentials provider to use your identity pool
    AWS.config.credentials = new AWS.CognitoIdentityCredentials({
      IdentityPoolId: 'us-east-1:7dea26fc-b8f2-4c8d-a215-a4cc1a493cb6',
      Logins: {
        'cognito-idp.us-east-1.amazonaws.com/us-east-1_Hxgpi6Roi': id_token
      }
    });

    AWS.config.credentials.get(function() {
      // Credentials will be available when this function is called.
      var accessKeyId = AWS.config.credentials.accessKeyId;
      var secretAccessKey = AWS.config.credentials.secretAccessKey;
      var sessionToken = AWS.config.credentials.sessionToken;
      apigClient = apigClientFactory.newClient({
        // apiKey: 'Wjuixivtg57BT2XHNP4jZ9KHb0zWIsI0lsjCGab0',
        accessKey: accessKeyId,
        secretKey: secretAccessKey,
        sessionToken: sessionToken
      });
      console.log(accessKeyId);
      console.log(secretAccessKey);
      console.log(sessionToken);
    });
  } else if (window.location.href.indexOf('code') >= 0) {
    // Signed in using code: we need to go to oauth2/token to exchange the code for the token
    var urlParams = new URLSearchParams(window.location.search);
    code = urlParams.get('code');
    requestbody =
      'grant_type=authorization_code&client_id=42g4pupk8g40nv2aamq8kd7cgc&code=' +
      code +
      '&redirect_uri=https://s3.amazonaws.com/dining-concierge-agent-2/front-end/index.html';
    $.ajax({
      url: 'https://diningbot.auth.us-east-1.amazoncognito.com',
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: requestbody,

      success: function(data) {
        access_token = data['access_token'];
        id_token = data['id_token'];
        refresh_token = data['refresh_token'];
        var urlParams = new URLSearchParams(window.location.href.split('#')[1]);
        // Set the region where your identity pool exists (us-east-1, eu-west-1)
        AWS.config.region = 'us-east-1';

        // Configure the credentials provider to use your identity pool
        AWS.config.credentials = new AWS.CognitoIdentityCredentials({
          IdentityPoolId: 'us-east-1:7dea26fc-b8f2-4c8d-a215-a4cc1a493cb6',
          Logins: {
            'cognito-idp.us-east-1.amazonaws.com/us-east-1_Hxgpi6Roi': id_token
          }
        });
        AWS.config.credentials.get(function() {
          // Credentials will be available when this function is called.
          var accessKeyId = AWS.config.credentials.accessKeyId;
          var secretAccessKey = AWS.config.credentials.secretAccessKey;
          var sessionToken = AWS.config.credentials.sessionToken;
          apigClient = apigClientFactory.newClient({
            // apiKey: 'Wjuixivtg57BT2XHNP4jZ9KHb0zWIsI0lsjCGab0',
            accessKey: accessKeyId,
            secretKey: secretAccessKey,
            sessionToken: sessionToken
          });
          console.log(accessKeyId);
          console.log(secretAccessKey);
          console.log(sessionToken);
        });
      }
    });
  } else {
    window.location.href =
      'https://diningbot.auth.us-east-1.amazoncognito.com/login?response_type=code&client_id=42g4pupk8g40nv2aamq8kd7cgc&redirect_uri=https://s3.amazonaws.com/dining-concierge-agent-2/front-end/index.html';
  }
});
