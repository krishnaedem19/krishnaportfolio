# Edem Krishna Chaithanya — Portfolio

A responsive portfolio web application built with:

- HTML5
- CSS3
- JavaScript
- Python
- Streamlit

All portfolio information in this version is based on the supplied resume. The supplied profile photo is included in `assets/profile.jpg`.

## 1. Project structure

```text
krishna_portfolio_streamlit/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── assets/
    ├── profile.jpg
    └── resume.pdf
```

## 2. Requirements

Install Python 3.10+ (Python 3.11 or 3.12 is a good choice).

Check Python:

```bash
python --version
```

## 3. Open the project in VS Code

1. Extract this ZIP file.
2. Open VS Code.
3. Select **File → Open Folder**.
4. Select the extracted `krishna_portfolio_streamlit` folder.

## 4. Create a virtual environment

Open the VS Code terminal:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

If PowerShell blocks activation, use Command Prompt in VS Code or run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the portfolio

```bash
streamlit run app.py
```

Streamlit will show a local address, normally:

```text
http://localhost:8501
```

Open that address in your browser.

## 7. How this project works

- `app.py` is the Python/Streamlit entry point.
- `templates/index.html` contains the portfolio structure and resume content.
- `static/style.css` contains the complete responsive design.
- `static/script.js` handles:
  - dark/light mode
  - mobile navigation
  - scroll reveal animations
  - current year
- `assets/profile.jpg` is the supplied profile image.
- `assets/resume.pdf` is the supplied resume.

`app.py` reads the HTML, CSS, JavaScript and image, then renders the website through Streamlit.

## 8. How to update GitHub and LinkedIn

The resume only lists "GitHub | LinkedIn" without the actual URLs.

Open:

```text
templates/index.html
```

Find the note about GitHub and LinkedIn and add the exact URLs when you have them. Do not replace them with guessed URLs.

## 9. How to change the profile photo

Replace:

```text
assets/profile.jpg
```

with your new image and keep the same filename.

Then restart Streamlit.

## 10. How to change portfolio content

Edit the relevant sections in:

```text
templates/index.html
```

Examples:

- About → `#about`
- Skills → `#skills`
- Education → `#education`
- Projects → `#projects`
- Certifications → `#certifications`
- Hackathons → `#activities`
- Contact → `#contact`

## 11. How to stop the server

In the VS Code terminal press:

```text
Ctrl + C
```

## 12. Common errors

### `streamlit is not recognized`

Use:

```bash
python -m streamlit run app.py
```

### `No module named streamlit`

Run:

```bash
pip install -r requirements.txt
```

### Wrong Python environment

Check:

```bash
python --version
where python
```

Then activate the project's virtual environment again:

```bash
venv\Scripts\activate
```

## 13. Deploy later

After testing locally, this project can be deployed to a Streamlit-compatible hosting service. Before public deployment, review the phone number and email address shown on the portfolio and decide whether you want them publicly visible.

## Resume information included

- Name and contact information
- Career objective
- Education and marks
- Technical skills
- Core subjects
- Soft skills
- FreshMart project
- SkillSphere project
- Certifications
- Workshops and hackathons

The portfolio intentionally does not invent GitHub/LinkedIn URLs because the supplied resume did not contain the actual profile links.
