from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

# ==================== Profile Schemas ====================

class StudentProfileBase(BaseModel):
    name: str = Field(..., example="Aarav Sharma")
    college: str = Field(..., example="RV College of Engineering")
    branch: str = Field(..., example="Computer Science and Engineering")
    current_year: str = Field(..., example="3rd Year")
    graduation_year: int = Field(..., example=2027)
    cgpa: float = Field(..., ge=0.0, le=10.0, example=8.65)
    backlogs: int = Field(0, ge=0, example=0)
    skills: List[str] = Field(default_factory=list, example=["Python", "SQL", "React", "Data Structures and Algorithms"])
    programming_languages: List[str] = Field(default_factory=list, example=["Python", "Java", "C++"])
    preferred_roles: List[str] = Field(default_factory=list, example=["Software Engineer", "AI/ML Engineer"])
    preferred_locations: List[str] = Field(default_factory=list, example=["Bengaluru", "Hyderabad", "Remote"])
    job_type_preference: str = Field("Both", example="Both")
    min_package: Optional[float] = Field(None, example=8.0)

class StudentProfileCreate(StudentProfileBase):
    pass

class StudentProfileUpdate(BaseModel):
    name: Optional[str] = None
    college: Optional[str] = None
    branch: Optional[str] = None
    current_year: Optional[str] = None
    graduation_year: Optional[int] = None
    cgpa: Optional[float] = None
    backlogs: Optional[int] = None
    skills: Optional[List[str]] = None
    programming_languages: Optional[List[str]] = None
    preferred_roles: Optional[List[str]] = None
    preferred_locations: Optional[List[str]] = None
    job_type_preference: Optional[str] = None
    min_package: Optional[float] = None

class StudentProfileOut(StudentProfileBase):
    id: int
    resume_filename: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==================== Eligibility & Matching Schemas ====================

class EligibilityAssessment(BaseModel):
    status: str # "eligible" | "not_eligible" | "eligibility_unknown"
    status_label: str # "Eligible" | "Not Eligible" | "Eligibility needs verification"
    reasons: List[str] = [] # Why ineligible or missing info
    is_gate_passed: bool
    match_score: Optional[int] = None # 0 to 100
    why_it_matches: List[str] = []
    skills_to_improve: List[str] = []
    recommended_topics: List[str] = []
    deadline_status: str # "urgent" | "closing_soon" | "open" | "closed"
    days_remaining: int
    disclaimer: str = "Match score is an algorithmic estimate based on your profile and is not a hiring probability or guarantee."


# ==================== Opportunity Schemas ====================

class OpportunityBase(BaseModel):
    company_name: str
    job_title: str
    job_description: str
    opportunity_type: str # On-campus placement, Off-campus placement, Internship, Graduate trainee, Apprenticeship, Full-time job, Part-time opportunity
    eligible_branches: List[str] = []
    eligible_academic_years: List[int] = []
    min_cgpa: Optional[float] = None
    max_backlogs: Optional[int] = None
    required_skills: List[str] = []
    job_location: str
    work_mode: str = "On-site"
    salary_or_stipend: Optional[str] = None
    application_opening_date: Optional[str] = None
    application_deadline: str # YYYY-MM-DD
    job_posting_date: Optional[str] = None
    official_application_url: str
    official_company_career_url: Optional[str] = None
    source_url: Optional[str] = None
    source_name: str = "Official Career Portal"
    source_verification_status: str = "verified"
    data_mode: str = "demo"

class OpportunityCreate(OpportunityBase):
    pass

class OpportunityUpdate(BaseModel):
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    job_description: Optional[str] = None
    opportunity_type: Optional[str] = None
    eligible_branches: Optional[List[str]] = None
    eligible_academic_years: Optional[List[int]] = None
    min_cgpa: Optional[float] = None
    max_backlogs: Optional[int] = None
    required_skills: Optional[List[str]] = None
    job_location: Optional[str] = None
    work_mode: Optional[str] = None
    salary_or_stipend: Optional[str] = None
    application_opening_date: Optional[str] = None
    application_deadline: Optional[str] = None
    official_application_url: Optional[str] = None
    official_company_career_url: Optional[str] = None
    source_url: Optional[str] = None
    source_name: Optional[str] = None
    source_verification_status: Optional[str] = None
    data_mode: Optional[str] = None

class OpportunityOut(BaseModel):
    id: int
    company_name: str
    job_title: str
    job_description: str
    opportunity_type: str
    eligible_branches: List[str]
    eligible_academic_years: List[int]
    min_cgpa: Optional[float] = None
    max_backlogs: Optional[int] = None
    required_skills: List[str]
    job_location: str
    work_mode: str
    salary_or_stipend: Optional[str] = None
    application_opening_date: Optional[str] = None
    application_deadline: str
    job_posting_date: Optional[str] = None
    official_application_url: str
    official_company_career_url: Optional[str] = None
    source_url: Optional[str] = None
    source_name: str
    source_verification_status: str
    data_mode: str
    last_verified_timestamp: datetime
    created_timestamp: datetime
    updated_timestamp: datetime

    class Config:
        from_attributes = True

class OpportunityWithAssessment(OpportunityOut):
    assessment: EligibilityAssessment
    is_saved: bool = False
    application_status: Optional[str] = None


# ==================== Application Tracker Schemas ====================

class ApplicationCreate(BaseModel):
    opportunity_id: int
    status: str = "Interested"
    applied_date: Optional[str] = None
    interview_date: Optional[str] = None
    notes: Optional[str] = ""

class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    applied_date: Optional[str] = None
    interview_date: Optional[str] = None
    notes: Optional[str] = None

class ApplicationOut(BaseModel):
    id: int
    student_id: int
    opportunity_id: int
    status: str
    applied_date: Optional[str] = None
    interview_date: Optional[str] = None
    notes: Optional[str] = ""
    created_at: datetime
    updated_at: datetime
    opportunity: Optional[OpportunityOut] = None

    class Config:
        from_attributes = True


# ==================== Saved Opportunities ====================

class SavedOpportunityOut(BaseModel):
    id: int
    student_id: int
    opportunity_id: int
    created_at: datetime
    opportunity: OpportunityOut

    class Config:
        from_attributes = True


# ==================== Notifications ====================

class NotificationOut(BaseModel):
    id: int
    student_id: int
    opportunity_id: Optional[int] = None
    title: str
    message: str
    category: str
    deadline_date: Optional[str] = None
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


# ==================== Chatbot Schemas ====================

class ChatMessageRequest(BaseModel):
    message: str
    opportunity_id: Optional[int] = None # Optional context when chatting about a specific role

class ChatOpportunityCard(BaseModel):
    id: int
    company_name: str
    job_title: str
    opportunity_type: str
    job_location: str
    salary_or_stipend: Optional[str] = None
    application_deadline: str
    official_application_url: str
    source_verification_status: str
    match_score: Optional[int] = None
    eligibility_status: str

class ChatMessageResponse(BaseModel):
    response: str
    matching_opportunities: List[ChatOpportunityCard] = []
    extracted_filters: Dict[str, Any] = {}
    is_ai_fallback: bool = False


# ==================== Interview Preparation Schemas ====================

class AptitudeQuestionOut(BaseModel):
    id: str
    category: str # "Quantitative", "Logical", "Verbal"
    question: str
    options: List[str]
    correct_option: int # index 0-3
    explanation: str

class MockInterviewStartRequest(BaseModel):
    role_or_title: str
    opportunity_id: Optional[int] = None
    difficulty: str = "Medium" # "Beginner", "Medium", "Advanced"

class MockInterviewQuestionOut(BaseModel):
    question_index: int
    total_questions: int
    question: str
    category: str
    target_role: str
    context_hint: Optional[str] = None

class MockInterviewEvaluateRequest(BaseModel):
    question: str
    answer: str
    target_role: str
    question_index: int

class MockInterviewEvaluationOut(BaseModel):
    indicative_score: int # 1 to 10
    strengths: List[str]
    areas_for_improvement: List[str]
    ideal_answer_summary: str
    disclaimer: str = "This is practice feedback designed for learning, not an official company evaluation or selection guarantee."


# ==================== Resume Analysis Schemas ====================

class ResumeAnalysisResponse(BaseModel):
    extracted_skills: List[str]
    detected_education: Dict[str, Any]
    detected_projects: List[str]
    recommended_opportunities: List[OpportunityWithAssessment]
    skill_gaps: List[str]
    total_text_length: int
