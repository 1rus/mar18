from setuptools import setup

config = {
    'description': 'Orange HRM Selenium Minutes Framework',
    'author': "Ruslan Rizvanov",
    'url': 'hrm.seleniumminutes.com',
    'download_url': 'github.com',
    'author_email': 'rus4ca@gmail.com',
    'version': '0.1',
    'packages': ['hrm-sm'],
    'scripts': [],
    'name': 'Orange HRM SM'
}

setup(**config,
    setup_requires = ['pytest-runner'],
    tests_require  = ['pytest']
)
