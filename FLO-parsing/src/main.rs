#[derive(Clone, Copy, Debug, PartialEq)]
enum Subject {
	Universal, 
	Existential, 
	Variables(x)
}

fn generate(s: Sentence) -> FOL {
	let subject = s.subject;
	match(subject) {
		Universal => {print_universal()}
		Variables(x) => {}
	}
}

#[derive(Clone, Copy, Debug, PartialEq)]
enum Quantifier {
	Universal, 
	Existential, 
}