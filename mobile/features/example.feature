Feature: Aprendendo Appium
   Given Eu inicio a aplicação

   @mcsj
   Scenario: Preenchendo a opção formulário
        Given Eu clico na opção formulário
        When Eu preencho o formulário com os dados abaixo
        |name   |xbox_one|checkbox|switch|
        |Teste 1|50      | True   |True  |
