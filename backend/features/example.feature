Feature: Listar um usuário

 @wip 
 Scenario Outline: Listar um usuário com sucesso
   Given Eu efetuo requisição "<metodo>" para "<endpoint>" com identificação usuário "<id>"
   Then  Eu verifico o codigo de retorno "<codigo_retorno>"
  #  And   Eu verifico o campo <email> 
  #  And   Eu verifico o campo <primeiro_nome>
  #  And   Eu verifico o campo <ultimo_nome>
  #  And   Eu verifico o campo <avatar>

   Examples:
    | metodo | endpoint | codigo_retorno | id | primeiro_nome | ultimo_nome | avatar                                                             |
    | GET    | users/   | 200            | 2  | Janet         | Weaver      | https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg |
    
