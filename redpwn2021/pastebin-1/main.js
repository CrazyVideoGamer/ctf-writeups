const express = require('express')
const https = require('https');
const cors = require('cors')

const app = express()
const port = 443

app.use(cors())

const fs = require('fs');
const key = fs.readFileSync('./key.pem');
const cert = fs.readFileSync('./cert.pem');

const server = https.createServer({key: key, cert: cert }, app);

app.get('/yay', (req, res) => {
	console.log(req.query.cookie)
	  res.send('Hello World!')
})

server.listen(port, () => {
	  console.log(`Example app listening at https://localhost:${port}`)
})
