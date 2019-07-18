Feature: Listar um usuário


Scenario: Listar um usuário com sucesso 1
   Given Eu efetuo requisição "GET" para "users/" com identificação usuário "2"
   Then  Eu verifico o codigo de retorno "200"
   And   Eu verifico o campo email "janet.weaver@reqres.in"
   And   Eu verifico o campo primeiro nome "Janet"
   And   Eu verifico o campo ultimo nome "Weaver"
   And   Eu verifico o campo avatar "https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"
 
Scenario Outline: Listar um usuário com sucesso 2
   Given Eu efetuo requisição "<metodo>" para "<endpoint>" com identificação usuário "<id>"
   Then  Eu verifico o codigo de retorno "<codigo_retorno>"
   And   Eu verifico o campo email "<email>"
   And   Eu verifico o campo primeiro nome "<primeiro_nome>"
   And   Eu verifico o campo ultimo nome "<ultimo_nome>"
   And   Eu verifico o campo avatar "<avatar>"

Examples:
  | metodo | endpoint | codigo_retorno | id | primeiro_nome | email                  | ultimo_nome | avatar                                                             |
  | GET    | users/   | 200            | 2  | Janet         | janet.weaver@reqres.in | Weaver      | https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg |
    

@wip
Scenario: Listar um usuário com sucesso 3
  Given Eu efetuo solicitação de dados do usuario
     | metodo | endpoint | id |
     | GET    | users/   | 2  |
  Then  Eu verifico seu retorno da solicitação
     | codigo_retorno | primeiro_nome | email                  | ultimo_nome | avatar                                                             |
     | 200            | Janet         | janet.weaver@reqres.in | Weaver      | https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg |

    