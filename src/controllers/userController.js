const User = require("../models/user");

exports.getAllUsers = async (req, res) => {
    try {
        const users = await User.find();
        res.status(200).json(users);
    } catch (error) {
        res.status(400).json({ error: "Não foi possível obter os usuários" });
    }
}

exports.createUser = async (req, res) => {
    const { name, email } = req.body;
    try {
        const newUser = await User.create({ name, email });
        res.status(201).json(newUser);
    } catch (error) {
        res.status(400).json({ error: "Não foi possível criar o usuário" });
    }
}

exports.updateUser = async (req, res) => {
    const { id } = req.params;
    const newData = req.body;
    try {
        const updatedUser = await User.findByIdAndUpdate(id, newData, { new: true });
        res.status(200).json(updatedUser);
    } catch (error) {
        res.status(400).json({ error: "Não foi possível atualizar o usuário" });
    }
}

exports.deleteUser = async (req, res) => {
    const { id } = req.params;
    try {
        await User.findByIdAndDelete(id);
        res.status(200).json({ message: "Usuário excluído com sucesso" });
    } catch (error) {
        res.status(400).json({ error: "Não foi possível excluir o usuário" });
    }
}

exports.login = async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = await User.findOne({ email, password });
        if (user) {
            res.status(200).json({ message: 'Login bem-sucedido' });
        } else {
            res.status(401).json({ error: 'Credenciais inválidas' });
        }
    } catch (error) {
        res.status(500).json({ error: "Erro interno do servidor" });
    }
};
