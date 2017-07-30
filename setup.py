from setuptools import setup

setup(name='onkyo-button',
      version='1.1',
      description='control Onkyo recievers from a GPIO button on a Raspberry Pi',
      url='https://github.com/szaske/onkyo-button.git',
      author='Steve Zaske',
      author_email='steve@zaske.com',
      license='MIT',
      packages=['onkyo-button'],
      install_requires=[
          'onkyo-eiscp',
	  'psutil",
	  'RPi.GPIO'
      ],
      zip_safe=False)