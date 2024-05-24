# -*- coding: utf-8 -*-
"""09 applied python: git, github, pip, streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SJQ0uiUIjozDMq9qRYvE2oIE2iHXOP7M

# **A Humorous Stroll Down Memory Lane of Source Control**

#### **Introduction**

```
Three things are certain:
Death, taxes, and lost data.
Guess which has occurred.
```

```
Having been erased,
The document you're seeking
Must now be retyped.
```

_**Context**: These haikus humorously highlight a truth in software development: losing data is almost inevitable, and retyping and rethinking is costly_


#### **Part 1: The Days Before Source Control**

- **The Tale of Lost Code**
  - **Anecdote**: Imagine a student, let's call him Alex. Alex had been working on his final project for weeks. The night before submission, in a bid to clean up his code, he accidentally deleted a crucial file. No backup, no version control. Panic ensued, followed by a sleepless night of trying to rewrite everything from memory.

- **Early Version Control Methods**
  - **Emailing Source Code**: There was a time when students like Alex would email themselves the latest version of their code. Subject lines like "Final_project_v3", "Final_project_v3.1_slightly_better" were a common sight, leading to an inbox more cluttered than their dorm rooms.
  - **The Zip File Strategy**: Others, like Alex's classmate Sarah, resorted to saving multiple zip files on their desktop. "Project_final.zip", "Project_really_final_this_time.zip", only to realize later that "Project_final_revision2.zip" was actually the one they needed.

#### **Part 2: Source Control - The Savior**

- **Shortcomings of Primitive Methods**
  - These early methods, while creative, were fraught with problems. They were inefficient, made tracking changes a nightmare, and were useless when it came to understanding what exactly changed between versions.

- **The Nightmare of Group Projects**
  - **Group Project Anecdote**: Consider a group project where each member, like Alex and Sarah, works in isolation. As the deadline looms, they realize their parts of the project are incompatible. The final days are spent in a frantic effort to stitch together disparate pieces of code, a task akin to assembling a puzzle without the picture on the box.

#### **Part 3: The Evolution of Source Control Tools**

- **From CVS to Git**
  - In the early days, source control was rudimentary. **CVS (Concurrent Versions System)** was a breakthrough, allowing developers to work simultaneously on different parts of the code. However, its centralized model was its Achilles' heel.
  - Then came **Subversion**, which fixed many of CVS's flaws but still clung to the centralized approach.
  - **Microsoft's SourceSafe** was another player, infamous for its issues with data corruption.
  - **BitKeeper** emerged, offering distributed version control, but its cost and proprietary nature were barriers.
  - Finally, **Git** arrived on the scene. Developed by Linus Torvalds for Linux kernel development, Git's distributed model, speed, and efficiency made it a game-changer. It allowed for branching and merging with unprecedented ease, revolutionizing source control.

#### **Part 4: Why Git and GitHub?**

- **Advantages of Git**
  - Git, unlike its predecessors, allows for local repositories, enabling developers to work offline and then sync with the central repository. Its branching capabilities mean that you can work on different features simultaneously without affecting the main codebase.
  - **GitHub** takes Git to the next level, providing a web-based platform for hosting repositories. It also adds features like issue tracking, code review, and a social networking-like environment for developers.

## **GitHub: The Powerhouse of Open Source Launchpads**


> GitHub has emerged as an indispensable tool in the world of open source development, functioning far beyond a mere repository for code. It's a dynamic launchpad for a plethora of services, seamlessly integrating the processes of developing, testing, and deploying applications, web pages, APIs, and more. With features like GitHub Pages, developers can transform their code into live websites in minutes. The platform's robust support for Continuous Integration and Deployment (CI/CD) pipelines automates the build and deployment process, ensuring that applications are updated smoothly and efficiently. GitHub Actions further streamline workflow automation, allowing for a seamless transition from code to deployment. By offering plug-and-play integration with major cloud services like Azure, AWS, and Google Cloud, GitHub simplifies the deployment process, making it more accessible and efficient. This synergy of code management and DevOps practices within GitHub not only accelerates project development but also fosters real-time collaboration and community feedback, crucial for the iterative improvement of open-source projects. In essence, GitHub stands as the nexus where code evolves into fully-fledged applications, embodying the spirit and dynamism of the open-source community.

- **GitHub: Open Source's Launch Control**: It's the command center for app deployment and more.
- **Seamless Integrations**: Think launching apps, websites, APIs. Click, connect, deploy.
- **GitHub Pages**: Websites live in minutes. Code in GitHub, website on the web.
- **CI/CD Pipelines**: Push code. Automatic build and deploy. Smooth, no sweat.
- **APIs in a Snap**: Code it. Push it. Your API is up and running.
- **GitHub Actions**: Automate everything. Test, build, deploy. Like clockwork.
- **Plug-and-Play Services**: Connect to cloud platforms. Azure, AWS, Google Cloud.
- **Open Source Meets DevOps**: GitHub is where code becomes product. Fast, efficient, integrated.
- **Real-Time Collaboration**: Code together, fix bugs faster, launch quicker.
- **Community Feedback Loop**: Launch, get feedback, iterate. Community-driven improvements.

>GitHub isn't just a repository; it's an open-source launchpad. Code, collaborate, launch - all in one place.


In the realm of Machine Learning (ML), GitHub has become a vital intersection for various services and platforms, enhancing the development and deployment of ML models. Notable integrations with GitHub in the ML landscape include Hugging Face, Streamlit, and Gradio, each offering unique capabilities that streamline ML workflows.

### GitHub in Machine Learning: Key Integrations

- **Hugging Face + GitHub**:
  - Plug into advanced NLP models.
  - Share, version, and improve ML models.
  - Open-source AI community hub.

- **Streamlit's GitHub Connect**:
  - Turn code into interactive apps.
  - Direct GitHub sync for seamless updates.
  - Rapid prototyping, instant sharing.

- **Gradio on GitHub**:
  - Create ML demos from repositories.
  - Quick, easy UI for ML models.
  - Collaborate, showcase, and get feedback.

Certainly! Besides Hugging Face, Streamlit, and Gradio, there are other notable services and tools that integrate with GitHub to enhance machine learning workflows:

- **TensorFlow and Keras**:
  - Directly access and manage TensorFlow and Keras models on GitHub.
  - Collaborate on deep learning projects with ease.

- **Jupyter Notebooks**:
  - Host, view, and share Jupyter notebooks on GitHub.
  - Essential for ML experimentation and documentation.

- **Weights & Biases**:
  - Track and visualize machine learning experiments.
  - Seamlessly integrate experiment tracking with GitHub repositories.

- **Docker**:
  - Containerize ML models and environments.
  - Deploy consistently across various platforms.

- **MLflow**:
  - Manage the ML lifecycle, including experimentation, reproducibility, and deployment.
  - Integrate with GitHub for tracking ML project versions.

These services, when combined with GitHub's robust platform, offer a comprehensive ecosystem for managing, tracking, and deploying machine learning projects, enhancing collaboration and efficiency in the ML community.

These integrations transform GitHub into a powerhouse for ML development, offering tools for everything from model sharing and app creation to interactive demonstrations and community engagement.

### **Understanding Git Add and Commit**

#### **Git Add**
The `git add` command is your way of telling Git which changes in your working directory you want to include (or 'stage') for the next commit. It's about preparing a snapshot of your files to be saved in the repository.

- **How It Works**: When you modify files, those changes are only in your working directory. To include these changes in your next commit, you first need to `add` them.
- **Usage**:
  - To stage a specific file: `git add <filename>`
  - To stage all changes in your current directory: `git add .`

#### **Git Commit**
After staging your changes with `git add`, the next step is to `commit` them. A commit is like taking a snapshot of your staged changes, preserving a record of exactly how your directory looked at that moment.

- **Best Practices**: Each commit should be a logically separate change. This makes it easier to understand the history of your project and to roll back or isolate specific changes if needed.
- **Commit Messages**: Writing good commit messages is crucial. A commit message should briefly summarize the change. This helps you and others understand the purpose of each change later on.
- **Usage**: `git commit -m "Your informative commit message"`

### **Understanding Git Push and Pull**

#### **Git Push**
`git push` is used to upload your local repository content to a remote repository. This is how you share your commits with others or backup your work to a remote server.

- **Remote Repositories**: Before you can push, you need to have a remote repository set up. GitHub, GitLab, and Bitbucket are common platforms for hosting remote repositories.
- **Usage**: After committing your changes, use `git push origin <branch_name>` to push them to the remote repository. The `origin` is a shorthand for the remote repository's URL, and `<branch_name>` is the branch you are pushing to.

#### **Git Pull**
Conversely, `git pull` is used to fetch and download content from a remote repository and immediately update your local repository to match that content.

- **Syncing Changes**: If others have made changes to the remote repository, you use `git pull` to get those changes. This is essential for collaborative work.
- **Avoiding Conflicts**: Regularly pulling helps avoid conflicts between your local changes and changes made by others.
- **Usage**: `git pull origin <branch_name>` will fetch changes from the specified branch of the remote repository and merge them into your current branch.

### **In GUI Interfaces**
Most GUI-based Git tools abstract these commands into buttons or menu options but fundamentally perform the same actions. Understanding what happens behind the scenes helps you use these tools more effectively and troubleshoot issues when they arise. For example, clicking a 'Commit' button in a GUI tool typically stages and commits the selected files in one step.

### **Conclusion**
Mastering these fundamental Git commands is key to efficient version control and collaboration. They form the core actions you'll perform regularly, whether directly in the command line or through a GUI tool.

# Download & install

- Github desktop - https://desktop.github.com/
- git command line - https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.2/Git-2.42.0.2-64-bit.exe
  > homepage https://git-scm.com/
- github.com - please create an account

### Step-by-Step Guide to Creating Your First Public Repository on GitHub

#### **Step 1: Log In to GitHub**
- **Access GitHub**: Open your web browser and go to [GitHub](https://www.github.com).
- **Sign In**: Use your GitHub username and password to log in. If you don’t have an account, you’ll need to sign up.

#### **Step 2: Start a New Repository**
- **Navigate to Repositories**: On the GitHub homepage, look for the "Repositories" tab or section.
- **Create New Repository**: Click the `New` button, usually found near the top right corner of the "Repositories" section.

#### **Step 3: Configure Your Repository**
- **Repository Name**: Enter a name for your repository. This should be descriptive and ideally indicate the purpose or content of the repository.
- **Description (Optional)**: Provide a brief description of your repository. This helps others understand what your project is about.
- **Public Repository**: Select the ‘Public’ option. This means anyone on the internet can see your repository. You can still choose who commits to your repository.
- **Initialize Repository**: Check the box next to "Initialize this repository with a README". This is recommended as it provides a starting point and information about your project.
- **Add .gitignore (Optional)**: Choose the `python` .gitignore

- ~**Choose a License (Optional)**: If you want to make it clear how others can use your code, select a license from the dropdown.~

#### **Step 4: Create the Repository**
- **Create Repository**: Click the `Create repository` button. GitHub will set up your new repository and take you to its page.

#### **Step 5: Explore Your Repository**
- **Repository Layout**: Familiarize yourself with the layout of your repository. You’ll see your README file displayed (if you opted to create one), along with tabs for "Code," "Issues," "Pull Requests," etc.
- **Clone or Download**: To work on your project locally, you can clone your repository to your computer using the URL provided.

#### **Step 6: Making Changes and Committing (Optional)**
- **Edit Files**: You can start by editing your README file on GitHub itself to add more details about your project.
- **Commit Changes**: After editing, commit your changes directly on GitHub by typing a commit message and clicking the commit button.

### **Conclusion**
Congratulations! You have created your first public repository on GitHub. This repository is now ready for you to add more files, collaborate with others, and start building your project. Remember, GitHub repositories are not just for code; they can host a variety of content, including documentation, data, and more.

### GitHub Desktop: A Step-by-Step Guide

#### **1. Installation and Setup**
- **Download**: Visit the [GitHub Desktop website](https://desktop.github.com/) and download the installer for your operating system (Windows or macOS).
- **Install**: Run the installer and follow the on-screen instructions to install GitHub Desktop.
- **Sign In**: Open GitHub Desktop. Sign in with your GitHub credentials. If you don’t have a GitHub account, you’ll need to create one.

#### **2. Configuring GitHub Desktop**
- **Set Up Git**: After signing in, go to `File` > `Options` (or `GitHub Desktop` > `Preferences` on Mac). Set your Git `Name` and `Email`. This is important as every commit you make will use this information.
- **Configure Default Branch**: In the same `Options` or `Preferences`, you can set the default branch name for new repositories (commonly `main`).

#### **3. Cloning a Repository**
- **Clone an Existing Repository**: Click on `File` > `Clone Repository`. You can choose a repository from your list on GitHub or enter a URL for any repository you have access to. Select a local path to save the repository.
- **Open in Editor**: Once cloned, you can open the repository in your preferred text editor or IDE directly from GitHub Desktop.

#### **4. Making Changes and Committing**
- **Change Files**: Open your project in your code editor and make your changes.
- **Review Changes**: Back in GitHub Desktop, go to the `Changes` tab. You’ll see a list of modified files. Click on a file to see a diff of the changes.
- **Commit Changes**: Write a commit message summarizing your changes and click `Commit to [your-branch]`.

#### **5. Syncing with Remote**
- **Fetch and Pull**: Before pushing your changes, it’s good practice to fetch and pull from the remote repository to ensure you have the latest changes. Click `Repository` > `Fetch origin`. If there are changes, `Fetch` will change to `Pull`. Click it to update your local repository.
- **Push Changes**: Click the `Push origin` button to upload your commits to the remote repository on GitHub.

#### **6. Creating and Managing Branches**
- **Create a New Branch**: Click the `Current Branch` dropdown at the top. Click `New Branch`, name your branch, and create it. Optionally, you can choose to create the branch based on another branch.
- **Switch Between Branches**: Use the `Current Branch` dropdown to switch between your branches.

#### **7. Merging Branches**
- **Merge into Another Branch**: To merge changes from one branch to another, switch to the branch you want to merge into. Click `Branch` > `Merge into Current Branch`. Select the branch you want to merge from and confirm.

#### **8. Pull Requests**
- **Open a Pull Request**: After pushing a branch, click the `Create Pull Request` button. This opens GitHub in your web browser, where you can fill out the pull request details and submit it.

### **Conclusion**
GitHub Desktop streamlines the Git workflow with a user-friendly interface, making version control more accessible, especially for those who prefer graphical interfaces over command-line tools. Remember, the best way to learn is by doing, so feel free to explore and experiment with different features as you get more comfortable with the tool.

# Your Turn: Collaborative GitHub Exercise for Two Students

#### **Objective**
The goal of this exercise is to familiarize yourself with basic Git and GitHub operations, including cloning a repository, making and committing changes, pushing and pulling updates, and collaborating through GitHub. This exercise involves using GitHub Desktop and PyCharm.

#### **Setup**
1. **Student A** creates a new public repository on GitHub, named "test".
2. **Student A** adds a simple Python script, `main.py`, with a basic print statement (e.g., `print("Hello, world!")`).
3. **Student A** invites **Student B** as a collaborator to the repository (Settings > Collaborators > Invite a collaborator).

![setup](https://awesomescreenshot.s3.amazonaws.com/image/1882885/44349167-57879106f898839b745a7d414e38df17.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231119%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231119T181155Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=037a17c77265906305f1be58c6aa1c31b7a906df92c77b59a4f6ca29b698b221)
#### **Exercise Steps**

##### Part 1: Initial Setup
1. Both students clone the repository using GitHub Desktop.
   - on `github.com` Use the green `code` button and selection "clone in github desktop"  option
   - clone the repo.
2. Open the cloned repository in PyCharm.

##### Part 2: Making Changes
1. **Student B** modifies `main.py` by adding another print statement (e.g., `print("This is a collaborative project!")`).
2. **Student B** commits the changes using GitHub Desktop.
   - Review the changes in the 'Changes' tab.
   - Write a commit message describing the change.
   - Click 'Commit to main'.

##### Part 3: Syncing Changes
1. **Student B** pushes the changes to the remote repository using GitHub Desktop.
   - Click 'Push' to push the commit to GitHub.
2. **Student A** fetches and pulls the changes.
   - Click 'Fetch' followed by 'Pull' in GitHub Desktop.
   - The changes made by Student B should now be visible in `main.py` in PyCharm.

##### Part 4: Adding New Content
1. **Student A** adds a new Python file, `feature.py`, with a simple function (e.g., a function that returns a greeting).
2. **Student A** commits and pushes the new file using the same process as Student B.

##### Part 5: Final Collaboration
1. **Student B** pulls the new changes made by Student A.
2. **Student B** modifies `feature.py` by adding another function or modifying the existing one.
3. **Student B** commits and pushes the changes.
4. **Student A** pulls the final changes.

#### **Conclusion**
Through this exercise, both students will have practiced the fundamental collaborative features of Git and GitHub. They will have experienced firsthand the process of cloning a repository, making changes, committing and pushing those changes, and pulling updates made by others. This exercise sets a foundation for more complex collaborative projects using Git, GitHub, and PyCharm.

---

### Pip and PyPI: An Overview

![pip](https://awesomescreenshot.s3.amazonaws.com/image/1882885/44349511-061dcbce687665944cf261ca8a380fdf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231119%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231119T190528Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=cef0957cd8b2af8920f32b6f95937648531076083cd86c63c9d1b687f7a9d262)

**PyPI (Python Package Index)** is an online repository where developers share open-source Python modules. It's a vast library of community-contributed packages, ranging from simple utilities to complex frameworks. PyPI plays a central role in the Python ecosystem, providing an accessible platform for distributing Python software.

**Pip** is the default package manager for Python, allowing users to install, update, and manage packages from PyPI. It's a command-line tool that automates the process of managing Python packages. Pip communicates with PyPI to fetch and install packages into your Python environment.

#### How It Works
- Developers upload their Python packages to PyPI.
- Users use pip to download and install these packages.

#### Basic Pip Commands
- **Installing a Package**: To install a package like Streamlit, you use:
  ```bash
  pip install streamlit
  ```
- **Listing Installed Packages**: To see what packages are installed:
  ```bash
  pip list
  ```
- **Uninstalling a Package**: To remove an installed package:
  ```bash
  pip uninstall streamlit
  ```

In summary, PyPI serves as the central hub for Python packages, and pip is the tool that makes it easy to install and manage these packages. Together, they greatly simplify the process of extending Python's capabilities with community-developed modules.

---

# Your first streamlit application
![23](https://awesomescreenshot.s3.amazonaws.com/image/1882885/44349189-3bba962b2522277fb7c39326d4fec8bd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231119%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231119T181551Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=3931056b30db6b32968e5f5337837f0f8302126d085fcef8079accd79098fd0b)

### Step 1: Set Up Your Development Environment

2. **Install Streamlit**: Open your command line or terminal and install Streamlit using pip:
   ```bash
   pip install streamlit
   ```

### Step 2: Create Your Streamlit App

1. **Create a Python File**: Create a new Python file for your app, call it `main.py`.

2. **Write the Streamlit Code**: Open the file in a text editor or IDE and write the following code:
   ```python
   import streamlit as st

   st.title('Hello Streamlit!')

   name = st.text_input("What's your name?")

   if name:
       st.write(f"Hello, {name}!")
   ```

### Step 3: Run the App Locally

1. **Run the App**: Open your command line or terminal, navigate to the folder where your `main.py` file is located, and run:
   ```bash
   streamlit run main.py
   ```
2. **View the App**: Your default web browser should open automatically with your running Streamlit app. If not, the terminal will provide a local URL you can use to view it.

### Step 4: Deploy Your App on the Web

To deploy your Streamlit app, you can use Streamlit sharing, which is a free and easy way to deploy, manage, and share your Streamlit apps.

1. **GitHub Repository**:
   - Push your Streamlit app (`hello_streamlit.py`) to a new GitHub repository.
   - Make sure your repository is public.

2. **Sign Up for Streamlit Sharing**:
   - Go to [Streamlit sharing](https://streamlit.io/sharing) and sign up with your GitHub account.

3. **Deploy Your App**:
   - Once signed up, click ‘New app’, then select your GitHub repository, branch, and the path to your Streamlit app.
   - Click ‘Deploy’ and Streamlit will start deploying your app.

4. **Access Your Web App**:
   - After deployment, Streamlit provides a URL to access your app.
   - Share this URL to let others view and interact with your Streamlit app.

# further reading streamlit

> https://docs.streamlit.io/library/api-reference/status

Streamlit offers a wide array of functionalities that can enhance even simple Python scripts, turning them into interactive web applications. Below are some cool methods you can use in Streamlit that don't require knowledge of Pandas, along with a small exercise idea.

### Cool Streamlit Methods (No Pandas Required)

1. **Text Input (`st.text_input`)**:
   - Collect text input from the user. Great for getting user feedback, names, or any short text.

2. **Slider (`st.slider`)**:
   - Let users select a number from a range. Ideal for parameters like age, rating, or any configurable setting.

3. **Button (`st.button`)**:
   - Execute actions when a user clicks a button. Useful for submitting forms or triggering functions.

4. **Select Box (`st.selectbox`)**:
   - Drop-down menu for options. Perfect for choices like cities, categories, or yes/no questions.

5. **Radio Buttons (`st.radio`)**:
   - For selecting one option from a set. Good for multiple-choice questions or preferences.

6. **Checkbox (`st.checkbox`)**:
   - Let users enable or disable an option. Useful for toggles or agreeing to terms.

7. **Write (`st.write`)**:
   - Display text, numbers, or even charts. It’s a versatile way to output data or messages.

### Small Exercise: Personalized Greeting App

**Objective**: Create an app that asks the user for their name and favorite color and then displays a personalized greeting in their chosen color.

#### Steps:

1. **Ask for User Input**:
   - Use `st.text_input` to get the user’s name.
   - Use `st.selectbox` or `st.radio` to let the user select their favorite color from a predefined list (e.g., Red, Blue, Green).

2. **Display a Greeting**:
   - Use `st.write` to show a personalized greeting, like “Hello [name]!”.

3. **Color Customization**:
   - Customize the color of the greeting text based on the user’s color choice. This can be achieved by using Streamlit’s `st.markdown` method with some inline CSS for color styling.

4. **Add a Button** (Optional):
   - Use `st.button` to create a 'Show Greeting' button. Display the greeting only when this button is clicked.

#### Example Code:

```python
import streamlit as st

st.title("Personalized Greeting App")

name = st.text_input("Enter your name:")
color = st.selectbox("Choose your favorite color:", ["Red", "Blue", "Green"])

if st.button("Show Greeting"):
    st.markdown(f"<h1 style='color: {color};'>Hello, {name}!</h1>", unsafe_allow_html=True)
```

**Exercise Outcome**: This simple exercise demonstrates how Streamlit can turn a basic Python script into a more engaging, interactive web application. It shows the use of different input methods and dynamic content display, making it an excellent introduction to Streamlit's capabilities without the need for complex data processing.
"""

