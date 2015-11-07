# mqtt_secure_chat
A simple script to chat securely using mqtt pub-sub

## Installation
- `pip install paho-mqtt`
- Generate the key and certificate to be used by clients. There's a [bash script](https://github.com/owntracks/tools/blob/master/TLS/generate-CA.sh) available for key generation.
- It produces six files if no arguments are given, we'll be using three (or two, if we are not running a broker).
  - `ca.crt` is used by the broker
  - `<hostname>.crt` and `<hostname>.key` are used by the clients
  - To connect `test.mosquitto.org`, use [mosquitto.org.crt](test.mosquitto.org/ssl/mosquitto.org.crt)
- If we want to run our own broker, get the version of mosquitto (or any other) that supports TLS. Better to compile the latest version of mosquitto, since it doesn't take much time. Also, it can be run under normal privilege. After compilation, modify the `mosquitto.conf` file with the instructions given in that file's comments.


P.S. The [mosquitto-tls](http://mosquitto.org/man/mosquitto-tls-7.html) page has some instructions to generate keys and certificates, but the details are inadequate. We'll end up with failure like `SSL3_GET_SERVER_CERTIFICATE:certificate verify failed`
