use std::fmt;

fn main() {
    println!("Lab 12: Generic Stack with TDD");
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Stack<T> {
    items: Vec<T>,
}

impl<T> Stack<T> {
    pub fn new() -> Stack<T> {
        Stack { items: Vec::new() }
    }

    pub fn is_empty(&self) -> bool {
        self.items.is_empty()
    }

    pub fn push(&mut self, item: T) {
        self.items.push(item);
    }

    pub fn len(&self) -> usize {
        self.items.len()
    }

    pub fn pop(&mut self) -> Option<T> {
        self.items.pop()
    }

    pub fn peek(&self) -> Option<&T> {
        self.items.last()
    }
}

impl<T: fmt::Display> fmt::Display for Stack<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[")?;
        for (i, item) in self.items.iter().enumerate() {
            if i > 0 {
                write!(f, ", ")?;
            }
            write!(f, "{}", item)?;
        }
        write!(f, "]")
    }
}

impl<T> Iterator for Stack<T> {
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        self.pop()
    }
}

// Note: do not implement IntoIterator explicitly for `Stack<T>` here.
// There's a blanket impl `IntoIterator for I where I: Iterator` in `core`
// which applies because `Stack<T>` implements `Iterator`. Implementing
// `IntoIterator` manually would conflict with that blanket impl.

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_stack_is_empty() {
        let stack: Stack<i32> = Stack::new();
        assert!(stack.is_empty());
        assert_eq!(stack.len(), 0);
    }

    #[test]
    fn test_push_increases_length() {
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assert_eq!(stack.len(), 3);
        assert!(!stack.is_empty());
    }

    #[test]
    fn test_pop_returns_last_pushed() {
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        assert_eq!(stack.pop(), Some(2));
        assert_eq!(stack.pop(), Some(1));
        assert_eq!(stack.pop(), None);
    }

    #[test]
    fn test_pop_empty_stack() {
        let mut stack: Stack<i32> = Stack::new();
        assert_eq!(stack.pop(), None);
    }

    #[test]
    fn test_peek_without_removing() {
        let mut stack = Stack::new();
        stack.push(42);
        assert_eq!(stack.peek(), Some(&42));
        assert_eq!(stack.len(), 1);
    }

    #[test]
    fn test_peek_empty_stack() {
        let stack: Stack<i32> = Stack::new();
        assert_eq!(stack.peek(), None);
    }

    #[test]
    fn test_multiple_types_string_and_int() {
        let mut s_stack = Stack::new();
        s_stack.push(String::from("a"));
        s_stack.push(String::from("b"));
        assert_eq!(s_stack.len(), 2);
        assert_eq!(s_stack.pop(), Some(String::from("b")));

        let mut i_stack: Stack<i32> = Stack::new();
        i_stack.push(10);
        assert_eq!(i_stack.peek(), Some(&10));
    }

    #[test]
    fn test_push_pop_sequences() {
        let mut stack = Stack::new();
        for i in 0..5 {
            stack.push(i);
        }
        for expected in (0..5).rev() {
            assert_eq!(stack.pop(), Some(expected));
        }
        assert!(stack.is_empty());
    }

    #[test]
    fn test_display_format() {
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        assert_eq!(format!("{}", stack), "[1, 2, 3]");
    }

    #[test]
    fn test_display_empty() {
        let stack: Stack<i32> = Stack::new();
        assert_eq!(format!("{}", stack), "[]");
    }

    #[test]
    fn test_iterator_next_lifo() {
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        let mut iter = stack.into_iter();
        assert_eq!(iter.next(), Some(3));
        assert_eq!(iter.next(), Some(2));
        assert_eq!(iter.next(), Some(1));
        assert_eq!(iter.next(), None);
    }

    #[test]
    fn test_for_loop_consumes_stack_in_lifo_order() {
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);

    let mut results: Vec<i32> = Vec::new();
        for item in stack {
            results.push(item);
        }
        assert_eq!(results, vec![2, 1]);
    }

    // Additional edge case tests
    #[test]
    fn test_len_after_operations() {
        let mut stack = Stack::new();
        assert_eq!(stack.len(), 0);
        stack.push(5);
        assert_eq!(stack.len(), 1);
        stack.pop();
        assert_eq!(stack.len(), 0);
    }

    #[test]
    fn test_clone_and_equality() {
        let mut stack1 = Stack::new();
        stack1.push(7);
        stack1.push(8);
        let stack2 = stack1.clone();
        assert_eq!(stack1, stack2);
    }

    #[test]
    fn test_iterator_on_empty_stack() {
        let stack: Stack<i32> = Stack::new();
        let mut iter = stack.into_iter();
        assert_eq!(iter.next(), None);
    }
}
