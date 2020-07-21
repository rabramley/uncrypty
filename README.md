# Uncrypty

## Development

To quickly get the server up and running open 2 command windows.
Run this command to start the Web Socket Server:

```
python server.py
```

You will then need a HTTP server to serve the client.html:

```
python -m http.server 8000
```

Then browse to http://localhost:8000/client.html
