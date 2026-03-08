def check_ai_readiness(skill_level):
    if skill_level > 7:
        return "Ready for GenAI!"
    else:
        return "Keep practicing Python."


# Loop through a list of skills
skills = ["Python", "Pandas", "Logic"]
for skill in skills:
    print(f"Learning: {skill}")

print(check_ai_readiness(8))
