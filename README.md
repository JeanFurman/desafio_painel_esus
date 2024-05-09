# Como rodar o projeto

```bash
git clone https://github.com/JeanFurman/desafio_painel_esus.git
```

```bash
docker-compose up --build
```

## Endpoint

A aplicação possui 1 endpoint, que se encontra em:

- `http://localhost:8001/api/v1/atendimentos` - (GET)

Porém com alguns filtros sendo eles:

- data_atendimento (str): Formato 'YYYY-mm-dd'.
- condicao_saude (str): hipertensao|diabetes|ferida vascular|dengue|tuberculose.
- unidade (str)

