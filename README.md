# DynaArm Software Documentation

[![build-and-deploy](https://github.com/Duatic/dynaarm_software_documentation/actions/workflows/build-and-deploy.yml/badge.svg)](https://github.com/Duatic/dynaarm_software_documentation/actions/workflows/build-and-deploy.yml)

This contains the documentation for the DynaArm software. \
The deployed documentation can be read at [dynaarm.duatic.com](https://dynaarm.duatic.com). 
The current state on the `main` branch is automatically published to github pages.

## License

This repository is under [Apache License 2.0](./LICENSE)

## Dependencies 

You will need several python3 requirements. You can either install them via the `requirements.txt` and pip install or if you are on a Debian based system you can also install them via apt:

```
sudo apt install python3-sphinx python3-sphinx-rtd-theme python3-sphinx-copybutton
```

__NOTE:__ You only need these dependencies if you want to build the documentation locally.\
Building the documentation locally is recommended for testing.



## Workflow

In order to update the documentation please follow the following workflow.

#### 1. Do your changes

Just do the changes you want to do. ReStructured Text (RST) in combination with sphinx needs a bit of time to get used to but is very powerfull in the end.

#### 2. Build the view your local state

In the root folder of the repository run:

```
make html
```

Sphinx will tell you if the current state is valid.

In order to view it then just open the `index.html` with your favourite browser. For firefox this would be:

```
firefox build/html/index.html  
```

#### 3. Create a new branch and push your changes to it

You should always create a new branch for your changes and create a pull-request on github.\
This way you can test that the CI pipeline can actually build your current state.

__NOTE:__ The CI pipeline performs only the build but not the publish step for PRs. 

__WARNING:__ Be careful with changing the CI pipeline. You may accidentially publish the contents of your current branch to github pages.


#### 4. Merge the changes to main

If the PR is built successfully (and in the best cased reviewed) you can merge it to main.

__NOTE:__ The current state on the `main` branch will be automatically published to github pages

