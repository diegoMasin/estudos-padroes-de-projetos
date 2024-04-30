![Alt text](https://raw.githubusercontent.com/diegoMasin/landing-maximumtech/master/assets/img/new-logo-mt-01.png)
<br><br>

# Padrões de Projetos - Singleton

###### Estudos e aprimoramento dos conhecimentos de padrões de projetos

## Definição / Resolve que problemas?

- Esse padrão define que uma classe tenha apenas uma instância e que seja fornecido um ponto global de acesso a essa instância.
- Vantagens e Garantias (Problema à resolver):
  - Conservação de recursos
  - Fornece meios de acesso concorrente para que a única instância de uma classe possa ser compartilhada entre componentes ou threads.
- Desvantagens:
  - Singleton viola o `princípio da responsabilidade única` (uma classe deve possuir uma, e apenas uma, responsabilidade) para resolver esses dois problemas
- Uma abordagem alternativa a ser considerada é por exemplo a `injeção de dependência`
- Singleton ainda é válido em cenários que aja uma necessidade genuína de ter classes com apenas uma instância

## Como aplicar e mais detalhes

- Se o comportamento padrão de um construtor é criar novas instâncias como aplicar Singleton?
- Passos:
  - Torne o construtor padrão privado, para evitar que outros objetos usem o operador new
  - Crie um método de criação estático que atue como construtor. Internamente, este método chama o construtor privado para criar um objeto e o salva em um campo estático. Todas as chamadas seguintes para este método retornam o objeto armazenado em cache.
    - Em outras palavras, sempre que esse método for chamado, o mesmo objeto será retornado.
- Lista de cenários potencias a aplicação do Singleton:
  - Logger
  - Acesso a banco de dados
  - Configurações globais
  - Gerenciamento de Sessão
  - Cache de dados frequentes acessados

## Dúvidas / Discussão em grupo

- Como injeção de dependencias seria uma alternativa ao invés do uso de Singleton? Existem outras alternativas?
- Como aplicar/usar a parte de uso compartilhado? Exemplos?
- O Principio de responsabilidade única pertence aos padrões de projetos? Pq é tão considerado a ponto de ser mais importante que o singleton que é um padrão de projeto? - SOLID X Padrões de projetos, qual seguir e pq seguir (`SOLID` são princípios, e `padrões de projetos` são padrões para resolver os mais comuns problemas de desenvolvimento do dia-a-dia)
