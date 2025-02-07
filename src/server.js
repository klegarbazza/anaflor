const express = require("express");
const cors = require("cors");
const controllers = require("./src/controllers");

const app = express();
app.use(cors());
app.use(express.json());

// Rotas
app.post("/cadastro", controllers.cadastrarUsuario);
app.post("/login", controllers.loginUsuario);

app.listen(3000, () => {
    console.log("Servidor rodando na porta 3000");
});
