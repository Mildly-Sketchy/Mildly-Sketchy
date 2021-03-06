# Opportune

**Author**: Kat Cosgrove, Gene Pieterson, Patricia Raftery, Austin Matteson
**Version**: 1.4.1

## Overview

Opportune is a web application that uses a web scraper and keywords from the user to find jobs in their area related to their chosen search terms. To use, the user must register or log in, choose their location and job keywords, and Opportune will email to them a list of 20 job postings within their specifications. Their results will also be displayed on their profile page. At any time the user can go back and search again, with different keywords/city, or if they use the same they will not get the same job postings again. The user has the ability to delete or add keywords, change their email, or fully delete their account. Data analysis is displayed to the user on salaries for different keyword searches.

## How It Works

This application returns 30 job postings to the user on submit of their location and keyword preferences. It does this by using Beautiful Soup to scrape Indeed.com. The results are stored in a csv file and emailed to the user, and also displayed on their profile page. Data analysis is done on common keyword searches in Seattle comparing salaries using Jupyter Notebook and Bokeh.

## Getting Started

To replicate this app, you would fork and clone our GitHub https://github.com/Mildly-Sketchy/Opportune. Then you would need to start a virtual environment, install the packages to get the dependencies used in this app, and have 3 empty databases set up.

## Architecture

Three SQL databases are used for persistence to store job postings and user data. Pyramid is used for the framework, and the web scraper used is Beautiful Soup. Other technologies used are Python3, Travis CI, Jupyter notebook, pandas, Bokeh, HTML, CSS, and JavaScript. Heroku is used for deployment.

## Change Log

#### Prework

04/10/2018 1400 - Discussed project ideas

04/11/2018 1400 - Selected project idea

04/12/2018 1400 - Did wireframes and planning

04/13/2018 1400 - Created repository

04/13/2018 1400 - Created front-end mock-ups

04/15/2018 1400 - Created Pyramid framework

#### Day 1

04/16/2018 1000 - Deployed scaffolded site with Heroku

04/16/2018 1100 - Travis CI utilized

04/16/2018 1200 - CSV with test data can be successfully emailed to the user

04/16/2018 1300 - Databases dropped and rebuilt

04/16/2018 1400 - Update gitignore

04/16/2018 1430 - Basic web scraper functionality achieved within a jupyter notebook

04/16/2018 1500 - Web scraper transfered to the proper file in Pyramid, still works

#### Day 2

04/17/2018 0900 - Keywords can be stored in the SQL database

04/17/2018 0930 - Web scraper now accepts keywords stored in the database

04/17/2018 1030 - Web scraper can accept a single city and multiple job keywords

04/17/2018 1130 - Basic tests written for views, coverage at 54%

04/17/2018 1245 - Keywords can be deleted from the database

04/17/2018 1330 - Dummy data file created for testing scraper, using the data from Indeed with the python keyword

04/17/2018 1430 - The user can add keywords to their account, they display on their profile page, and can be selectively deleted

04/17/2018 1500 - Test for web scraper works. Test uses monkey patch to direct the scraper to the dummy data

04/17/2018 1600 - User's results are written to a csv and displayed on the profile page

04/17/2018 1700 - More styling and formatting done on the front end to make buttons look more appealing, improve organization

#### Day 3

04/18/2018 0900 - Merge developmenent branch to master branch, redeploy

04/18/2018 1030 - The user can update their email address or delete their entire account

04/18/2018 1130 - Front end styling for search page

04/18/2018 1230 - Testing with fake authenticated user can post keywords, passes

04/18/2018 1300 - Tests broken up in to different files

04/18/2018 1400 - Data Analysis for different properties of dev related keywords

#### Day 4

04/19/2018 0900 - 401 redirect for bad login caught, scraper now returns job summaries

04/19/2018 1000 - Small UI issues corrected, admin permissions for analytics page in place

04/19/2018 1100 - Forbidden view and existing username tests added

04/19/2018 1200 - Mass scraper notebook with CSV files added

04/19/2018 1300 - Data analysis done on the user's keyword searches and is displayed to the user's profile

04/19/2018 1400 - Test coverage is 85%

04/19/2018 1600 - Test coverage is 95%

04/19/2018 1800 - About Us page, pictures and descriptions added, styling done

#### Day 5

04/20/2018 0900 - Bug fixes with scraper and email

04/20/2018 1000 - LinkedIn and GitHub links added to About Us page, better styling done

04/20/2018 1400 - Presentation
