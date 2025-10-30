// Lab10: Borrow checker and ownership exercises

fn takes_ownership(s: String) {
    // Takes ownership and drops at end of scope
}

fn makes_copy(x: i32) {
    // i32 implements Copy
}

fn gives_ownership() -> String {
    String::from("yours")
}

fn takes_and_gives_back(s: String) -> String {
    s
}

fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

fn main() {
    let s1 = gives_ownership();
    let s2 = String::from("hello world");
    let word = first_word(&s2);
    println!("{} {}", s1, word);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_word() {
        let s = String::from("hello rust");
        assert_eq!(first_word(&s), "hello");
    }

    #[test]
    fn test_takes_and_gives_back() {
        let s = String::from("ownership");
        let s2 = takes_and_gives_back(s);
        assert_eq!(s2, "ownership");
    }

    #[test]
    fn test_gives_ownership() {
        let s = gives_ownership();
        assert_eq!(s, "yours");
    }
}
