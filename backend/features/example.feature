# language: pt
Funcionalidade: Listar um usuário

 Esquema do Cenário: Listar um usuário com sucesso
   Dado Eu efetuo requisição <metodo> para <endpoint> com identificação usuário <id>
   Então Eu verifico o resultado da requisição
   E Eu verifico o codigo de retorno <codigo_retorno>
   E Eu verifico o campo <email> 
   E Eu verifico o campo <primeiro_nome>
   E Eu verifico o campo <ultimo_nome>
   E Eu verifico o campo <avatar>

   Examples:
    | metodo | endpoint | codigo_retorno | id | primeiro_nome | ultimo_nome | avatar                                                             |
    | GET    | /users/2 | 200            | 2  | Janet         | Weaver      | https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg |
    
