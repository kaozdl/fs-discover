import os
import platform

from files.models import File, Tag

SEPARATOR = "/" if platform.system() in ["Linux", "Darwin"] else "\\"

def discover_shell(path: str = ""):
    if not os.path.isdir(path):
        print("Path is not a directory")
        return

    for file in os.listdir(path):
        path = f"{path}{SEPARATOR}{file}"
        print(f"{path}\n")


def tag_file(path: str, tag_name: str):
    
    file, _ = File.objects.get_or_create(path=path)

    file_tags = file.tags.all().values_list('name', flat=True)
    if tag_name not in file_tags:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        file.tags.add(tag)


def remove_tag(path: str, tag_name: str):
    file = File.objects.filter(path=path).first()
    tag = file.tags.filter(name=tag_name).first()
    if tag is not None:
        file.tags.remove(tag)


def print_file_tags(path: str):
    file = File.objects.filter(path=path).first()
    print(f"{file.path}\n")
    for tag in file.tags.all():
        print(f"|_ {tag.name}")
            

