import datetime

from django.shortcuts import render

from .models import Project, Skill, Employer
from .utils import get_exp


def main_page(request):
    template = 'main/index.html'
    projects = Project.objects.filter(is_published=True)
    skills = Skill.objects.filter(is_published=True)
    employers = Employer.objects.filter(is_published=True)
    exp_from = datetime.datetime(year=2023, month=6, day=1)
    exp_now = datetime.datetime.now()
    experience = get_exp(exp_from, exp_now)
    projects_list = []
    for project in projects:
        project_dict = {
            'project': project, 'skills': project.skills.all()
        }
        projects_list.append(project_dict)
    context = {
        'projects': projects_list,
        'skills': skills,
        'employers': employers,
        'experience': experience
    }
    return render(request, template, context)


def about_page(request):
    template = 'main/about-me.html'
    return render(request, template)


def hobbies_page(request):
    template = 'main/hobbies.html'
    return render(request, template)
