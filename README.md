# qalypso_2022
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CQCL/qalypso_2022/HEAD)

Repository for presentations, notebooks and hackathon exercises from the Qalypso summer school 2022

Join our [slack channel](https://tketusers.slack.com/join/shared_invite/zt-18qmsamj9-UqQFVdkRzxnXCcKtcarLRA#/shared-invite/email)!

## Running the contents of these notebooks
There are a number of ways to execute the notebooks, here are three suggested in
order of most to least environmental set up done for you.

1. Use the "launch binder" link at the top of this README, a jupyter lab
   instance will open in your browser from which the notebooks can be run.
2. The binder instance is running on a docker image (`seyonsivarajah224/hackathon:latest`) with all the dependencies
   installed. If you install Docker on your system, you can run it locally.
   First clone this repository, then navigate to the repository in your shell
   and execute the command
   ```

   docker run -it --rm -p 8888:8888 -v "$PWD":/home/jovyan/work seyonsivarajah224/hackathon:latest jupyter notebook work --NotebookApp.default_url=/lab/ --ip=0.0.0.0 --port=8888
   ```
   You can then use jupyter lab normally in your browser.

3. Create a python virtual environment in your system and install the
   dependencies yourself, see tket_intro.md. WARNING: check that you are on a
   suitable operating system, have a compatible python version (3.8, 3.9, 3.10), and any possible
   binary libraries required installed on your system (e.g. graphviz).

## Useful Links

- [Pytket User manual](https://cqcl.github.io/pytket/manual/index.html)
- [Pytket API docs](https://cqcl.github.io/tket/pytket/api/)
- [Pytket Notebook Examples](https://github.com/CQCL/pytket/tree/main/examples)