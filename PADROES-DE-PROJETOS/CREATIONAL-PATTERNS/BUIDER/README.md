![Alt text](https://raw.githubusercontent.com/diegoMasin/landing-maximumtech/master/assets/img/new-logo-mt-01.png)
<br><br>

# Padrões de Projetos - Builder

###### Estudos e aprimoramento dos conhecimentos de padrões de projetos

## Definição / Resolve que problemas?

- Esse padrão define uma forma de construir um objeto complexo por partes.
- Problema que resolve / Vantagens:
  - Quando temos um objeto complexo que requer uma inicialização trabalhosa e passo a passo de muitos campos e objetos aninhados.
  - Um construtor gigante com muitos parâmetros. E nem sempre precisamos de todos os parâmetros principalmente se vez ou outra precisar apenas criar um instancia simples daquele objeto.
- Falando mais sobre a solução Builder:
  - Builder é basicamente você extrair o código de construção do objeto de sua própria classe e o move-lo para objetos separados chamados construtores (por isso, "construir por partes").
  - O Builder também não permite que outros objetos acessem o objeto alvo enquanto ele estiver sendo construído.
  - Podemos inclusive ter outros tipos de objetos construtores para construir uma versão específica com detalhes específicos do objeto alvo. Exempo o Objeto alvo é Casa, e criamos o objeto BuilderCasa que constroi tanto casas pequenas como casas grandes com diversos e imagináveis atributos que uma casa grande poderia ter, porem também podemos criar navas classes construtores de casas específicas como por exemplo: BuilderCastelo, BuilderCasaCampo, BuilderCasaExterior, etc;

## Dúvidas / Discussão em grupo

- Seria possível ter um exemplo de como seria/ocorreria a negação quando outro objeto tivesse tentando acessar o objeto ainda em construção? O que aconteceria nos logs, e tal.
