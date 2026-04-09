from database import StudentDB

DB_STRING = "postgresql://postgres:gfhjkm2013@localhost:5432/SQL"
db = StudentDB(DB_STRING)


def test_add_student():
    db.add_student(user_id=99, level='Beginner',
                   education_form='Full-time', subject_id=999)

    student = db.get_student(99, 999)
    assert student is not None, "Студент не добавился"
    assert student['level'] == 'Beginner', f"Уровень неправильный: {
        student['level']}"
    assert student['education_form'] == 'Full-time', f"Форма неправильная: {
        student['education_form']}"

    db.delete_student(user_id=99, subject_id=999)


def test_update_student():

    db.add_student(user_id=99, level='Beginner', education_form='Full-time',
                   subject_id=999)

    db.update_student_level(user_id=99, subject_id=999, new_level='Advanced')

    student = db.get_student(99, 999)
    assert student is not None, "Студент пропал после обновления"
    assert student['level'] == 'Advanced', f"Уровень не изменился: {
        student['level']}"

    db.delete_student(user_id=99, subject_id=999)


def test_delete_student():

    db.add_student(user_id=99, level='Beginner', education_form='Full-time',
                   subject_id=999)

    student = db.get_student(99, 999)
    assert student is not None, "Студент не создался перед тестом"

    db.delete_student(user_id=99, subject_id=999)

    student = db.get_student(99, 999)
    assert student is None, "Студент не удалился"


if __name__ == "__main__":
    test_add_student()
    test_update_student()
    test_delete_student()
    print("🎉 Все тесты пройдены!")
