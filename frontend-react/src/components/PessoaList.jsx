import { useEffect, useState } from "react";
import { listarPessoas, deletarPessoa } from "../services/api";
import EditarPessoa from "./EditarPessoa";

function PessoaList() {
  const [pessoas, setPessoas] = useState([]);
  const [editandoId, setEditandoId] = useState(null);

  function carregar() {
    listarPessoas().then(setPessoas);
  }

  useEffect(() => {
    carregar();
  }, []);

  async function handleDelete(id) {
    await deletarPessoa(id);
    carregar();
  }

  return (
  <ul>
  {pessoas.map(p => (
    <li key={p.id}>
      {p.foto && (
        <img
          className="pessoa-img"
          src={`http://127.0.0.1:8000${p.foto}`}
          alt={p.nome}
        />
      )}

      <div className="pessoa-info">
        <p><strong>Nome:</strong> {p.nome}</p>
        <p><strong>Idade:</strong> {p.idade}</p>
        <p><strong>Curso:</strong> {p.curso}</p>
        <p><strong>Período:</strong> {p.periodo}</p>
        <p><strong>Opinião:</strong> {p.opiniao}</p>
      </div>

      <div className="pessoa-actions">
        <button
          className="btn-delete"
          onClick={() => handleDelete(p.id)}
        >
          ❌
        </button>

        <button
          className="btn-edit"
          onClick={() => setEditandoId(p.id)}
        >
          ✏️
        </button>
      </div>

      {editandoId === p.id && (
        <EditarPessoa
          pessoa={p}
          onAtualizado={() => {
            setEditandoId(null);
            carregar();
          }}
        />
      )}
    </li>
  ))}
</ul>

  );
}

export default PessoaList;
