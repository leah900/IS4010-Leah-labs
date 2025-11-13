mod student;
use student::{Student, Grade, CourseGrade, StudentDatabase};

fn main() {
    println!("Student Management System demo");

    let mut db = StudentDatabase::new();

    let mut alice = Student::new(
        String::from("S001"),
        String::from("Alice Johnson"),
        String::from("alice@example.com"),
    );
    alice.add_grade(CourseGrade::new(
        String::from("IS4010"),
        String::from("App Dev with AI"),
        3,
        Grade::A,
    ));

    let mut bob = Student::new(
        String::from("S002"),
        String::from("Bob Smith"),
        String::from("bob@example.com"),
    );
    bob.add_grade(CourseGrade::new(
        String::from("IS3050"),
        String::from("Database Design"),
        3,
        Grade::B,
    ));

    db.add_student(alice).unwrap();
    db.add_student(bob).unwrap();

    println!("Total students: {}", db.student_count());
    println!("Average GPA: {:.2}", db.average_gpa());

    println!("\nStudents list:");
    for s in db.list_students() {
        println!("  {} - {} (GPA: {:.2})", s.id, s.name, s.calculate_gpa());
    }
}
