import os

badhash = os.environ["badhash"]
goodhash = os.environ["goodhash"]

os.system(f"git bisect start {badhash} {goodhash}")

os.system("git bisect run python manage.py test")

os.system("git bisect reset")
