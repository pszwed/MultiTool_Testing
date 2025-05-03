function fn() {
  karate.configure('connectTimeout', 10000);
  karate.configure('readTimeout', 10000);

  var config = {
    baseUrl: 'http://localhost:3000'
  };

  var auth = karate.callSingle('classpath:setup/authentication.feature');

  config.authToken = auth.token;
  config.basketId = auth.basketId;
  config.email = auth.email;
  config.password = auth.password;

  config.headers = {
    Authorization: 'Bearer ' + auth.token
  };

  karate.configure('headers', config.headers);

  return config;
}