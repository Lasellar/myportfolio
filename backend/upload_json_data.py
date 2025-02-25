from tqdm import tqdm
import json

from backend.settings import DATAFILES_DIR


def open_json(datafile):
    path = DATAFILES_DIR / datafile
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as ex:
        print(ex)
        return


def load_json(datafiles):
    for model, datafile in datafiles:
        data = open_json(datafile)
        if model.__name__ == 'ProjectSkill':
            for obj in tqdm(data, desc=f'CRT ProjectSkill OBJ', colour=''):
                model.objects.get_or_create(
                    project=Project.objects.get(id=obj['project']),
                    skill=Skill.objects.get(title=obj['skillttl'])
                )
            return
        for obj in tqdm(data, desc=f'CRT {model.__name__} OBJ', colour=''):
            model.objects.get_or_create(**obj)


if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    django.setup()
    from main.models import Skill, Project, ProjectSkill, Employer
    DATAFILES = (
        (Skill, 'skills_data.json'),
        (Project, 'projects_data.json'),
        (Employer, 'employers_data.json'),
        (ProjectSkill, 'projects_skills_data.json')
    )
    load_json(DATAFILES)
