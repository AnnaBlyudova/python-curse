from sqlalchemy import create_engine, text


class StudentDB:
    def __init__(self, db_connection_string):
        self.engine = create_engine(db_connection_string)

    def get_student(self, user_id, subject_id):
        with self.engine.connect() as conn:
            result = conn.execute(text("""
                SELECT * FROM student
                WHERE user_id = :user_id AND subject_id = :subject_id
            """), {
                "user_id": user_id,
                "subject_id": subject_id
            })
            rows = result.mappings().all()
            return rows[0] if rows else None

    def add_student(self, user_id, level, education_form, subject_id):
        with self.engine.connect() as conn:
            conn.execute(text("""
                INSERT INTO student(user_id, level, education_form, subject_id)
                VALUES (:user_id, :level, :education_form, :subject_id)
            """), {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            })
            conn.commit()

    def update_student_level(self, user_id, subject_id, new_level):
        with self.engine.connect() as conn:
            conn.execute(text("""
                UPDATE student
                SET level = :new_level
                WHERE user_id = :user_id AND subject_id = :subject_id
            """), {
                "user_id": user_id,
                "subject_id": subject_id,
                "new_level": new_level
            })
            conn.commit()

    def delete_student(self, user_id, subject_id):
        with self.engine.connect() as conn:
            conn.execute(text("""
                DELETE FROM student
                WHERE user_id = :user_id AND subject_id = :subject_id
            """), {
                "user_id": user_id,
                "subject_id": subject_id
            })
            conn.commit()
