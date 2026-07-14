from extensions import db

USER_ROLE_ENUM = db.Enum("admin","company","student")
STUDENT_GENDER_ENUM = db.Enum("male","female","other")
JOB_MODE_ENUM = db.Enum("office","remote","hybrid")
APPLICATION_STATUS_ENUM = db.Enum("applied", "shortlisted", "selected", "rejected")

# users -> (admin, company, student)
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(USER_ROLE_ENUM, nullable=False, default="student")
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_blacklisted = db.Column(db.Boolean, nullable=False, default=False)

    company = db.relationship("Company", backref="user", uselist=False, cascade="all, delete-orphan")
    student = db.relationship("Student", backref="user", uselist=False, cascade="all, delete-orphan")

# when admin approved -> only then company can logged in !
# (hr_contact, website_url) -> can be NULL
class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    hr_contact = db.Column(db.String(10), nullable=True)
    website_url = db.Column(db.Text, nullable=True)
    
    is_approved = db.Column(db.Boolean, nullable=False, default=False)

    placement_drives = db.relationship("PlacementDrive", backref="company", cascade="all, delete-orphan")

# resume_url -> can be NULL
class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    gender = db.Column(STUDENT_GENDER_ENUM,nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    department = db.Column(db.Text, nullable=False)
    cgpa = db.Column(db.Numeric(3,2), nullable=False)
    resume_url = db.Column(db.Text, nullable=True)
    is_placed = db.Column(db.Boolean, nullable=False, default=False)

    applications = db.relationship("Application", backref="student", cascade="all, delete-orphan")

# location -> can be NULL (when job_mode -> remote)
# (is_approved: True) -> bcz only approved companies can login -> hence create drive -> but admin can disapprove placement_drive
class PlacementDrive(db.Model):
    __tablename__ = "placement_drives"

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)
    job_title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    job_mode = db.Column(JOB_MODE_ENUM, nullable=False, default="office")
    location = db.Column(db.String(80), nullable=True)
    minimum_cgpa = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    is_approved = db.Column(db.Boolean, nullable=False, default=True)

    applications = db.relationship("Application", backref="placement_drive", cascade="all, delete-orphan")

# (interview_date) -> can be NULL
class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    placement_drive_id = db.Column(db.Integer, db.ForeignKey("placement_drives.id"), nullable=False)
    applied_date = db.Column(db.Date, nullable=False)
    application_status = db.Column(APPLICATION_STATUS_ENUM, nullable=False, default="applied")
    interview_date = db.Column(db.Date, nullable=True)