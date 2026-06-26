# Render Deployment Guide

This guide explains how to deploy your `StudentProject` API on Render as a live web service.

---

## Step 1: Push your Code to GitHub

Before deploying on Render, you need to push your project to a Git repository (like GitHub):
1. Create a new repository on GitHub.
2. Initialize and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initialize student project with Render support"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

---

## Step 2: Create a Web Service on Render

1. Log in to [Render](https://render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub account and select your `StudentProject` repository.

---

## Step 3: Configure Web Service Settings

Configure the web service with the following settings:

- **Name**: `student-api` (or any name you prefer)
- **Environment**: `Python 3`
- **Region**: Select the region closest to your users (e.g., Singapore, Oregon, Frankfurt)
- **Branch**: `main`
- **Root Directory**: `Month-1/Week-3/Day-4/Assignments/StudentProject` (This tells Render where `manage.py` and `requirements.txt` are located)
- **Runtime**: `Python`
- **Build Command**: `./build.sh` (We created this file to automatically run migrations and collect static files)
- **Start Command**: `gunicorn StudentProject.wsgi:application`

---

## Step 4: Configure Environment Variables

Click the **Advanced** button or go to the **Environment** tab on Render and add the following variables:

1. `SECRET_KEY` = `your-custom-production-secret-key-here` (generate a long random string)
2. `DEBUG` = `False` (disables debug mode for production)
3. `PYTHON_VERSION` = `3.12.4` (optional: ensures Render uses the same Python version you tested with)

### (Optional) Database Setup: SQLite vs PostgreSQL
- **SQLite (Default)**: By default, the app will run with SQLite, but note that SQLite files are deleted whenever the service restarts on Render because the disk is ephemeral.
- **PostgreSQL (Recommended)**: To store data permanently:
  1. Click **New +** on Render and select **PostgreSQL**.
  2. Once the PostgreSQL database is created, copy its **Internal Database URL** or **External Database URL**.
  3. Go back to your Web Service **Environment** page and add a new environment variable:
     - Key: `DATABASE_URL`
     - Value: `postgres://<username>:<password>@<host>/<database>` (paste the URL you copied)
  4. Our `settings.py` is preconfigured to automatically detect `DATABASE_URL` and use PostgreSQL if the variable exists!

---

## Step 5: Deploy!

Click **Create Web Service** at the bottom of the page. Render will build the image, run migrations, compile static files, and start Gunicorn. Once the build is complete, you will get a public URL (e.g., `https://student-api.onrender.com`).

You can test your endpoints:
- **GET All (with Pagination)**: `https://student-api.onrender.com/api/students/`
- **GET Single**: `https://student-api.onrender.com/api/students/1/`
- **POST/PUT/DELETE**: `https://student-api.onrender.com/api/students/` and `https://student-api.onrender.com/api/students/1/`
