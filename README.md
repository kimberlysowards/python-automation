### Kim's Notes
---
1. Use Ctrl+` to open up Command Line inside VSCode
2. Install dependencies: `pip install`, and more...
3. More notes.. to come...

### How to Save Changes
1. Make change to any file
2. Check git gui




# Welcome to the python-automation Repo!
This is a public repo that is meant for anyone to join in and collaborate on. The goal is simple: Create a Test Automation Framework to test as many of the League of Legends websites like lolesports.com.

This is primarily for the participants at **QA at the Point** and all communication is done in our Slack group called **QA Utah**. If you are not actively at QA at the Point or live in Utah, you are still very much welcome to join in! Also, feel free to reach out to me if you'd like to be invited to the QA Utah Slack group.

Each participant is called an "Autobot" and so our channel is called `#autobots` on Slack.


## How do I get started?
First, you need to have Python 3.x installed. Simply go here: https://www.python.org/downloads/ to download and install.

Create a `Dev` directory on your "root" and then `fork` or `clone` the repo down into your newly created directory and get started!

- Windows: `C:/Dev`
- Mac: `/users/carlos/Dev`
    
NOTE: Everyone in training has been told to use **VS Code**, but you can use any IDE like PyCharm.

Open this project in your terminal and run the following command:
- `pip install -r requirements.txt` for Windows
- `pip3 install -r requirements.txt` for Mac and Linux (assuming you've installed Python 3.6+)

This will grab the necessary packages that are required like Selenium and Pytest.


## Running the tests
We use **Pytest** to run our tests. In the command-line, simply run `pytest <path-to-file>` to run the tests within the file.

There are currently two main test suites in the **Tests** directory, but each is easy to run:
- esports.py - `pytest tests/esports.py`
- api.py - `pytest tests/api.py`

There are also Performance Tests using Locust. This is the `locustfile.py` under the **Tests** directory. Follow the instructions in that file to get them up and running. Please be careful when running the Locust Swarm. You can run thousands of users at once, but please use these only on non-critical websites you own so you don't accidentally bring someone's site down and get in trouble.


## What can I work on?
All of the work is being tracked in the `Issues` tab. Autobots are using a very simple Kanban board, but all work is divided into Issues with labels. The Label System should be used and adhered to:

1. Any work being done should be recorded as an Issue. If there is no Issue tied to what you are working on, create one! Label it with the appropriate `type` and give it as much detail so you can mark it as `ready`.
2. Each Issue should have a solid `Title`, `Description`, and `Acceptance Criteria`. If not, it will be marked with the `more info` label and any PRs from it will be denied.
3. Each Issue should have at least one `type label` and `status label`.

#### Status Labels:
- `changes requested`
- `code review`
- `help wanted`
- `in progress`
- `more info`
- `ready`
    
#### Type Labels:
- `bug`
- `enhancement`
- `test`
    
4. Once the Issue is created, start working on it! Create a branch where you will make your changes (or work in your fork), and once you feel satisfied that you've met all Acceptance Criteria, submit a `Pull Request` (PR) and assign Carlos aka `ElSnoMan` as the Reviewer.
*Do not touch `master` in any situation without Admin approval. Do not pass Go and collect $200. Offenders will be removed from the repo.*


## Tracking Issues with the Label System
Issues are used to track the work being done, especially when there are multiple people working on it. The Label System is simple and makes it easy to know what is being worked on, what's in the backlog, and what the status for those tickets are.

### Type Label
The Issue Type should be the very first label that is added to an Issue.

1. `bug` - Any bugs found in our code and/or tests should be labeled with the `bug` type
2. `enhancement` - Any refactoring, editing, or additional code. Most Issues will be this type
3. `test` - A Test that needs to be written. These act like User Stories since they usually require 1 or more enhancements to be completed. Any new test or changes to existing tests should be labeled with the `test` type

### Status Label
What is the current status of the Issue? Use these as if there was not a Kanban board because not everyone has access to it. This is the bread and butter of the Label System and each Issue should be as "true" as possible at all times.

1. `changes requested` - only Admins should use this label. This means that `Code Review` is complete and your PR has been denied
2. `code review` - use this label once you have submitted your PR
3. `help wanted` - this is a `flag` that is used with a status. Use this anytime you need help with anything on your Issue. Need help writing better Acceptance Criteria or envisioning the finished product? Need help coding, debugging, or running into IDE issues? I would ask that you reach out to me after labeling with `help wanted`, otherwise I'll reach out to you once I see it.
4. `in progress` - this is actively being worked on by you. The Issue should also be assigned to you if it isn't already. If you start it and then let it go stale, please unassign yourself and put it back into the `ready` status.
5. `more info` - if your Issue requires more information to be completed, then this label will be used and other statuses will be removed.
6. `ready` - the Issue is ready to be worked on

### Example Issue Flow
1. I just came up with a cool idea for a test. I'll create the Issue and give it a title: "Test Foo".
2. Add `type: test` label
3. I give it as much information as I can but I'd like to review it with the team next Thursday. Add `more info` label
4. On Thursday we groom the Issue and give it the necessary info. Add `ready` label and remove `more info` label
5. I start working on it. Add `in progress` label and remove `ready` label
6. I run into a blocker and need someone's help. Add `help wanted` label and KEEP `in progress` label.
7. Carlos is awesome and we work through the blocker and finish the Issue and submit a PR. Add `code review` label and remove `in progress` label
8. Approved by Admin and archived. Woot!
