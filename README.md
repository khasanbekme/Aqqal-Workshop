# Flowise Agent Setup Guide

Welcome to the Flowise Agent setup guide. Follow these steps to set up your agent and integrate it with Telegram using Aiogram. This guide assumes you have basic familiarity with Python and Telegram bots.

## Prerequisites

-   Python installed on your system
-   A Telegram account

## Setup Instructions

1. **Access Flowise Dashboard**:

    - Navigate to [flowise.aqqal.com](https://flowise.aqqal.com).
    - Log in using the username: `suleiman` and password: `andrew@cmu`.

2. **Create a New Agent**:

    - Once logged in, create a new agent.
    - Ensure the agent is operational by checking its status on the dashboard.

3. **Install Aiogram**:

    - Open your terminal or command prompt.
    - Install the Aiogram package by running the command:
        ```
        pip install aiogram
        ```

4. **Configure API URL**:

    - Copy the `FLOWISE_API_URL` from your dashboard.
    - Paste this URL into the provided Python code where indicated.

5. **Create a Telegram Bot**:

    - Open Telegram and search for [`@BotFather`](https://t.me/BotFather).
    - Follow the prompts to create a new bot. You will receive a `BOT_TOKEN`.

6. **Update Python Code**:

    - Paste the `BOT_TOKEN` into the provided Python code in the designated area.

7. **Run the Python Code**:
    - Execute the Python code.
    - If the Telegram bot responds "CONGRATULATIONS!!!", the setup is successful.
    - If you encounter issues, revisit Step 1 and ensure all steps were followed correctly.
