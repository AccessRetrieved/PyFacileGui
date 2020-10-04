from distutils.core import setup
setup(
  name = 'PyGui',         # How you named your package folder (MyLib)
  packages = ['PyGui'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simpler life with most modules combined.',   # Give a short description about your library
  author = 'Jerry Hu',                   # Type in your name
  author_email = 'bestfit.jerry.wu@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/AccessRetrieved/PyGui',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AccessRetrieved/PyGui/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['pygui', 'PyGui', 'python', 'Python', 'easy', 'combined', 'modules'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pyautogui',
          'keyboard',
          'yagmail',
          'touchid',
          'tkinter',
          'rumps'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',    #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)