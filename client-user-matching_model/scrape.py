import pandas as pd
import numpy as np
import json
import random
from datetime import datetime, timedelta
import os

def generate_dataset(num_freelancers=1000, num_projects=2000):
    print(f"\nGenerating synthetic freelance marketplace dataset...")
    print(f"Creating {num_freelancers} freelancer profiles and {num_projects} projects...")

    # Define comprehensive skill sets by category
    skill_sets = {
        'programming': [
            'Python', 'JavaScript', 'Java', 'C++', 'React', 'Node.js', 
            'SQL', 'Django', 'Angular', 'Vue.js', 'PHP', 'Ruby', 'Swift'
        ],
        'design': [
            'UI Design', 'UX Design', 'Graphic Design', 'Photoshop', 
            'Illustrator', 'Figma', 'Adobe XD', 'Logo Design'
        ],
        'writing': [
            'Content Writing', 'Copywriting', 'Technical Writing', 
            'Blog Writing', 'SEO Writing', 'Creative Writing'
        ],
        'marketing': [
            'Digital Marketing', 'SEO', 'Social Media Marketing', 
            'Email Marketing', 'Content Marketing', 'PPC', 'Analytics'
        ]
    }

    # Generate Freelancer Data
    print("\nGenerating freelancer profiles...")
    freelancers = []
    for i in range(num_freelancers):
        # Select 1-2 main categories for the freelancer
        categories = random.sample(list(skill_sets.keys()), random.randint(1, 2))
        
        # Select 3-7 skills from chosen categories
        skills = []
        for category in categories:
            skills.extend(random.sample(skill_sets[category], 
                                     random.randint(2, 5)))
        
        experience_years = random.randint(1, 15)
        base_rate = 15 + (experience_years * random.randint(3, 10))
        
        freelancer = {
            'freelancer_id': f'FR{i+1:04d}',
            'skills': ', '.join(skills),
            'main_category': categories[0],
            'experience_years': experience_years,
            'hourly_rate': base_rate,
            'rating': round(random.uniform(3.5, 5.0), 1),
            'jobs_completed': random.randint(5, 100),
            'success_rate': round(random.uniform(0.80, 1.0), 2),
            'response_time_hours': round(random.uniform(1, 48), 1),
            'on_time_delivery_rate': round(random.uniform(0.85, 1.0), 2)
        }
        freelancers.append(freelancer)
        
        if (i + 1) % 200 == 0:
            print(f"Generated {i + 1} freelancer profiles...")

    # Generate Project Data
    print("\nGenerating project data...")
    projects = []
    for i in range(num_projects):
        # Select a random category and its skills
        category = random.choice(list(skill_sets.keys()))
        required_skills = random.sample(skill_sets[category], 
                                      random.randint(2, 5))
        
        # Generate project duration and budget
        duration_weeks = random.randint(1, 12)
        complexity = random.choice(['Low', 'Medium', 'High'])
        base_budget = 100 * random.randint(5, 100)
        
        if complexity == 'Medium':
            base_budget *= 1.5
        elif complexity == 'High':
            base_budget *= 2.5

        project = {
            'project_id': f'PJ{i+1:04d}',
            'category': category,
            'required_skills': ', '.join(required_skills),
            'complexity': complexity,
            'duration_weeks': duration_weeks,
            'budget': round(base_budget, 2),
            'required_experience_years': random.randint(1, 8),
            'preferred_hourly_rate_range': f"${random.randint(15, 30)}-${random.randint(31, 100)}",
            'project_description': f"Project requiring expertise in {', '.join(required_skills)}",
            'status': random.choice(['Open', 'In Progress', 'Completed'])
        }
        projects.append(project)
        
        if (i + 1) % 400 == 0:
            print(f"Generated {i + 1} projects...")

    # Create DataFrames
    df_freelancers = pd.DataFrame(freelancers)
    df_projects = pd.DataFrame(projects)

    # Create output directory if it doesn't exist
    output_dir = 'freelance_data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\nCreated directory: {output_dir}")

    # Save to CSV
    freelancers_path = os.path.join(output_dir, 'freelancers.csv')
    projects_path = os.path.join(output_dir, 'projects.csv')
    
    df_freelancers.to_csv(freelancers_path, index=False)
    df_projects.to_csv(projects_path, index=False)

    print("\nDataset generation complete!")
    print(f"Files saved in '{output_dir}' directory:")
    print(f"1. Freelancers data: {freelancers_path}")
    print(f"2. Projects data: {projects_path}")
    
    # Print sample statistics
    print("\nQuick Statistics:")
    print(f"Number of freelancers: {len(df_freelancers)}")
    print(f"Number of projects: {len(df_projects)}")
    print(f"Average freelancer rating: {df_freelancers['rating'].mean():.2f}")
    print(f"Average project budget: ${df_projects['budget'].mean():.2f}")
    
    return df_freelancers, df_projects

if __name__ == "__main__":
    df_freelancers, df_projects = generate_dataset()