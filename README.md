This is the API server that can translate morse code into english and english into morse code.

**Demo:** https://morse.freaks.dev

#### Usage
To translate morse code into english:
```
curl -L -d 'input=Hello World!' morse.freaks.dev
```

To translate english into morse code:
```
curl -L -d 'input=.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--' morse.freaks.dev
```

#### Local Testing
With docker:
```
docker run --rm -d -p 3000:3000 heinokesoe/morse-translate-api-server:latest
```

With docker-compose:
```
docker-compose up -d
```

The API server will be running at http://localhost:3000
