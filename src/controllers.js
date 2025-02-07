const db = require("../models/db");

// Função para cadastrar usuário
const cadastrarUsuario = (req, res) => {
    const { nome, email, senha } = req.body;

    const sql = "INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)";
    
    db.query(sql, [nome, email, senha], (err, result) => {
        if (err) {
            return res.status(500).json({ error: "Erro ao cadastrar usuário" });
        }
        res.json({ message: "Usuário cadastrado com sucesso!" });
    });
};

module.exports = { cadastrarUsuario };


// Função para fazer login
const loginUsuario = (req, res) => {
    const { email, senha } = req.body;

    const sql = "SELECT * FROM users WHERE email = ? AND senha = ?";
    
    db.query(sql, [email, senha], (err, result) => {
        if (err) {
            return res.status(500).json({ error: "Erro no servidor" });
        }
        
        if (result.length > 0) {
            res.json({ message: "Login bem-sucedido!" });
        } else {
            res.status(401).json({ error: "Email ou senha incorretos" });
        }
    });
};

module.exports = { cadastrarUsuario, loginUsuario };
