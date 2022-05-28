# API

All source code related to the API.

`docker build -t drewdahlquist/dmc-pi-api:0.0 .`

`docker run -p 5000:8080 drewdahlquist/dmc-pi-api:0.0 >> server.log 2>&1`

NOTE: Containterized `server.js` works but need to iron out details of its communication with other app's such as the machine's api, etc. TLDR; Don't use Docker just yet for this
