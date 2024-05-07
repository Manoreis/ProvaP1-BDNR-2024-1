const express = require('express');
const path = require('path');
const dotenv = require('dotenv');
const ConnectMongoDB = require('./src/database');
const userRoutes = require('./src/routes/userRoutes');


dotenv.config({ path: 'src/.env' });

const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));
ConnectMongoDB();

app.use('/', userRoutes);

app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'src', 'public', 'login.html'));
});

app.post('/login', async (req, res) => {
    const { email, password } = req.body;
    
    res.redirect('/success');
});

app.use((req, res) => {
    res.status(404).send('Página não encontrada');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta: ${PORT}`);
});