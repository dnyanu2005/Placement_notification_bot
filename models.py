from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import json
from .database import Base

class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    college = Column(String(200), nullable=False)
    branch = Column(String(100), nullable=False) # e.g. Computer Science, Electronics, Information Technology
    current_year = Column(String(50), nullable=False) # e.g. 3rd Year
    graduation_year = Column(Integer, nullable=False) # e.g. 2026 or 2027
    cgpa = Column(Float, nullable=False)
    backlogs = Column(Integer, default=0)
    skills = Column(Text, default="[]") # JSON list of strings
    programming_languages = Column(Text, default="[]") # JSON list of strings
    preferred_roles = Column(Text, default="[]") # JSON list of strings
    preferred_locations = Column(Text, default="[]") # JSON list of strings
    job_type_preference = Column(String(50), default="Both") # Internship, Full-time, Both
    min_package = Column(Float, nullable=True) # LPA
    resume_filename = Column(String(255), nullable=True)
    resume_extracted_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    applications = relationship("Application", back_populates="student", cascade="all, delete-orphan")
    saved_opportunities = relationship("SavedOpportunity", back_populates="student", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="student", cascade="all, delete-orphan")

    def get_skills_list(self):
        try:
            return json.loads(self.skills)
        except Exception:
            return []

    def get_languages_list(self):
        try:
            return json.loads(self.programming_languages)
        except Exception:
            return []

    def get_roles_list(self):
        try:
            return json.loads(self.preferred_roles)
        except Exception:
            return []

    def get_locations_list(self):
        try:
            return json.loads(self.preferred_locations)
        except Exception:
            return []


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(150), nullable=False, index=True)
    job_title = Column(String(200), nullable=False, index=True)
    job_description = Column(Text, nullable=False)
    opportunity_type = Column(String(100), nullable=False, index=True) # On-campus placement, Off-campus placement, Internship, Graduate trainee, Apprenticeship, Full-time job, Part-time opportunity
    
    # Eligibility Criteria
    eligible_branches = Column(Text, default="[]") # JSON list e.g. ["Computer Science", "Information Technology"]
    eligible_academic_years = Column(Text, default="[]") # JSON list of graduation years e.g. [2026, 2027]
    min_cgpa = Column(Float, nullable=True) # None means no minimum requirement published
    max_backlogs = Column(Integer, nullable=True) # None means no backlog criteria published
    required_skills = Column(Text, default="[]") # JSON list e.g. ["Python", "SQL", "React"]
    
    # Logistics
    job_location = Column(String(150), nullable=False) # e.g. "Bengaluru, India" or "Remote"
    work_mode = Column(String(50), default="On-site") # On-site, Remote, Hybrid
    salary_or_stipend = Column(String(100), nullable=True) # e.g. "₹12.0 - ₹18.0 LPA" or "₹45,000 / month"
    
    # Dates
    application_opening_date = Column(String(50), nullable=True) # ISO Date string YYYY-MM-DD
    application_deadline = Column(String(50), nullable=False, index=True) # ISO Date string YYYY-MM-DD
    job_posting_date = Column(String(50), nullable=True) # ISO Date string YYYY-MM-DD
    
    # Official Links & Verification
    official_application_url = Column(String(500), nullable=False)
    official_company_career_url = Column(String(500), nullable=True)
    source_url = Column(String(500), nullable=True)
    source_name = Column(String(150), default="Official Portal")
    source_verification_status = Column(String(50), default="verified") # verified, unverified, pending
    data_mode = Column(String(20), default="demo") # demo, live
    
    last_verified_timestamp = Column(DateTime, default=datetime.utcnow)
    created_timestamp = Column(DateTime, default=datetime.utcnow)
    updated_timestamp = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    applications = relationship("Application", back_populates="opportunity", cascade="all, delete-orphan")
    saved_by = relationship("SavedOpportunity", back_populates="opportunity", cascade="all, delete-orphan")
    link_clicks = relationship("ApplicationLinkClick", back_populates="opportunity", cascade="all, delete-orphan")

    def get_branches(self):
        try:
            return json.loads(self.eligible_branches)
        except Exception:
            return []

    def get_years(self):
        try:
            return json.loads(self.eligible_academic_years)
        except Exception:
            return []

    def get_skills(self):
        try:
            return json.loads(self.required_skills)
        except Exception:
            return []


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"), nullable=False)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"), nullable=False)
    status = Column(String(50), default="Interested") # Interested, Planning to Apply, Applied, Assessment Scheduled, Interview Scheduled, Selected, Rejected, Withdrawn
    applied_date = Column(String(50), nullable=True)
    interview_date = Column(String(50), nullable=True)
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student = relationship("StudentProfile", back_populates="applications")
    opportunity = relationship("Opportunity", back_populates="applications")


class SavedOpportunity(Base):
    __tablename__ = "saved_opportunities"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"), nullable=False)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("StudentProfile", back_populates="saved_opportunities")
    opportunity = relationship("Opportunity", back_populates="saved_by")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"), nullable=False)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"), nullable=True)
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    category = Column(String(50), default="general") # urgent, closing_soon, new_match, eligibility_change, general
    deadline_date = Column(String(50), nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("StudentProfile", back_populates="notifications")


class ApplicationLinkClick(Base):
    __tablename__ = "application_link_clicks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student_profiles.id"), nullable=True)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"), nullable=False)
    clicked_at = Column(DateTime, default=datetime.utcnow)
    user_agent = Column(String(255), nullable=True)

    opportunity = relationship("Opportunity", back_populates="link_clicks")
