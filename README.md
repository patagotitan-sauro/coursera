# coursera
cursos e exercícios do Coursera

## Software Design Patterns in Python

O diretório [pythonDesign/](pythonDesign/) contém as anotações e exercícios do curso de
**Software Design Patterns**, focado em Python. O curso é dividido em 11 módulos, indo dos
princípios fundamentais de design até anti-patterns específicos da linguagem:

| Módulo | Tópico |
|---|---|
| 1 | Foundational Design Principles |
| 2 | SOLID Principles |
| 3 | Creational Design Patterns |
| 4 | Structural Design Patterns |
| 5 | Behavioral Design Patterns |
| 6 | Architectural Design Patterns |
| 7 | Concurrency and Asynchronous Patterns |
| 8 | Performance Patterns |
| 9 | Distributed Systems Patterns |
| 10 | Patterns for Testing |
| 11 | Python Anti-Patterns |

### Módulo 1 — Foundational Design Principles

Antes de qualquer padrão de projeto, o curso apresenta os princípios que sustentam um bom
design de software:

- **Encapsulamento**: esconder o estado interno de um objeto e expor apenas o comportamento
  necessário através de uma interface bem definida ([`ch01/encapsulate.py`](pythonDesign/ch01/encapsulate.py)).
- **Abstração**: definir contratos (classes abstratas, `Protocol`) que descrevem *o que* um
  objeto faz, sem amarrar o código a *como* isso é feito
  ([`ch01/abstractclass.py`](pythonDesign/ch01/abstractclass.py)).
- **Composição sobre herança**: montar comportamento combinando objetos menores (ex.: um `Car`
  que possui um `Engine`) em vez de criar hierarquias de herança rígidas
  ([`ch01/composition.py`](pythonDesign/ch01/composition.py)).

Esses princípios preparam o terreno para o SOLID, aplicado no módulo seguinte.

### Módulo 2 — SOLID Principles

SOLID é um acrônimo para cinco princípios de design orientado a objetos que tornam o código
mais fácil de entender, estender e manter:

- **S — Single Responsibility Principle**: uma classe deve ter um único motivo para mudar,
  ou seja, uma única responsabilidade bem definida.
- **O — Open/Closed Principle**: entidades de software devem estar abertas para extensão, mas
  fechadas para modificação — novas funcionalidades são adicionadas por extensão (herança,
  `Protocol`), não alterando código já existente e testado
  ([`ch02/ocp.py`](pythonDesign/ch02/ocp.py), onde novas formas geométricas são adicionadas sem
  tocar em `calculate_area`).
- **L — Liskov Substitution Principle**: uma subclasse deve poder substituir sua classe base sem
  quebrar o comportamento esperado pelo programa.
- **I — Interface Segregation Principle**: é melhor ter várias interfaces pequenas e específicas
  do que uma única interface genérica que força classes a implementar métodos que não usam
  ([`ch02/isp.py`](pythonDesign/ch02/isp.py), onde `Printer`, `Scanner` e `Fax` são `Protocol`s
  separados em vez de uma única interface "multifuncional").
- **D — Dependency Inversion Principle**: módulos de alto nível não devem depender de módulos de
  baixo nível diretamente; ambos devem depender de abstrações (interfaces/`Protocol`).

### Módulo 3 — Creational Design Patterns

Padrões que tratam da criação de objetos, aplicando os princípios acima na prática:

- **Factory Method** ([`ch03/factory_method.py`](pythonDesign/ch03/factory_method.py)) — delega
  a criação de objetos a uma função/método dedicado.
- **Abstract Factory** ([`ch03/abstract_factory_method.py`](pythonDesign/ch03/abstract_factory_method.py))
  — agrupa vários factory methods relacionados.
- **Builder** ([`ch03/builder_pattern.py`](pythonDesign/ch03/builder_pattern.py)) — separa a
  construção de um objeto complexo de sua representação final.
- **Prototype** ([`ch03/prototype_pattern.py`](pythonDesign/ch03/prototype_pattern.py)) — cria
  novos objetos copiando instâncias existentes em vez de construí-los do zero.
- **Singleton** ([`ch03/singleton_pattern.py`](pythonDesign/ch03/singleton_pattern.py)) — garante
  que uma classe tenha apenas uma instância, com ponto de acesso global.

Os módulos 4 em diante (Structural, Behavioral, Architectural, Concurrency, Performance,
Distributed Systems, Testing e Anti-Patterns) serão adicionados a este repositório conforme o
curso avança.
