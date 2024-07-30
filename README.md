# Forge Auth2 🚀

## Descrição 📜

O repositório `forge-auth2` é responsável pelo gerenciamento de identidade das entidades do projeto Forge. Abaixo estão as informações sobre as branches e o processo de automação.

## Estrutura das Branches 🌳

- **`development`**: Ambiente de desenvolvimento (`localhost:50000`) 🔧
- **`master`**: Ambiente de produção (`localhost:5000`) 🌟

## Recomendações para Branches 🔖

- **Nomeclatura das Branches**: As novas branches devem seguir a nomenclatura `feature/xxx` ou `bugfix/xxx` para facilitar a organização e o controle das alterações.
- **Branch `development` e `master`**: Essas branches são restritas. Para realizar alterações nelas, você deve:
  1. Criar uma branch `feature` ou `bugfix` a partir da branch `development`.
  2. Submeter um Pull Request (PR) para a branch `development`.
  3. Após a aprovação e integração na branch `development`, submeter um PR para a branch `master`.

## Processos Automatizados ⚙️

Todo o processo de integração e deploy é automatizado para garantir que as mudanças sejam feitas de maneira organizada e segura.

## Como Contribuir 🤝

1. Crie uma branch `feature` ou `bugfix` para suas alterações.
2. Faça um Pull Request para a branch `development`.
3. Após aprovação, faça um Pull Request para a branch `master`.