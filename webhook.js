const { IncomingWebhook } = require('@slack/webhook');
const fetch = require('node-fetch');

const webhookURL = process.env.PYTHON_API_URL;

module.exports = async (req, res) => {
    const response = await fetch(webhookURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(req.body),
    });

    const data = await response.json();

    res.status(response.status).json(data);
};
