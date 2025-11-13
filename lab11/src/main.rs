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
        // Reference additional fields to avoid unused-field warnings
        println!("  {} - {} <{}> (GPA: {:.2})", s.id, s.name, s.email, s.calculate_gpa());
        // Print transcript details (uses course_code and course_name)
        if !s.grades.is_empty() {
            println!("    Transcript:");
            for cg in &s.grades {
                println!("      {} - {}: {:?} ({:.1} quality points)",
                    cg.course_code, cg.course_name, cg.grade, cg.quality_points());
            }
        }
    }

    // Demonstrate mutable lookup and update using find_student_mut
    if let Some(student_mut) = db.find_student_mut("S001") {
        student_mut.add_credits(3);
        println!("\nUpdated credits for {}: {}", student_mut.id, student_mut.credits_earned);
    }
}
