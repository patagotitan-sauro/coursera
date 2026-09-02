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

Princípios de design são a base de qualquer software bem arquitetado: funcionam como um guia
que ajuda a criar aplicações fáceis de manter, escaláveis e robustas, evitando as armadilhas de
um design ruim. O módulo cobre quatro princípios fundamentais, que preparam o terreno tanto
para o SOLID (Módulo 2) quanto para os padrões de projeto (Módulo 3 em diante):

- **Encapsulate What Varies**: isolar as partes do código que estão sujeitas a mudança, para
  que adicionar ou trocar um comportamento não exija alterar o código que já funciona. Em
  [`ch01/encapsulate.py`](pythonDesign/ch01/encapsulate.py), `PaymentBase.process_payment()` é
  o "ponto de variação": `CreditCard` e `PayPal` implementam esse método cada um à sua maneira,
  e o laço `for payment in payments: payment.process_payment()` nunca precisa saber qual é o
  meio de pagamento concreto — um novo método de pagamento se encaixa sem tocar no código que
  os consome. Já [`ch01/encapsulate_bis.py`](pythonDesign/ch01/encapsulate_bis.py) mostra a face
  mais clássica do encapsulamento: esconder o estado interno (`_radius`) atrás de uma
  `@property`, validando o novo valor no setter em vez de expor o atributo diretamente.
- **Favor Composition Over Inheritance**: montar comportamento combinando objetos menores
  (relação "tem um") em vez de criar hierarquias de herança rígidas (relação "é um"). Em
  [`ch01/composition.py`](pythonDesign/ch01/composition.py), `Car` não herda de `Engine`; ele
  possui um `Engine` e delega a ele a responsabilidade de `start()`, o que evita hierarquias
  frágeis e permite trocar ou testar o `Engine` isoladamente.
- **Program to Interfaces, Not Implementations**: depender de um contrato (interface, classe
  abstrata ou `Protocol`) em vez de uma classe concreta específica, o que aumenta a flexibilidade
  e facilita a manutenção. [`ch01/abstractclass_abs.py`](pythonDesign/ch01/abstractclass_abs.py)
  faz isso com uma `ABC` (`Logger` com o método abstrato `log`), enquanto
  [`ch01/abstractclass_bis.py`](pythonDesign/ch01/abstractclass_bis.py) mostra a alternativa mais
  "pythônica" com `typing.Protocol` (tipagem estrutural, sem herança obrigatória). Em ambos os
  casos, `log_message(logger: Logger, message: str)` funciona com qualquer implementação —
  `ConsoleLogger` ou `FileLogger` — sem nunca depender das classes concretas.
  [`ch01/abstractclass.py`](pythonDesign/ch01/abstractclass.py) traz um exemplo mínimo do mesmo
  conceito com `MyInterface`/`MyClass`.
- **Loose Coupling**: reduzir as dependências entre componentes para que cada um possa ser
  modificado, testado ou substituído isoladamente, sem provocar um efeito cascata no resto do
  sistema. É a consequência natural de aplicar os três princípios anteriores: ao encapsular o
  que varia, preferir composição e programar contra interfaces, os próprios exemplos deste
  módulo (`Car`/`Engine`, `log_message`/`Logger`, `payments`/`PaymentBase`) já nascem fracamente
  acoplados — nenhum lado precisa conhecer os detalhes internos do outro para colaborar.

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

- **Factory Method** ([`ch03/factory_method.py`](pythonDesign/ch03_CreationalDesignPatterns/factory_method.py))
  — desacopla o código que precisa de um objeto do código que decide qual classe concreta
  instanciar, para que o chamador trabalhe contra uma interface comum em vez de uma cadeia de
  `if/elif` com nomes de classes espalhada pelo código. No exemplo do arquivo,
  `extract_factory(filepath)` centraliza essa decisão (extensão `.json` → `JSONDataExtractor`,
  `.xml` → `XMLDataExtractor`) em um único lugar; como ambas as classes expõem a mesma
  propriedade `parsed_data`, o chamador (`extract()`) nunca vê `JSONDataExtractor(...)` nem
  `XMLDataExtractor(...)` diretamente, e adicionar um novo formato exige apenas um novo branch
  na fábrica e uma nova classe, sem tocar em quem consome os dados. O próprio repositório traz
  o contraponto ao lado, em
  [`ch03/factory_method_not_needed.py`](pythonDesign/ch03_CreationalDesignPatterns/factory_method_not_needed.py):
  para casos simples, com poucos tipos, basta chamar `JSONDataExtractor(path)` diretamente —
  "just create objects where you need them" — sem a indireção de uma fábrica. O padrão só
  compensa seu custo quando o conjunto de tipos concretos é grande, tende a crescer, ou quando
  a lógica de criação em si é complexa (validação, lookups de configuração, múltiplos
  argumentos de construtor).
- **Abstract Factory** ([`ch03/abstract_factory_method.py`](pythonDesign/ch03_CreationalDesignPatterns/abstract_factory_method.py))
  — agrupa várias factory methods relacionadas em uma única fábrica, de modo que o código
  cliente crie **famílias inteiras de objetos relacionados** sem conhecer suas classes
  concretas. No exemplo do arquivo, `FrogWorld` e `WizardWorld` são fábricas que produzem,
  cada uma, um par consistente de objetos (`Frog`+`Bug` ou `Wizard`+`Ork`); `GameEnvironment`
  só conhece a interface `make_character()`/`make_obstacle()`, nunca as classes concretas.
  Isso garante que os objetos de uma família nunca se misturem (não existe `Wizard` lutando
  contra `Bug`), permite adicionar um novo "mundo" só criando uma nova fábrica sem alterar
  `GameEnvironment` (Open/Closed) e mantém o código cliente dependendo de abstrações, não de
  implementações (Dependency Inversion) — é, na prática, o Factory Method levado um nível
  acima: em vez de um método de fábrica produzir um tipo de objeto, o Abstract Factory agrupa
  vários métodos de fábrica que juntos produzem um conjunto coerente de objetos.
- **Builder** ([`ch03/builder_pattern.py`](pythonDesign/ch03_CreationalDesignPatterns/builder_pattern.py))
  — separa a construção de um objeto complexo de sua representação final, quando essa
  construção envolve **múltiplos passos sequenciais e estado intermediário**, algo que um
  único construtor ou uma factory (que entrega o objeto pronto em uma única chamada) não
  representa bem. No exemplo do arquivo, montar uma pizza segue sempre a mesma sequência
  (`prepare_dough → add_sauce → add_topping → bake`), com estado acumulado a cada passo
  (`self.pizza.dough`, `.sauce`, `.topping`); `MargaritaBuilder` e `CreamyBaconBuilder`
  seguem esse mesmo procedimento mas implementam cada passo de forma diferente (massa fina
  vs. grossa, coberturas e tempo de forno distintos). O `Waiter` atua como "diretor": conhece
  a ordem dos passos mas não os detalhes de cada builder concreto, evitando também um
  construtor telescópico (`Pizza(dough, sauce, topping, baking_time, ...)`).
- **Prototype** ([`ch03/prototype_pattern.py`](pythonDesign/ch03_CreationalDesignPatterns/prototype_pattern.py)) — cria
  novos objetos copiando instâncias existentes em vez de construí-los do zero.
- **Singleton** ([`ch03/singleton_pattern.py`](pythonDesign/ch03_CreationalDesignPatterns/singleton_pattern.py)) — garante
  que uma classe tenha apenas uma instância, com ponto de acesso global.
- **Object Pool** ([`ch03/object_pool_pattern.py`](pythonDesign/ch03_CreationalDesignPatterns/object_pool_pattern.py))
  — evita o custo de criar e destruir repetidamente objetos caros de instanciar, reutilizando
  um conjunto fixo de instâncias já existentes. No exemplo do arquivo, `CarPool` mantém duas
  listas, `_available` (carros ociosos, prontos para reuso) e `_in_use` (carros emprestados);
  `acquire_car()` só cria um `Car` novo quando o pool está vazio, e `release_car()` devolve o
  carro para `_available` em vez de deixá-lo ser descartado. Diferente do Singleton (que
  restringe a *uma única* instância), o Object Pool gerencia um conjunto *reutilizável e
  limitado* de instâncias, trocando um pouco de complexidade de controle (rastrear o que está
  em uso vs. disponível) por menos overhead de alocação/destruição sob demanda repetida —
  útil sobretudo para recursos caros como conexões de banco de dados, threads ou, como na
  analogia do próprio arquivo, carros de aluguel.

Os módulos 4 em diante (Structural, Behavioral, Architectural, Concurrency, Performance,
Distributed Systems, Testing e Anti-Patterns) serão adicionados a este repositório conforme o
curso avança.
