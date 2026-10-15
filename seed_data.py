from datetime import datetime, timedelta
import json
from sqlalchemy.orm import Session
from .models import Opportunity, StudentProfile, Application, SavedOpportunity, Notification

def seed_database(db: Session):
    # Only seed if no opportunities exist
    if db.query(Opportunity).count() > 0:
        return

    today = datetime.utcnow().date()

    opportunities_data = [
        {
            "company_name": "Google",
            "job_title": "Software Engineering Intern - Summer 2027",
            "job_description": "Google software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. You will work on scalable algorithms, distributed systems, and real-time processing pipelines.",
            "opportunity_type": "Internship",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Electronics and Communication"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 8.0,
            "max_backlogs": 0,
            "required_skills": ["Data Structures and Algorithms", "C++", "Java", "Python"],
            "job_location": "Bengaluru / Hyderabad, India",
            "work_mode": "Hybrid",
            "salary_or_stipend": "₹1,25,000 / month",
            "application_opening_date": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=2)).strftime("%Y-%m-%d"), # Urgent (<3 days)
            "job_posting_date": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
            "official_application_url": "https://careers.google.com/jobs/results/",
            "official_company_career_url": "https://careers.google.com/",
            "source_url": "https://careers.google.com/jobs/results/",
            "source_name": "Google Careers Official Portal",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Microsoft",
            "job_title": "Software Engineer (Full-Time - Campus Drive)",
            "job_description": "Join Microsoft's Core Services Engineering & Operations (CSEO) or Azure Cloud. Design, implement, test, and ship resilient software products operating on a planetary scale.",
            "opportunity_type": "On-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Electronics and Communication"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 7.5,
            "max_backlogs": 0,
            "required_skills": ["Data Structures and Algorithms", "C#", "C++", "Cloud Computing", "Object-Oriented Programming"],
            "job_location": "Hyderabad / Bengaluru / Noida",
            "work_mode": "Hybrid",
            "salary_or_stipend": "₹28.0 - ₹34.0 LPA",
            "application_opening_date": (today - timedelta(days=14)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=5)).strftime("%Y-%m-%d"), # Closing Soon (3-7 days)
            "job_posting_date": (today - timedelta(days=14)).strftime("%Y-%m-%d"),
            "official_application_url": "https://careers.microsoft.com/students/us/en",
            "official_company_career_url": "https://careers.microsoft.com/",
            "source_url": "https://careers.microsoft.com/students/us/en",
            "source_name": "Microsoft University Recruiting",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Amazon",
            "job_title": "Software Development Engineer 1 (SDE-1)",
            "job_description": "Amazon is seeking ambitious graduates to build highly scalable backend microservices, real-time catalog ranking, and AWS cloud-native fulfillment architectures.",
            "opportunity_type": "Off-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Electronics and Communication", "Electrical Engineering"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 7.0,
            "max_backlogs": 0,
            "required_skills": ["Java", "Data Structures and Algorithms", "SQL", "System Design", "AWS"],
            "job_location": "Bengaluru / Hyderabad / Chennai",
            "work_mode": "On-site",
            "salary_or_stipend": "₹25.0 - ₹32.0 LPA",
            "application_opening_date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=12)).strftime("%Y-%m-%d"), # Open (>7 days)
            "job_posting_date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
            "official_application_url": "https://www.amazon.jobs/en/job_categories/software-development",
            "official_company_career_url": "https://www.amazon.jobs/",
            "source_url": "https://www.amazon.jobs/en/job_categories/software-development",
            "source_name": "Amazon Jobs Portal",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Cisco Systems",
            "job_title": "Software Consulting Engineer - Campus 2026/2027",
            "job_description": "Design, automate, and secure enterprise networking and cloud infrastructure. Hands-on scripting with Python, Linux internals, network protocols, and containerized deployments.",
            "opportunity_type": "On-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Electronics and Communication"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 7.5,
            "max_backlogs": 0,
            "required_skills": ["Python", "Computer Networks", "Linux", "C++"],
            "job_location": "Bengaluru, India",
            "work_mode": "Hybrid",
            "salary_or_stipend": "₹15.5 - ₹19.0 LPA",
            "application_opening_date": (today - timedelta(days=6)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=4)).strftime("%Y-%m-%d"), # Closing Soon
            "job_posting_date": (today - timedelta(days=6)).strftime("%Y-%m-%d"),
            "official_application_url": "https://jobs.cisco.com/jobs/SearchJobs/software",
            "official_company_career_url": "https://www.cisco.com/c/en/us/about/careers.html",
            "source_url": "https://jobs.cisco.com",
            "source_name": "Campus Placement Cell Notice Board",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Oracle Corporation",
            "job_title": "Associate Software Applications Developer",
            "job_description": "Build resilient enterprise applications powering Oracle Cloud Infrastructure (OCI). Requires solid understanding of Core Java, Relational Databases, and Microservices.",
            "opportunity_type": "On-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 7.0,
            "max_backlogs": 0,
            "required_skills": ["Java", "SQL", "Spring Boot", "Data Structures and Algorithms"],
            "job_location": "Hyderabad / Bengaluru",
            "work_mode": "Hybrid",
            "salary_or_stipend": "₹16.0 - ₹20.0 LPA",
            "application_opening_date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=1)).strftime("%Y-%m-%d"), # Urgent (1 day)
            "job_posting_date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
            "official_application_url": "https://careers.oracle.com/students",
            "official_company_career_url": "https://www.oracle.com/corporate/careers",
            "source_url": "https://careers.oracle.com",
            "source_name": "Oracle Early Career Recruitment",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Qualcomm",
            "job_title": "Interim Engineering Intern - Wireless & Embedded Systems",
            "job_description": "Work on Qualcomm's Snapdragon processors, 5G wireless protocol stacks, and low-level Linux driver development in our Bengaluru R&D center.",
            "opportunity_type": "Internship",
            "eligible_branches": ["Electronics and Communication", "Computer Science and Engineering", "Electrical Engineering"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 7.5,
            "max_backlogs": 0,
            "required_skills": ["C++", "C", "Embedded Systems", "Operating Systems", "Python"],
            "job_location": "Bengaluru / Hyderabad, India",
            "work_mode": "On-site",
            "salary_or_stipend": "₹55,000 / month",
            "application_opening_date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=16)).strftime("%Y-%m-%d"), # Open
            "job_posting_date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
            "official_application_url": "https://qualcomm.wd5.myworkdayjobs.com/External",
            "official_company_career_url": "https://www.qualcomm.com/company/careers",
            "source_url": "https://qualcomm.wd5.myworkdayjobs.com",
            "source_name": "Qualcomm Careers",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Adobe",
            "job_title": "Quality Engineering & Automation Specialist",
            "job_description": "Join Adobe Creative Cloud engineering team. Build test automation frameworks, write CI/CD test pipelines, and ensure pixel-perfect rendering for millions of graphic creators.",
            "opportunity_type": "Off-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Electronics and Communication"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 7.0,
            "max_backlogs": 0,
            "required_skills": ["Python", "Selenium", "JavaScript", "Docker", "Git"],
            "job_location": "Noida / Bengaluru",
            "work_mode": "Hybrid",
            "salary_or_stipend": "₹16.0 - ₹21.0 LPA",
            "application_opening_date": (today - timedelta(days=8)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=6)).strftime("%Y-%m-%d"), # Closing Soon
            "job_posting_date": (today - timedelta(days=8)).strftime("%Y-%m-%d"),
            "official_application_url": "https://careers.adobe.com/us/en/university",
            "official_company_career_url": "https://careers.adobe.com/",
            "source_url": "https://careers.adobe.com/us/en/university",
            "source_name": "Adobe University Careers",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Tata Consultancy Services (TCS)",
            "job_title": "TCS Digital Cadre - Advanced Software Engineer",
            "job_description": "TCS Digital offers elite engineering graduates high-impact positions in AI/ML, Cloud Solutions, IoT, Blockchain, and Cybersecurity. Selection based on TCS NQT examination.",
            "opportunity_type": "On-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Electronics and Communication", "Mechanical Engineering", "Electrical Engineering"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 6.5,
            "max_backlogs": 1,
            "required_skills": ["Python", "Java", "SQL", "Data Structures and Algorithms", "Problem Solving"],
            "job_location": "Pan India (Bengaluru, Pune, Hyderabad, Mumbai, Delhi)",
            "work_mode": "Hybrid",
            "salary_or_stipend": "₹7.0 - ₹9.0 LPA",
            "application_opening_date": (today - timedelta(days=20)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=22)).strftime("%Y-%m-%d"), # Open
            "job_posting_date": (today - timedelta(days=20)).strftime("%Y-%m-%d"),
            "official_application_url": "https://nextstep.tcs.com/campus/#/",
            "official_company_career_url": "https://www.tcs.com/careers",
            "source_url": "https://nextstep.tcs.com",
            "source_name": "TCS NextStep Official Portal",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Infosys",
            "job_title": "Specialist Programmer (SP)",
            "job_description": "Infosys Specialist Programmer role focuses on high-end coding, competitive programming, full-stack architecture, and building digital transformation solutions for global Fortune 500 enterprises.",
            "opportunity_type": "On-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Electronics and Communication"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 6.8,
            "max_backlogs": 0,
            "required_skills": ["Java", "Python", "Data Structures and Algorithms", "Competitive Programming", "DBMS"],
            "job_location": "Mysuru / Bengaluru / Pune",
            "work_mode": "On-site",
            "salary_or_stipend": "₹9.5 - ₹11.0 LPA",
            "application_opening_date": (today - timedelta(days=12)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=18)).strftime("%Y-%m-%d"), # Open
            "job_posting_date": (today - timedelta(days=12)).strftime("%Y-%m-%d"),
            "official_application_url": "https://www.infosys.com/careers.html",
            "official_company_career_url": "https://www.infosys.com/careers.html",
            "source_url": "https://www.infosys.com/careers.html",
            "source_name": "Infosys Early Careers",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Swiggy",
            "job_title": "Software Development Engineer 1 (Backend - Freshers)",
            "job_description": "Scale Swiggy's high-throughput order dispatch, routing, and payment orchestration services handling millions of peak requests per second.",
            "opportunity_type": "Off-campus placement",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 7.0,
            "max_backlogs": 0,
            "required_skills": ["Java", "Go", "Distributed Systems", "SQL", "Redis"],
            "job_location": "Bengaluru, India",
            "work_mode": "Hybrid",
            "salary_or_stipend": "₹18.0 - ₹24.0 LPA",
            "application_opening_date": (today - timedelta(days=4)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=3)).strftime("%Y-%m-%d"), # Urgent (3 days)
            "job_posting_date": (today - timedelta(days=4)).strftime("%Y-%m-%d"),
            "official_application_url": "https://careers.swiggy.com/#/careers",
            "official_company_career_url": "https://careers.swiggy.com",
            "source_url": "https://careers.swiggy.com",
            "source_name": "Swiggy Careers Portal",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Larsen & Toubro (L&T)",
            "job_title": "Graduate Engineer Trainee (GET) - Digital & Systems",
            "job_description": "L&T GET program provides immersive rotational engineering exposure in smart manufacturing, SCADA systems, industrial IoT, and embedded control engineering.",
            "opportunity_type": "Graduate trainee",
            "eligible_branches": ["Electrical Engineering", "Electronics and Communication", "Mechanical Engineering", "Computer Science and Engineering"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 6.5,
            "max_backlogs": 0,
            "required_skills": ["Python", "C++", "IoT", "MATLAB", "Industrial Automation"],
            "job_location": "Mumbai / Chennai / Vadodara",
            "work_mode": "On-site",
            "salary_or_stipend": "₹6.5 - ₹8.0 LPA",
            "application_opening_date": (today - timedelta(days=15)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=25)).strftime("%Y-%m-%d"), # Open
            "job_posting_date": (today - timedelta(days=15)).strftime("%Y-%m-%d"),
            "official_application_url": "https://www.larsentoubro.com/corporate/careers/",
            "official_company_career_url": "https://www.larsentoubro.com/corporate/careers/",
            "source_url": "https://www.larsentoubro.com",
            "source_name": "L&T Graduate Campus Program",
            "source_verification_status": "verified",
            "data_mode": "demo"
        },
        {
            "company_name": "Goldman Sachs",
            "job_title": "Summer Analyst - Global Investment Research & Tech",
            "job_description": "Work with quantitative engineers building real-time pricing models, risk calculation microservices, and high-frequency execution pipelines.",
            "opportunity_type": "Internship",
            "eligible_branches": ["Computer Science and Engineering", "Information Technology", "Mathematics and Computing", "Electronics and Communication"],
            "eligible_academic_years": [2026, 2027],
            "min_cgpa": 8.0,
            "max_backlogs": 0,
            "required_skills": ["Python", "C++", "Data Structures and Algorithms", "SQL", "Statistics"],
            "job_location": "Bengaluru, India",
            "work_mode": "On-site",
            "salary_or_stipend": "₹1,00,000 / month",
            "application_opening_date": (today - timedelta(days=11)).strftime("%Y-%m-%d"),
            "application_deadline": (today + timedelta(days=5)).strftime("%Y-%m-%d"), # Closing soon
            "job_posting_date": (today - timedelta(days=11)).strftime("%Y-%m-%d"),
            "official_application_url": "https://www.goldmansachs.com/careers/students/programs/",
            "official_company_career_url": "https://www.goldmansachs.com/careers/",
            "source_url": "https://www.goldmansachs.com",
            "source_name": "Goldman Sachs Student Programs",
            "source_verification_status": "verified",
            "data_mode": "demo"
        }
    ]

    for item in opportunities_data:
        opp = Opportunity(
            company_name=item["company_name"],
            job_title=item["job_title"],
            job_description=item["job_description"],
            opportunity_type=item["opportunity_type"],
            eligible_branches=json.dumps(item["eligible_branches"]),
            eligible_academic_years=json.dumps(item["eligible_academic_years"]),
            min_cgpa=item["min_cgpa"],
            max_backlogs=item["max_backlogs"],
            required_skills=json.dumps(item["required_skills"]),
            job_location=item["job_location"],
            work_mode=item["work_mode"],
            salary_or_stipend=item["salary_or_stipend"],
            application_opening_date=item["application_opening_date"],
            application_deadline=item["application_deadline"],
            job_posting_date=item["job_posting_date"],
            official_application_url=item["official_application_url"],
            official_company_career_url=item["official_company_career_url"],
            source_url=item["source_url"],
            source_name=item["source_name"],
            source_verification_status=item["source_verification_status"],
            data_mode=item["data_mode"],
            last_verified_timestamp=datetime.utcnow()
        )
        db.add(opp)

    db.commit()

    # Seed an exemplary default student profile for instant presentation readiness
    if db.query(StudentProfile).count() == 0:
        demo_student = StudentProfile(
            name="Rahul Sharma",
            college="RV College of Engineering",
            branch="Computer Science and Engineering",
            current_year="3rd Year",
            graduation_year=2027,
            cgpa=8.45,
            backlogs=0,
            skills=json.dumps(["Python", "Java", "SQL", "React", "Data Structures and Algorithms", "Machine Learning"]),
            programming_languages=json.dumps(["Python", "Java", "C++", "JavaScript"]),
            preferred_roles=json.dumps(["Software Engineer", "AI/ML Engineer", "Web Developer"]),
            preferred_locations=json.dumps(["Bengaluru", "Hyderabad", "Remote"]),
            job_type_preference="Both",
            min_package=10.0,
            created_at=datetime.utcnow()
        )
        db.add(demo_student)
        db.commit()
        db.refresh(demo_student)

        # Seed sample saved opportunities and tracker application for demonstration
        opps = db.query(Opportunity).all()
        if opps:
            # Save Google and Microsoft
            db.add(SavedOpportunity(student_id=demo_student.id, opportunity_id=opps[0].id))
            db.add(SavedOpportunity(student_id=demo_student.id, opportunity_id=opps[1].id))
            
            # Application tracker entry for Amazon and Cisco
            db.add(Application(
                student_id=demo_student.id,
                opportunity_id=opps[2].id, # Amazon
                status="Applied",
                applied_date=(today - timedelta(days=3)).strftime("%Y-%m-%d"),
                interview_date=(today + timedelta(days=10)).strftime("%Y-%m-%d"),
                notes="Online assessment completed on Amazon HackerRank. Scored 100% on both coding problems."
            ))
            db.add(Application(
                student_id=demo_student.id,
                opportunity_id=opps[3].id, # Cisco
                status="Assessment Scheduled",
                applied_date=(today - timedelta(days=2)).strftime("%Y-%m-%d"),
                interview_date=(today + timedelta(days=3)).strftime("%Y-%m-%d"),
                notes="Cognitive aptitude & technical networking round scheduled for Friday 10:00 AM."
            ))
            db.commit()
