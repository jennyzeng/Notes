# Quiz 3 review by Jenny Zeng
## Propositional Logic
### logical Agents
#### basic concepts:
3. **Propositional logic**: concrete statements that are either true or false. e.g. John is married to Sue.
4. **Predicate logic (first order logic/ first order predicate calculus)**: allows statements to contain variables, functions, and quantifiers. e.g. For all X, Y: If X is married to Y then Y is married to X.
5. **Probability: **statements that are possibly true; the chance I win the lottery?
6. **Fuzzy logic: **vague statements; paint is ++slightly grey++; sky is ++very cloudy++.
7. **Modal logic: ** is a class of various logics that introduce modalities:
	- **Temporal logic: ** statements about time; John was a student at UCI for ++four years++
	- **Belief and knowledge**: Mary ++knows++ that john is married to Sue
	- **Possibility and Necessity: ** what ++might++ happen(possibility) and ++must++ happen (nacessity);
	- **Obligation and Permission: ** It is ++obligatory++ taht students study for their tests; it is ++permissible++ that I go fishing when I am on vacation.
8. **Induction: ** Reason from facts to the general law. 
9. **Abduction: ** Reason from facts to the best explanation.
10. **Analogy: ** Reason that a new situation is like an old one. 
11. **Schematic perspective: **If KB is true in the real world, then any sentence $\alpha$ entailed by KB is also true in the real world. 

#### important concepts: 
11. **Logics: ** are formal languages for represneting information such as conclusions can be drawn from formal inference patterns.
12. **Syntax: **Specifies all the sentences in a language that are well formed.
13. **Semantics**: Defines truth of each sentence with respect to each possible world.
15. **Entailment: ** The idea that a sentence follows logically from other sentneces.
16. **inference**: deriving sentences from other sentences
17. **model: ** Possible world that assigns TRUE or FALSE to each proposition.
18. **soundness: **derivations produce only entailed sentences
19. **KB**: knowledge base - a set of sentences or facts
20. **valid**: sentence is true in every model (a tautology)
21. **satisfiable: **A sentence is satisfiable if it is true in some model
22. **unsatisfiable: **A sentence is unsatisfiable if it is false in all model.

#### logical equivalence
![logical equivalence](logicalEquivalence.png "" "width:70%")
### truth table
![truth table](truthtable.png "" "width:60%")
### Methods of Proof
1. **Sound: ** An inference procedure that derives only entailed sentences.
2. **Complete: ** An inference procedure that derives all entailed sentences. 
3. **Propositional Symbol: **Stands for a proposition taht can be true or false.
4. **Proof: **Chain of inference rule conclusions leading to a desired sentence.
5. **Conjunctive Normal Form: **Describes a sentence that is true in some model.


### Knowledge engineering process
1. Identify the task.
2. Assemble the relevant knowledge.
3. Decide on a vocabulary of predicates, functions, and constants.
4. Encode general knowledge about the domain.
5. Encode a description of the specific problem instance.
6. Pose queries to the inference procedure and get answers.
7. Debug the knowledge base.


## First-order Logic Syntax
### Syntax of FOL: 
- A **Predicate** is a list of m-tuples making the predicate true.
	- E.g., PrimeFactorOf \= \{<2,4>, <2,6>, <3,6>, <2,8>, <3,9>, …\}
- A **Property** lists the m-tuples that have the property.
	- E.g., IsRed = { < Ball-5 >, < Toy-7 >, < Car-11 > }
- A **Function **CAN BE represented as an m-ary relation
	– the first (m-1) objects are the arguments and the mth is the value.
- An **Object** CAN BE represented as a function of zero arguments that returns the object.
- **Term** = logical expression that refers to an object
	- **Constant Symbols** stand for (or name) objects
	- **Function Symbols** map tuples of objects to an object
- **Atomic Sentences** state facts (logical truth values).



#### possible quiz questions
1. ==All persons are mortal.==
	![s1](s1.png "" "width:50%")
2. ==Fifi has a sister who is a cat.==
	![s2](s2.png "" "width:50%")
3.  ==For every food, there is a person who eats that food.==
	![s3](s3.png "" "width:60%")
4. ==every person eats every food.==
	![s4](s4.png "" "width:50%")
5. ==all greedy kings are evil.==
	![s5](s5.png "" "width:55%")
6. ==everyone has a favorite food.==
	![s6](s6.png "" "width:50%")
7. ==There is someone at UCI who is smart.==
	![s7](s7.png "" "width:50%")
8. ==Every one at UCI is smart.==
	![s8](s8.png "" "width:50%")
9. ==Every person eats some food.==
	![s9](s9.png "" "width:55%")
10. ==some person eats some food.==
	![s10](s10.png "" "width:50%")

