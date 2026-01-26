import os
from pathlib import Path

def detect_missing_translations(base_dir, target_lang="pt-br"):
    skills_dir = Path(base_dir) / "skills"
    target_dir = skills_dir / target_lang
    
    # Get all active skills (top level, excluding target_lang and hidden)
    all_skills = [d.name for d in skills_dir.iterdir() 
                  if d.is_dir() and not d.name.startswith('.') and d.name != target_lang]
    
    # Check for categories (e.g., game-development)
    # For simplicity, we'll assume skills are either top-level or one level deep in categories
    # However, the current pt-br structure is flat under skills/pt-br/
    
    missing = []
    translated = []
    
    if target_dir.exists():
        translated = [d.name for d in target_dir.iterdir() if d.is_dir()]
    
    for skill in all_skills:
        if skill not in translated:
            # Special case: check if it's a category folder
            skill_path = skills_dir / skill
            if (skill_path / "SKILL.md").exists():
                missing.append(skill)
            else:
                # It might be a category folder
                sub_skills = [s.name for s in skill_path.iterdir() if s.is_dir() and (skill_path / s / "SKILL.md").exists()]
                for sub in sub_skills:
                    full_id = f"{skill}/{sub}"
                    # Check if translated version exists (we use flat names in pt-br for now, or we should mirror?)
                    # If we follow the current clean-code -> pt-br/clean-code, it's flat.
                    if sub not in translated:
                        missing.append(full_id)

    return missing, translated

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent
    missing, translated = detect_missing_translations(base_dir)
    
    print(f"📊 Translation Status (pt-br):")
    print(f"✅ Translated: {len(translated)}")
    print(f"❌ Missing: {len(missing)}")
    
    if missing:
        print("\nTop 10 Missing Skills:")
        for m in missing[:10]:
            print(f"  - {m}")
        
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more.")
