import { useState } from "react";
import { atualizarPessoa } from "../services/api";

function EditarPessoa({ pessoa, onAtualizado }) {
  const [nome, setNome] = useState(pessoa.nome);
  const [foto, setFoto] = useState(null);
  const [idade, setIdade] = useState(pessoa.idade);
  const [curso, setCurso] = useState(pessoa.curso);
  const [periodo, setPeriodo] = useState(pessoa.periodo);
  const [opiniao, setOpiniao] = useState(pessoa.opiniao);

  const [preview, setPreview] = useState(null);

<input
  type="file"
  onChange={(e) => {
    const file = e.target.files[0];
    setFoto(file);
    setPreview(URL.createObjectURL(file));
  }}
/>

{preview && (
  <img src={preview} width="120" />
)}


  async function handleSubmit(e) {
    e.preventDefault();

    await atualizarPessoa(pessoa.id, {
      nome,
        idade,
        curso,
        periodo,
        opiniao,
      foto
    });

    onAtualizado();
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={nome}
        onChange={e => setNome(e.target.value)}
      />
      <input
        type="number"
        value={idade}
        onChange={e => setIdade(e.target.value)}
      />
      <input
        value={curso}
        onChange={e => setCurso(e.target.value)}
      />
      <input
        type="number"
        value={periodo}
        onChange={e => setPeriodo(e.target.value)}
      />
      <input
        value={opiniao}
        onChange={e => setOpiniao(e.target.value)}
      />
        <input
          type="file"
          onChange={(e) => {
            const file = e.target.files[0];
            setFoto(file);
            setPreview(URL.createObjectURL(file));
          }}
        />
      <button type="submit">💾 Salvar</button>
    </form>
  );
}

export default EditarPessoa;
