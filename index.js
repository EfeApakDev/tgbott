const express = require('express');
const bodyParser = require('body-parser');
const { Telegraf } = require('telegraf');

const app = express();
app.use(bodyParser.json());

const bot = new Telegraf(process.env.BOT_TOKEN); // Bot token'ınızı çevre değişkenlerinden alır

// Webhook endpoint
app.post('/webhook', (req, res) => {
    bot.handleUpdate(req.body);
    res.sendStatus(200);
});

// Bot komutları
bot.start((ctx) => ctx.reply('Bot çalışıyor!'));

// Uygulamayı başlat
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server çalışıyor: ${port}`);
});
