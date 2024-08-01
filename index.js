const express = require('express');
const bodyParser = require('body-parser');
const { Telegraf } = require('telegraf');

const app = express();
app.use(bodyParser.json());

// Bot token'ınızı çevre değişkenlerinden alır
const bot = new Telegraf(process.env.BOT_TOKEN);

// Webhook endpoint
app.post('/webhook', (req, res) => {
    bot.handle
